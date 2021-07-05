
from threading import Thread
import time

begin = time.time()
def disp():
   for i in range(100):
    print("child running")


t = Thread(target=disp)
t.start()

for i in range(100):
    print("Main Thread")

end = time.time()
k = end-begin
print("total time",k)