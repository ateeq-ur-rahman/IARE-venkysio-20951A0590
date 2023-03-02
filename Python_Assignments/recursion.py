'''import time
def func(a):
    c=time.time()
    b=8
    a=a+b
    a=a*b
    a=a//b
    print(a)
    e=time.time()
    print(e-c)
func(10)'''
#Reverse Of String
'''
import time
def xyz(a):
    c=time.time()
    i=0
    j=len(a)-1
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    print(a)
    d=time.time()
    print(d-c)
xyz([1,2,3])'''
#Reverse a String
'''import time
def rev(a):
    c=time.time()
    a=a[::-1]
    d=time.time()
    print("After Reversal",a)
    print(d-c)
rev("Ateeq")'''
# Reversal a Dictionary
'''import time
def dic(a):
    c=time.time()
    b={j:i for i,j in a.items()}
    d=time.time()
    print(b)
    print(d-c)
dic({'a':1,'b':2,'c':3})
'''
#Reverse Order Of words in python
'''import time
def rev(s):
    c=time.time()
    de=s.split()
    r=de[::-1]
    d=time.time()
    r=' '.join(r)
    print(r)
s="How Are You!"
rev(s)
'''
#reverse order of each character of word in python
'''import time
def rev(a):
    c=time.time()
    e=a.split()
    r=[i[::-1] for i in e]
    r=' '.join(r)
    d=time.time()
    print(r)
    print(d-c)
a="How Are You!"
rev(a)
'''
#Reverse Digits Of Integer
'''import time
def digi(a):
    c=time.time()
    i=str(a)[::-1]
    
    d=time.time()
    print(int(i))
    print(d-c)
digi(12345)'''

#Reverse a integer without converting to string
'''import time
a=int(input())
r=0
c=time.time()
while a>0:
    e=a%10
    r=r*10+e
    a=a//10
d=time.time()
print(r)
print(d-c)
'''
# How can you reverse the order of elements in a multidimensional list in Python?
'''import time
def comp(a):
    c=time.time()
    reversed_list = [sublist[::-1] for sublist in a[::-1]]
    d=time.time()
    print(reversed_list)
    print(d-c)
a=[[1,2,3],[4,5,6]]
comp(a)
'''
#Reverse a string without built in function
'''
import time
def comp(a):
    c=time.time()
    a=a[::-1]
    d=time.time()
    print(a)
    print(d-c)
comp("Ateeq")'''

#How can you reverse a list without using the built-in reverse function in Python?

'''import time
def comp(a):
    c=time.time()
    a=a[::-1]
    d=time.time()
    print(a)
    print(d-c)
a=[1,2,3,4]
comp(a)
'''


