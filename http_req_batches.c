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
#include "pthread.h"
#include "signal.h"

typedef struct Data {
    int sd;
    char hostname[100];
} Data;

void *send_http_request(void *data) {
    ssize_t nbytes_last;
    ssize_t nbytes_total;
    unsigned long int req_count = 0;
    int request_len;
    Data *thread_data = (Data *)data;
    enum CONSTEXPR {MAX_REQUEST_LEN = 1024};
    char request[MAX_REQUEST_LEN];
    pthread_t thread_id = pthread_self();
    char request_template[] = "GET /?abc-%ld HTTP/1.1\r\n"
                              "Host: %s\r\n"
                              "Cache-Control: private, no-cache, no-store, max-age=0\r\n\r\n"
                              "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/77.0.%ld.120 Safari/537.36";

    signal(SIGPIPE, SIG_IGN);
    do {
        request_len = snprintf(request, MAX_REQUEST_LEN, request_template, req_count, thread_data->hostname, req_count);
        if (request_len >= MAX_REQUEST_LEN) {
            fprintf(stderr, "request length large: %d\n", request_len);
            return NULL;
        }

        nbytes_total = 0;
        while (nbytes_total < request_len) {
            // printf("Before sending\n");
            nbytes_last = write(thread_data->sd, request + nbytes_total, request_len - nbytes_total);
            // printf("After sending\n");
            if (nbytes_last == -1) {
                perror("write");
                return NULL;
            }
            nbytes_total += nbytes_last;
        }
        req_count += 1;
        if (req_count % 1000 == 0)
            printf("Thread ID[%d]: Sent %ld HTTP requests\n", (int)thread_id, req_count);
    } while(1);
    return NULL;
}

void *receive_http_rsp(void *sd) {
    char buffer[BUFSIZ];
    ssize_t nbytes_total;
    int socket_file_descriptor = *(int *)sd;
    unsigned long int rsp_count = 0;
    do {
        // fprintf(stderr, "debug: before read\n");
        while ((nbytes_total = read(socket_file_descriptor, buffer, BUFSIZ)) > 0) {
            // fprintf(stderr, "debug: after a read\n");
            // write(STDOUT_FILENO, buffer, nbytes_total);
        }
        // fprintf(stderr, "debug: after read\n");
        if (nbytes_total == -1) {
            perror("read");
            return NULL;
        }
        rsp_count += 1;
        if (rsp_count % 1000000 == 0)
            printf("Received %ld HTTP responses\n", rsp_count);
    } while(1);
    return NULL;
}

int main(int argc, char** argv) {
    struct protoent *protoent;
    char *hostname = "example.com";
    in_addr_t in_addr;
    int socket_file_descriptor;
    struct hostent *hostent;
    struct sockaddr_in sockaddr_in;
    unsigned short server_port = 80;
    pthread_t thread_send, thread_receive;
    Data data;

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

    // Create thread to send and receive HTTP requests
    data.sd = socket_file_descriptor;
    strcpy(data.hostname, hostname);
    data.hostname[strlen(hostname)] = '\0';
    pthread_create(&thread_send, NULL, send_http_request, &data);
    pthread_create(&thread_receive, NULL, receive_http_rsp, &socket_file_descriptor);

    pthread_join(thread_send, NULL);
    // pthread_join(thread_receive, NULL);
}
