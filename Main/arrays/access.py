import array as arr

#accesing th array elements
a=arr.array('i',[1,2,3,4,4,5])
print(a[2])

#lenght of an array
print(len(a))

#appending value to an array
for i in range(0,10):
    a.append(i)
print(a)   
 
#insert takes two arguments the position  and value to insert
a.insert(1,14)
print(a) 

#extent ,ust ise square brackets   
a.extend([12,13,14,15])
print(a)    

#removing elements using remove the first occurence of element  specified
a.remove(15)
print(a) 

#using the pop function removing the last elements
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

list = [9, 9, 6, 89, 90, 90, 90, 123, 91, 13, 12, 34, 22, 56, 70, 45, 33]
print(list)
print(max(list))
print(min(list))

#list compression
h_letters = [letter for letter in 'human']
print(h_letters)
