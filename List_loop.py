list1 = [1,2,3,4]
for i in list1:
    i = i + 1
    print(i)
print("That's my first loop")
for i in range(1,11):
    print(i)
even_num = list(range(0,9,2))
print(even_num)
mysum = 0
sum_of_sqaures = []
for s in range(1,11):
    s = s ** 2
    sum_of_sqaures.append(s)
    mysum = mysum + s
print(sum_of_sqaures)
print(mysum)
print(sum(sum_of_sqaures))
list2 = [i ** 2 for i in range(1,11)]
print(list2[:3])
list3 = list1
del list3[0]
print(list3)
print(list1)