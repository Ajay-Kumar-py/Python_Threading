
from threading import Thread, current_thread

def disp():
    print("Default Child Thread Name", current_thread().getName())
    current_thread().setName("Ajay")
    print("Default Child Thread Name", current_thread().getName())

t1 = Thread(target=disp)
t2 = Thread(target=disp)
t1.start()
t2.start()

print("Main thread Name", current_thread().getName())
current_thread().setName("Ajay_Main")
print("New Main thread Name", current_thread().getName())