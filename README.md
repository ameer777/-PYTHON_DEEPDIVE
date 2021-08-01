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


