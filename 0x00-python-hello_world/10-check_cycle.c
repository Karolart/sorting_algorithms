#include "lists.h"
/**
 * check_cycle.c - looking for a cycle in the linked list
 *:list: pointer will be check
 *return: 1 if is a cycle or 0 if it is not
*/
int check_cycle(listint_t *list)
{
	listint_t *head, *current;

	head = list;
	current = list;

	while (head && current && current->next)
	{
		current = current->next->next;
		if (head == current)
			return (1);

		head = head->next;		
	}

	return (0);
}
