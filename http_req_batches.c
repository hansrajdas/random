/* https://cirosantilli.com/linux-kernel-module-cheat#socket */
/* 
 * Source:
 * https://github.com/cirosantilli/linux-kernel-module-cheat/blob/b4b2164f29f3ae04ae9e3b7c0913ee8125910476/userland/posix/wget.c
 */

#define _XOPEN_SOURCE 700
#include <arpa/inet.h>
#include <assert.h>
#include <netdb.h> /* getprotobyname */
#include <netinet/in.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

int main(int argc, char** argv) {
    char buffer[BUFSIZ];
    enum CONSTEXPR { MAX_REQUEST_LEN = 1024};
    char request[MAX_REQUEST_LEN];
    char request_template[] = "GET /?abc-%ld HTTP/1.1\r\n"
                              "Host: %s\r\n"
                              "Cache-Control: private, no-cache, no-store, max-age=0\r\n\r\n"
                              "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/77.0.%ld.120 Safari/537.36";
    struct protoent *protoent;
    char *hostname = "example.com";
    in_addr_t in_addr;
    int request_len;
    int socket_file_descriptor;
    ssize_t nbytes_total, nbytes_last;
    struct hostent *hostent;
    struct sockaddr_in sockaddr_in;
    unsigned short server_port = 80;
    unsigned long int req_count = 0;

    if (argc > 1)
        hostname = argv[1];
    if (argc > 2)
        server_port = strtoul(argv[2], NULL, 10);

    /* Build the socket. */
    protoent = getprotobyname("tcp");
    if (protoent == NULL) {
        perror("getprotobyname");
        exit(EXIT_FAILURE);
    }
    socket_file_descriptor = socket(AF_INET, SOCK_STREAM, protoent->p_proto);
    if (socket_file_descriptor == -1) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    /* Build the address. */
    hostent = gethostbyname(hostname);
    if (hostent == NULL) {
        fprintf(stderr, "error: gethostbyname(\"%s\")\n", hostname);
        exit(EXIT_FAILURE);
    }
    in_addr = inet_addr(inet_ntoa(*(struct in_addr*)*(hostent->h_addr_list)));
    if (in_addr == (in_addr_t)-1) {
        fprintf(stderr, "error: inet_addr(\"%s\")\n", *(hostent->h_addr_list));
        exit(EXIT_FAILURE);
    }
    sockaddr_in.sin_addr.s_addr = in_addr;
    sockaddr_in.sin_family = AF_INET;
    sockaddr_in.sin_port = htons(server_port);

    /* Actually connect. */
    if (connect(socket_file_descriptor, (struct sockaddr*)&sockaddr_in, sizeof(sockaddr_in)) == -1) {
        perror("connect");
        exit(EXIT_FAILURE);
    }

    /* Send HTTP request. */
    signal(SIGPIPE, SIG_IGN);
    do {
        request_len = snprintf(request, MAX_REQUEST_LEN, request_template, req_count, hostname, req_count);
        if (request_len >= MAX_REQUEST_LEN) {
            fprintf(stderr, "request length large: %d\n", request_len);
            exit(EXIT_FAILURE);
        }

        nbytes_total = 0;
        while (nbytes_total < request_len) {
            printf("Before sending\n");
            nbytes_last = write(socket_file_descriptor, request + nbytes_total, request_len - nbytes_total);
            printf("After sending\n");
            if (nbytes_last == -1) {
                perror("write");
                exit(EXIT_FAILURE);
            }
            nbytes_total += nbytes_last;
        }
        fprintf(stderr, "debug: before read\n");
        while ((nbytes_total = read(socket_file_descriptor, buffer, BUFSIZ)) > 0) {
            // fprintf(stderr, "debug: after a read\n");
            // write(STDOUT_FILENO, buffer, nbytes_total);
        }
        fprintf(stderr, "debug: after read\n");
        if (nbytes_total == -1) {
            perror("read");
            exit(EXIT_FAILURE);
        }

        req_count += 1;
        printf("Sent %ld HTTP requests\n", req_count);
#if 0
        if (req_count % 2500 == 0) {
            fprintf(stderr, "Reconnecting...\n");
            close(socket_file_descriptor);
            socket_file_descriptor = socket(AF_INET, SOCK_STREAM, protoent->p_proto);
            if (socket_file_descriptor == -1) {
                perror("socket");
                exit(EXIT_FAILURE);
            }
            if (connect(socket_file_descriptor, (struct sockaddr*)&sockaddr_in, sizeof(sockaddr_in)) == -1) {
                perror("connect");
                exit(EXIT_FAILURE);
            }
        }
#endif
    } while(1);
    close(socket_file_descriptor);
    exit(EXIT_SUCCESS);
}
