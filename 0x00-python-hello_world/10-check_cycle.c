#include "lists.h"
/**
 * check_cycle.c - looking for a cycle in the linked list
 *:list: pointer will be check
 *return: 1 if is a cycle or 0 if it is not 
*/
 
 int check_cycle(listint_t *list)
 {
      listint_t *skilpad;
      listint_t *haas;
      
       while true:
       {
         if(list == NULL || list->next == NULL)
               return (0);
             
         skilpad = haas = list;
        
         if (skilpad && haas && haas->next)  
            
             skilpad = skilpad->next;
             hass = hass->next->;   
             if (skilpad == hass)
                    return(1);
           
        }
        return (0); 
 }
