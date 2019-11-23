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
#include "pthread.h"

char *host_ip = "127.0.0.1";

void *send_udp_requests(void *data) {
  int clientSocket, nBytes;
  struct sockaddr_in serverAddr;
  socklen_t addr_size;
  unsigned short int port = 1;
  char buffer[4] = "...";
  pthread_t thread_id = pthread_self();

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
      printf("%d. Failed for port: %u\n", (int)thread_id, port);
      return NULL;
    }
    if (!port)
      printf("Cycle completed by %d\n", (int)thread_id);
    port += 1;
  }
  return NULL;
}

int main(int argc, char** argv) {
  pthread_t udp_send;

  if (argc > 1)
    host_ip = argv[1];

  pthread_create(&udp_send, NULL, send_udp_requests, NULL);

  pthread_join(udp_send, NULL);
  return 0;
}
