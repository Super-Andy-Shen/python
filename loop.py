age = "Enter your age:"
age = input(age)
age = int(age)
print(f"Your age * 2 is :{age * 2}")

poll = {}
active = True
while active:
    name = input("What is your name :")
    age = input("What is your age :")
    poll[name] = age

    q = input("Do you want to quit? yes/no : ")
    if(q == 'yes'):
        active = False

for i,j in poll.items():
    print(f"{i} is {j} years old")