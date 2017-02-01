msg="good afternoon"

print(msg.capitalize())

name="mehul chopra"
print(name.title())

print(name.upper())
print(name.lower())

print(msg.find("afternoon"))
print(msg.find("evening")) #-1 since not found

msg1="hello  "
print(msg1.rstrip()) #lstrip

#length of the string
print(len(msg)) #no of characters in the str

#substring
print(name[6:12]) #start index-inclusive last index-exclusive
print(msg[2:14])

#replace
print(msg.replace("afternoon","evening"))

tokens=name.split(" ")
print(tokens[0])
print(tokens[1])
