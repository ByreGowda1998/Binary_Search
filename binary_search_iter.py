                  #Program Binary Search using Iterative Method
                  
                  
""" These Program invoves seaching particular 
   element in array or list  using itereative Method
    """
posi=0                                #taking intial posistion of the serching element as 0
def binary_search_iter(arr,serch_ele):
    """
    These function takes the  array or list and element that is to seached
    returns the posistion of the element in the list if element present in the list or array
    """
    arr.sort()   # Sorting the array
    l=0           # l represented as lowerbound   
    u=len(arr)-1    # u represented as upperbound  

    while l <= u:
         mid=(l+u)//2       
         if arr[mid]==serch_ele:
             globals()['posi']=mid       # converting local variable as global variable and assigning index no elemnt if element is in list 
             return True
         else:
             if arr[mid] < serch_ele:
                l=mid+1                    # if value of middle element greater than element to be seraching element making lower bound as middle index no and increaminting middle index no to plus 1
             else:
                u=mid-1                     # if value of middle element leser than element to be seraching element making upper bound as middle index no and decreaminting middle index no minus 1
            
    return False 

arr=[12,43,132,34,56,23,45,78,93,34,47,21]
serch_ele=int(input("eneter the serching element :"))


if binary_search_iter(arr,serch_ele):       # calling function 
    print(f"Array after sorting is {arr}")
    print(f"The no you are searching {serch_ele} is at {posi+1} position in array after sorting array")
else:
    print(f"The no you are searching {serch_ele} not in  give array")
    

