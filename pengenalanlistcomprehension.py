#contoh 1
seq = []
for i in range (5):
    seq.append(i*2)

print(seq)

#contoh 2
seq = []
for i in range (10):
    if i % 2 == 1:
     seq.append[i]

print(seq)

#contoh 3 
seq = []
for i in range (1,10):
    seq = []
    for i in range (1,10):
     seq.append(i* (2 if i % 2 == 0 else 3))

print(seq)

#contoh 4
list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']

seq = []
for x in list_x:
    for y in list_y:
        seq.append(x+y)

print(seq)

#contoh 5
matrix =[
   [1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
]

transposed = []
for i in range(4):
   tr =[]
   for row in matrix:
      tr.append(row[i])
   transposed.append(tr)

print(transposed)

