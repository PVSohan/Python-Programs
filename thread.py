from threading import Thread, Event

event_1 = Event()
event_2 = Event()

def func_1(ev1, ev2):
    for i in range(1, 11, 2):
        ev2.wait()  # wait for the second thread to hand over
        ev2.clear()  # clear the flag
        print('1')
        ev1.set()  # wake the second thread

def func_2(ev1, ev2):
    for i in range(2, 11, 2):
        ev2.set()  # wake the first thread
        ev1.wait()  # wait for the first thread to hand over
        ev1.clear()  # clear the flag
        print('2')

t1 = Thread(target=func_1, args=(event_1, event_2))
t2 = Thread(target=func_2, args=(event_1, event_2))