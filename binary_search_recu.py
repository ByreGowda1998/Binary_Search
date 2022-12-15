                   #Program Binary Search using Recursion Method
                   
                   
""" These Program invoves seaching particular 
   element in array or list  using rRecursion Method
"""                  
                   
                   
        

posi=0                                       #taking intial posistion of the serching element as 0
def binary_search(arr,serch_ele,lB,uB):
    """
    These function takes the  array or list and element that is to seached and lowerbound and upperbound
    returns the posistion of the element in the list if element present in the list or array

    """
    
    arr.sort()
    while lB <= uB:
         mid = (lB+uB)//2
         if arr[mid] == serch_ele:
             globals()['posi'] = mid          #converting local variable as global variable and assigning index no elemnt if element is in list 
             return True
         else:
             if arr[mid] < serch_ele:
                return binary_search(arr,serch_ele,mid+1,uB)      # if value of middle element greater than element to be seraching element making lower bound as middle index no and increaminting middle index no to plus 1 and calling the  function
        
             else:
                return binary_search(arr,serch_ele,lB,mid-1)      #if value of middle element leser than element to be seraching element making upper bound as middle index no and decreaminting middle index no minus  calling the function  
            
    return False 

arr = [12,43,132,34,56,23,45,78,93,34,47,21]
serch_ele = int(input("eneter the searching element :"))
lB = 0                                                                    # lB represented as lowerbound
uB = len(arr)-1                                                            # uB represented as upperbound  
 

if binary_search(arr,serch_ele,lB,uB):
    print(f"Array after sorting is {arr}")
    print(f"The no you are searching {serch_ele} is at {posi+1} position in array after sorting array")
else:
    print(f"The no you are serching {serch_ele} not in Array")
    

                

    
    
    
