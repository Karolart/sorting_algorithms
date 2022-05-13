#include <stdlib.h>
#include "lists.h"

/**
  * dlistint_len - counter for the elements of doubly linked_list
  * @h: doubly likned list
  *
  * Return: doubly linked list number elements
  */
size_t dlistint_len(const dlistint_t *h)
{
	int lenght = 0;

	while (h != NULL)
	{
		++lenght;
		h = h->next;
	}

	return (lenght);
}
