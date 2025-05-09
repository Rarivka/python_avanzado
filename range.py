for num in range(10+1):
    print(num)
 
 #range(inicio. fin , paso)  
for num in range (0,100,5) :
    print(num)
for num in range (-5, 0):
    print(num)
    
  #para que convierta range en lista iterable se hace un cambiando nombre range x lista  
nums=range (10)
list_of_nums=list (nums)
print(list_of_nums)