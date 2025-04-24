mylist = ['a','b']
mylist.append('c')   # append - dobavqne i dobavqme c
print(mylist)

mylist.extend(['l','m','n'])  # extend - razshirqvame , razshirqvame l , m , n
print(mylist)

mylist.insert(0,'z') # insert - vkarvame [0] e purva poziciq na z
print(mylist)

mylist.pop() # pop maha poslednoto
print(mylist)

mylist.remove('a') # maha koqto poiskame ot lista
print(mylist)

fib = [1,1,2,5,6,10,12,15]
print(fib.count(1))  # tova dava kolko puti ima 1 v lista

fit = [10,12,10,10,15]
print(fit.count(10)) # poneje ima 3 puti 4isloto 10 pokazva print 3

print(fit.index(15)) # indexa pokazva na koe mqsto e 4isloto primerno [0] e 4isloto 10 , [1] e 4isloto 12 i pokazva
# na printa 4 za 4isloto 15


g = [1,2,3] # tazi komanda obrushta elementite na obratno ako e 1,2,3 stava 3 ,2,1
g.reverse()
print(g)

n = [60,40,25,10,2]
print(sorted(n)) # tazi komanda sortira cifrite ako sa 60,30,20 gi pravi 20,30,60

sorted(n,reverse=True)  # tazi komanda gi sortira naobratno
print(n)

print(min(n)) # nai golqmoto 4islo
print(max(n)) # nai malkoto 4islo