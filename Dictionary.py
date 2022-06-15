from lib2to3.pgen2.token import NEWLINE


root = {'name':"Andy",'password':911216}
print(f"The root name is {root['name']},and the password is {root['password']} .")

root["password"] = 123456
print(f"The root name is {root['name']},and the new password is {root['password']} .")

del root["password"]
print(root)

users = {
    'Xia Yuan' : 8799075,
    'Kang Shen' : 911216,
    'Da Dou' : 123456,
    'Ha Ha' : 000000,
}
users2 = {
    'Xia Yuan' : 8799075,
    'Kang Shen' : 911216,
    'Da Dou' : 123456,
}
print('\n')
for i,j in users.items():
    if i in users2.keys():
     print(f"{i}'s password is {j}")
    else:
        print("No match")
   
users3 = {
    'Xia Yuan' : ['wife','mother'],
    'Kang Shen' : ['husband','father'],
    'Da Dou' : ['son','son'],
}
for i,j in users3.items():
    print(f"{i}'s identities :")
    for idn in j:
        print(idn)




