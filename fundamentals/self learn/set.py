myset = {3,1,2} # v set elemntite ne sa podredeni i edin i sushti element ako se povtarq nqma da se printira

print(myset) # ako imame 3,1,2 toi go printira 1,2,3 ako imame dva puti 4isloto 2 go printira edin put

set1 = {1,2,3}
set2 = {3,4,5}
print(set1 | set2) # obedinqva dvato seta
print(set1 & set2) # vrushta obshtite elementi
print(set2 - set1) # vrushta elementi koito sa samo v ediniq set
print(set1 ^ set2) # vrushata vsi4ki elementi bez ednakvite

myset.add(4) # set moje da se promenq dobavqme elemnti
print(myset)
myset.remove(2)
print(myset)

frozen_set = frozenset([1,2,3]) # tozi specialen set ne moje da dobavqsh ili premahvash elementi

