#menggunakan method copy
list_1 = [10, 70, 20] 
list_2 = list_1.copy() 
print(list_1) 
# output ➜ [10, 70, 20]

print(list_2) 
# output ➜ [10, 70, 20]

#kombinasi assigment dan slicing
list_1 = [10, 70, 20] 
list_2 = list_1[:] 
print(list_1) 
# output ➜ [10, 70, 20]

print(list_2)
 # output ➜ [10, 70, 20]