from threading import *
class ex:
    def B(self):
        lst = [2,1,'w',8.7,'abc']
        for x in lst:
            print("Child printing", x)

myobj = ex()
t1 = Thread(target=myobj.B)
t1.start()
t1.join()
print('done')