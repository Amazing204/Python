# f = open('hello.txt','r')
# print(f.read())


# f = open('hello2.txt','w')
# print(f.read())


# f = open('hello.txt','a')
# f.write("lets see if it appends")
# f.close()

with open('file.txt','a') as f:
    f.write("with using with statement")
