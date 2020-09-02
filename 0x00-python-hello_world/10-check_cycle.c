#include "lists.h"
/**
 * check_cycle - checks for a cycle
 * @list: the list
 * Return: 1 for cycle, 0 for no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *new_01 = list, *new_02 = list;

	for (; new_01 && new_02 && new_02->next;)
	{
		new_01 = new_01->next;
		new_02 = new_02->next->next;
		if (new_02 == new_01)
			return (1);
	}
	return (0);
}
