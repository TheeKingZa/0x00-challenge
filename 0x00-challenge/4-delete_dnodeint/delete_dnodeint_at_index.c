#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current;
	unsigned int i;

	if (*head == NULL)
		return (-1);
	current = *head;

	if (index == 0)
	{
		/* Update the head to the next node and handle next's prev */
		*head = current->next;

		if (current->next)
			current->next->prev = NULL;
		free(current);
		return (1);
	}
	
	i = 0;
	
	while (i < index)
	{
		if (current == NULL)
			return (-1);  /* Index is out of bounds */
		current = current->next;
		i++;
	}
	if (current == NULL)
		return (-1);  /* Index is out of bounds */

	/* Update the previous node's next and handle next's prev */
	current->prev->next = current->next;
	if (current->next)
		current->next->prev = current->prev;

	free(current);
	return (1);
}
