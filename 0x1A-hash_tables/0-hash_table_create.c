#include <stdlib.h>
#include <stdio.h>
#include "hash_tables.h"

/**
  * hash_table_create - Creates a hash table
  * @size: hash table size
  *
  * Return: new hash table pointer
  */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *htable = NULL;

	if (size == 0)
		return (NULL);
	htable = malloc(sizeof(hash_table_t));
	if (!htable)
		return (NULL);
	(*htable).size = size;
	(*htable).array = malloc(sizeof(hash_node_t *) * size);
	if (!(*htable).array)
	{
		free(htable);
		return (NULL);
	}
	return (htable);
}
