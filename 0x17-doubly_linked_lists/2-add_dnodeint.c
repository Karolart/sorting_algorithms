#include "lists.h"
#include "stdio.h"
/**
 *size_t dlistint_len(const dlistint_t *h)- Adds a new node 
 * @head:doubly linked list head pointer
 * @n: The integer for the new node to contain.
 *
 * Return: null-when the function fail
 *         Otherwise - the address of the new node.
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node = NULL;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	if (*head)
	{
		new_node->next = *head;
		new_node->prev = (*head)->prev;
		(*head)->prev = new_node;
		*head = new_node;
		return (*head);
	}

	new_node->next = *head;
	new_node->prev = NULL;
	*head = new_node;
	return (*head);
}
