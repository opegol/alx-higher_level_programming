#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly-linked list has a cycle in it
 * @list: singly-linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *t1, *t2;

	if (!(list) || !(list->next))
		return (0);

	t1 = list->next;
	if (t1)
		t2 = t1->next;

	while (t1 != NULL && t2 != NULL)
	{
		if (t1 == t2)
			return (1);
		
		t1 = t1->next;
		t2 = t2->next;
		if (t2)
			t2 = t2->next;
	}
	return (0);
}
