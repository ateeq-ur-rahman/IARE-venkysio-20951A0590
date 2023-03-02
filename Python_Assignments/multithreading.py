import threading
import time

def worker(num):
    
    print(f"Worker {num} started")
    time.sleep(1)
    print(f"Worker {num} finished")

if __name__ == '__main__':
    
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
    
    for t in threads:
        t.start()
    
    
    for t in threads:
        t.join()
    
    print("All threads finished")

