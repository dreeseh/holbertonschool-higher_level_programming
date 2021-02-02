#include "lists.h"
/**
 * check_cycle - checks if given linked list is cyclic
 * @list: linked list
 * Return: 1 if cyclic, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *move1 = list, *move2 = list;

	for (; move1 && move2 && move2->next;)
	{
		move1 = move1->next;
		move2 = move2->next->next;
		if (move2 == move1)
			return (1);
	}
	return (0);
}
