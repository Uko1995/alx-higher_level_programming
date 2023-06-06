#include "list.h"

/**
 * check_cycle - chacks if a singly linked list has a cycle in it
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast -> next != NULL)
	{
		slow = slow-> next;
		fast = fast -> next -> next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return(0);
}
