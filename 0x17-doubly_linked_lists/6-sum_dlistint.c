#include <stdlib.h>
#include "lists.h"

/**
  * sum_dlistint - Sum the elements in a doubly linked list
  * @head: doubly linked list head
  *
  * Return: doubly linked list data sum
  */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *current = head;
	int sum = 0;

	if (head)
	{
		while (current != NULL)
		{
			sum += current->n;
			current = current->next;
		}
	}

	return (sum);
}
