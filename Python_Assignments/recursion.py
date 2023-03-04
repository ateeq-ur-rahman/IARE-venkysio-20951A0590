#Recursion to reverse of string

def rev(s):
    if len(s)==0:
        return ''
    return rev(s[1:])+s[0]
p=input().split()
r=[]
for i in p:
    r.append(rev(i))
print(' '.join(r))





