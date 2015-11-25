import multiprocessing as mp 
import random
import string

output = mp.Queue()

def funcion1(st, st2):
	print st,"este es el proceso", st2


processes = [mp.Process(target=funcion1, args=(2, x)) for x in range(4)]

for p in processes:
	p.start()

"""
for p in processes:
	p.join()
"""
