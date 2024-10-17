str = input("hello please put a string")
str2 = ('')
for i in str:
    str2 = i + str2

print("regular string", str)
print("\n new string", str2)