# -PYTHON_DEEPDIVE Sorting test

## main class
I was creative two files Order and Cust, I wrote in both the data respectively
* "with open" function,
In the first compartment : Location of the file on the computer (the file we want to write).
In the second compartment : File type. "w" Writing file

* Cust_writer function,
write to row ..

## aplication class
* constructor : Contains three lists
   * id_array : List of all IDs
   * name_array : List of all names
   * Orders_array : list of lists that contains {id,Order list}
   
* init_idArray function : 
  * Initialize id_array list
  * The form of writing in the file is problematic, between each line we skip one and do not write anything there , 
    My solution is to refer only full rows through the definition of variable C and then in each iteration check if it is even or incorrect and finally promote it.
  * At the end of the list size will be the amount of IDs in the file
  
* init_nameArray function : 
  * Initialize name_array list
  * In a similar way of function init_idArray I go through the full lines and fill out the list of names
  * Use C in a similar way to the previous one
  * At the end of the list size will be the amount of names in the file
  
* init_Orders function :
  * Initialize Orders_array list
  * The first cell will contains id and in the second cell will contains the lists for this id/
  * Set up 4 boolean variables to check if Melino has already been promoted to a cell and is not empty (fill in the cell first or add another list to the cell).
  * Read from the file and in each iteration fill the cells in the lists so that in the first cell there will be an identity card of the first person and a list of all his         orders.
  * At the end of the list size will be the amount of IDs*orders in the file

* return_name function : 
  * A function that returns an ID by name
  * If the name is in cell x in the name_array I return the ID in cell X + 1 from a list id_array , whyIt is true that the form of filling in the lists is appropriate for this     solution so that I entered the names in order and also the ID card in the same order so the X person in the list of names will have an ID card X + 1 in the ID list
  
*  return_listById :
   * A function that returns a list of all orders by ID
   * In this function all the work is already done and then we are left to retrieve the information from Orders_array list 

