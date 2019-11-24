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
 * Compile:
 * gcc -g udp_burst.c -lpthread -o udp_burst
 *
 * Usage:
 * ./udp_burst <HOST_IP> <NUMBER_OF_CLIENTS> <WAIT_ON_FAILURE>
 *
 * HOST_IP(default = 127.0.0.1): IPv4 address of host to burst with UDP packets
 * NUMBER_OF_CLIENTS(default = 1): Number of clients/threads to use
 * WAIT_ON_FAILURE(default = 500): Wait in ms if sending UDP fails before sending again
 *
 * Example:
 * ./udp_burst 148.66.137.25 3 1000
 * It will make UDP requests to host "1.2.3.4" using "3" clients/threads and
 * waits for 1000ms(1 second) on failure to send UDP packet.
 */

#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <time.h>
#include "pthread.h"

// Globals
char *host_ip = "127.0.0.1";
unsigned long int wait_in_ms = 500;

void delay(int milliseconds) {
  long pause;
  clock_t now,then;

  pause = milliseconds * (CLOCKS_PER_SEC / 1000);
  now = then = clock();
  while((now - then) < pause)
    now = clock();
}

void *send_udp_requests(void *data) {
  int clientSocket, nBytes;
  struct sockaddr_in serverAddr;
  socklen_t addr_size;
  unsigned short int port = 1;
  char *buffer = ".";
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
      printf("Failed for thread[%d], port[%u]\n", (int)thread_id, port);
      delay(wait_in_ms);
    }
    if (!port)
      printf("Cycle completed by %d\n", (int)thread_id);
    port += 1;
  }
  return NULL;
}

int main(int argc, char** argv) {
  pthread_t *udp_send;
  unsigned long int i = 0;
  unsigned long int n = 1;

  if (argc > 1)
    host_ip = argv[1];

  if (argc > 2)
    n = strtoul(argv[2], NULL, 10);

  if (argc > 3)
    wait_in_ms = strtoul(argv[3], NULL, 10);

  udp_send = (pthread_t *)malloc(n * sizeof(pthread_t));
  if (!udp_send) {
    printf("malloc failed");
    return -1;
  }

  for(;i < n; i++) {
    pthread_create(&udp_send[i], NULL, send_udp_requests, NULL);
    printf("Created thread %ld\n", i + 1);
  }

  for(i = 0; i < n; i++)
    pthread_join(udp_send[i], NULL);
  return 0;
}
