from audioop import reverse
from pickle import TRUE


mylist1 = ['andy','shen',"kang"]
print(mylist1[0])
print(mylist1[2].title())
print(mylist1[-2])
mylist1.append(1)
print(mylist1)
mylist1.insert(1,"haha")
print(mylist1)
del mylist1[1]
print(mylist1)
firstitem = mylist1.pop(0)
mylist1.remove("shen")
print(mylist1)
var1 = 'kang'
mylist1.remove(var1)
print(mylist1)
mylist2 = [4,5,1]
mylist2.sort()
print(mylist2)
mylist2.sort(reverse=True)
print(mylist2)
print(sorted(mylist2))
mylist2.reverse()
print(mylist2)
print(len(mylist2))
