import multiprocessing as mp 
import random
import string
lista1=[1,2,3,4,5,6,7]
m = mp.Manager()
out_queue=m.Queue()

def cuadrado(x, lista, out_queue):
	print "proceso",x
	lista[x]=lista[x]+x**2
	print lista[x]
	out_queue.put(lista)

pool=mp.Pool(processes=4)
results=[pool.apply(cuadrado, args=(x,lista1, out_queue)) for x in range(1,7)]
pool.close()
pool.join()
print lista1
res_list=[]
for r in results:
	res_list.append(out_queue.get())
print res_list