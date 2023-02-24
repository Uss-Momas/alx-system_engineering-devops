#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 * infinite_while - function that contains infinity loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point program
 * Return: nothing
 */
int main(void)
{
	int pid, count_zombies = 0;

	while (count_zombies < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %i\n", pid);
			sleep(1);
			count_zombies++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}

