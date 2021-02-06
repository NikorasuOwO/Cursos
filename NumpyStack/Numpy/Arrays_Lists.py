import numpy as np

L = [1,2,3]

A = np.array([1,2,3])

for e in L:
    print(e)


for e in A:
    print(e)

L.append(4) #Can be done because the length can chnage
# A.append cant be done because length cant chaange

L = L + [5]
print(str(L))

A = A + np.array([5]) #Adds 5 to each element
print(str(A))

A = A + np.array([1,2,3]) #Adds two arrays: adds elements with the same index
print(str(A))

print(str(2*A)) #Multiplies the elements of the arrays
print(str(2*L)) # Repeats the list

print(np.array([3,4,5])**2) # Squares the elements of the array
print(np.exp(np.array([3,4,5]))) #
print(np.tanh(np.array([3,4,5])))
