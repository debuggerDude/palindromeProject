s= "1@@1"  
size= len(s)
print(size)
reverse=""
i=size

if size<2:
    if size==0:
        print("empty string")
    else:
        print("Lenght of the string provided as input, is 1. It will always be a palindrome")

else:
    while i!=0:
        reverse= reverse+s[i-1]
        i=i-1

if reverse==s:
    print("string is palindrome")

else:
    print(s)
    print(reverse)
    print("given string is not a palindrome")    