#print sum of the numbers from 3 list using map
l1=[1,2,3,4]
l2=[1,2,3,4]
l3=[1,2,3,4]

L=list(map(lambda x,y,z: x+y+z,l1,l2,l3))
print(L)

#Filter out the names of the fruits which has letter 'g' in it
fruits=['Mango','Orange','Apple','Kiwi']
f=list(filter(lambda x: 'g' in x,fruits))
print(f)
