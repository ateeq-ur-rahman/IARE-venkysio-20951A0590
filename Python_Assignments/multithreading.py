
#Reverse Of a string using multi threading
import threading

def reverse_string(s):
    mid = len(s) // 2
    for i in range(mid):
        s[i], s[-i-1] = s[-i-1], s[i]

def reverse_string_multithreaded(s):
    mid = len(s) // 2
    t1 = threading.Thread(target=reverse_string, args=(s[:mid],))
    t2 = threading.Thread(target=reverse_string, args=(s[mid:],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    reverse_string(s)

s = "Hello, World!"
s = list(s)
reverse_string_multithreaded(s)
s = ''.join(s)
print(s)




