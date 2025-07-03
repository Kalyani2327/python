#Without using functions
word=input("enter here:")
sample=ord(word)
if sample>=65 and sample<=90:
    print("Upper Case")
elif sample>=97 and sample<=122:
    print("Lower Case")
elif sample>=48 and sample<=56:
    print("Number")
else:
    print("Special Character")


word="hello"
secret=""
for i in range(len(word)):
    code=ord(word[i])
    if (word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u") or (word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O" or word[i]=="U"):
        secret+=chr(code+1)
    else:
        secret+=word[i]
print(secret)

#by using functions

def encript(word):
    secret=""
    for i in range(len(word)):
        code=ord(word[i])
        if (word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u") or (word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O" or word[i]=="U"):
            secret+=chr(code+1)
        else:
            secret+=word[i]
    print(secret)
encript("hello")

def asc_code(word):
     sample=ord(word)
     if sample>=65 and sample<=90:
        print("Upper Case")
     elif sample>=97 and sample<=122:
        print("Lower Case")
     elif sample>=48 and sample<=56:
        print("Number")
     else:
        print("Special Character")
asc_code("E")



