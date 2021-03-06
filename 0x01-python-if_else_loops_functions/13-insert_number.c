#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to the head of the list
 * @number: number to insert
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
        if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
                return (new);
	}
	temp = *head;
	while (temp->next)
	{
		if (number < temp->n)
		{
			new->next = temp;
			*head = new;
			return (new);
		}
		if (temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	new->next = NULL;
	temp->next = new;
	return (new);
}
