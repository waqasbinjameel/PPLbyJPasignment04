dict = {1:"apple", 2:"mango", 3:"banana"}
dict.keys()
if int(input('enter number\n')) in dict.keys():
    print("already exist")
else: print("not exist")