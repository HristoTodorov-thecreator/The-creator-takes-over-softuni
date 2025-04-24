
from first.hash_table import HashTable

h = HashTable()
h['name'] = 'Peter'
h['age'] = 25
print(h)  # {name: Peter, age: 25}

h.remove_item('name')
print(h)  # {age: 25}

print(len(h))  # 1