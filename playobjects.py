from sys import intern

n1="mehul"
n2="m"+"ehul"

print(n1 is n2)

n1="mehul chopra"
n2="mehul"+" chopra"

print(n1==n2) #true
print(n1 is n2) #false

n1="mehul chopra"
n2="mehul chopra"
print(n1 is n2)#true because of compiler level rearranging of the code n1=n2="mehul chopra"

a=4+5
b=8+1

print(a is b) #True

c=255+2
d=256+1

print(c is d) #False
print(c==d) #true

e=d=258
print(e is d) #true
                                                                
#bypass python str caching rules
n1=intern("mehul chopra")
n2=intern("mehul"+" chopra")
print(n1 is n2) #true
