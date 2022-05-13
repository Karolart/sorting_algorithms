#include "lists.h"
#include "stdio.h"
/**
 *size_t dlistint_len(const dlistint_t *h)- Adds a new node 
 * @head:Head pointer od doubly linked list
 * @n: The integer for the new node to contain.
 *
 * Return: null-when the function fail
 *         Otherwise - the address of the new node.
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->prev = NULL;
	new->next = *head;
	if (*head != NULL)
		(*head)->prev = new;
	*head = new;

	return (new);
}
