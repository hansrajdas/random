/*
 * Date: 2019-11-16
 *
 * Description:
 * This program sends UDP packets on a given IP address in burst. It sends UDP
 * packets on all ports from 1 to 65535 continuously.
 *
 * Executing this program has networking side effects like your device might
 * disconnect from wifi.
 *
 * Approach:
 * Accepts IP as command line argument and sends UDP packets on all ports
 * from main thread.
 *
 * Usage:
 * ./a.out 1.2.3.4
 *
 */

#include <arpa/inet.h>
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>

int main(int argc, char** argv) {
  int clientSocket, nBytes;
  char buffer[4] = "...";
  char *host_ip = "127.0.0.1";
  struct sockaddr_in serverAddr;
  socklen_t addr_size;
  unsigned short int port = 1;

  if (argc > 1)
    host_ip = argv[1];

  /*Create UDP socket*/
  clientSocket = socket(AF_INET, SOCK_DGRAM, 0);

  /*Configure settings in address struct*/
  serverAddr.sin_family = AF_INET;
  serverAddr.sin_addr.s_addr = inet_addr(host_ip);
  memset(serverAddr.sin_zero, '\0', sizeof serverAddr.sin_zero);  

  /*Initialize size variable to be used later on*/
  addr_size = sizeof serverAddr;

  nBytes = strlen(buffer) + 1;
  while(1) {
    serverAddr.sin_port = htons(port);
    /*Send message to server*/
    if (port && sendto(clientSocket, buffer, nBytes, 0, (struct sockaddr *)&serverAddr, addr_size) < 0) {
      perror("sendto failed");
      printf("Failed for port: %u\n", port);
      return -1;
    }

    /*Receive message from server*/
    // recvfrom(clientSocket, buffer, 1024, 0, NULL, NULL);
    if (!port)
      printf(".\n");
    port += 1;
  }
  return 0;
}
