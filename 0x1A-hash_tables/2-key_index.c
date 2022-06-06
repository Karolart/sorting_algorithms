#include "hash_tables.h"
/**
* key_index - hash table set
* @key: the key
* @size: size value
* Return: the place the value is store in the array
*/
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
