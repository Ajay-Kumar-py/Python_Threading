

from threading import *

class A(Thread):
    def run(self):
        for x in range(7):
            print(x)

obj = A()
obj.start()
obj.join()
print("Control returned to ", current_thread().getName())