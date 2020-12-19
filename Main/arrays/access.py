import array as arr

#accesing th array elements
a=arr.array('i',[1,2,3,4,4,5])
print(a[2])

#lenght of an array
print(len(a))

#appending to an array
for i in range(0,10):
    a.append(i)
print(a)   
 
#insert takes two arguments the position and value to insert
a.insert(1,14)
print(a) 

#extent ,ust ise square brackets   
a.extend([12,13,14,15])
print(a)    

#removing elements using remove the first occurence element  specified
a.remove(15)
print(a) 

#using the pop function removinf the last elements
a.pop()
print(a)
a.pop(3)
print(a) 


#array concatenation
b = arr.array('i',[90,80,78,48])
print(a+b)

#slicing arrays
c = a+b
print(c[0:5])

#revese the array
print(c[::-1])

#looping t