from collections import deque

client = input()

clients = deque()

while client != 'End':
    if client == 'Paid':
        while clients:
            print(clients.popleft())

    else:
        clients.append(client)

    client = input()
print(f'{len(clients)} people remaining.')