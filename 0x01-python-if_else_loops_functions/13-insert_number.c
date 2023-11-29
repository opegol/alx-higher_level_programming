#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head : pointer to head of linked list.
 * @number : number to insert
 * Return: the address of the tmp node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;

	node = *head;
	tmp = malloc(sizeof(listint_t));
	if (!tmp)
		return (NULL);
	tmp->n = number;

	if (node == NULL || ((node->n) >= number))
	{
		tmp->next = node;
		*head = tmp;
		return (tmp);
	}

	while (node != NULL && (node->next) != NULL && (node->next)->n < number)
		node = node->next;

	tmp->next = node->next;
	node->next = tmp;

	return (tmp);
}

