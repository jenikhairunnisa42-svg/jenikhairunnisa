data_str = "hello world" 
print(data_str) 
# output ➜ hello world

# menggunakan data_str
data_str = "hello world" 
slice1 = data_str[0:3] 
print(slice1) 
# output ➜ hel

# data_str[2:8]
slice2 = data_str[2:8] 
print(slice2) 
# output ➜ llo wo

#data_str[5:0]
slice3 = data_str[:5] 
print(slice3) 
# output ➜ hello

# data_str[3:7:1]
slice5 = data_str[3:7:1] 
print(slice5) 
# output ➜ lo w

#data_str[2:9:2]
slice6 = data_str[2:9:2] 
print(slice6) 
# output ➜ lowr

#data_str[0:len(data_str)]
slice7 = data_str[:] 
print(slice7) 
# output ➜ hello world

#data_str[0:len(data_str):2]
slice8 = data_str[::2] 
print(slice8) 
# output ➜ hlowrd
