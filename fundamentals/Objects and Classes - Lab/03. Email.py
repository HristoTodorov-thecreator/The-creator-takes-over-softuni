
class Email():
    def __init__(self,sender, receiver ,content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content
    def send(self):
        self.is_sent = True
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input()
    if command == 'Stop':
        break
    g = command.split(' ')
    sender = g[0]
    receiver = g[1]
    content = g[2]
    email = Email(sender,receiver,content)
    emails.append(email)
index = [int(i) for i in input().split(', ')]

for m in index:
    emails[m].send()
for email in emails:
    print(email.get_info())


