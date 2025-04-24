
commands = input()
commands = commands.replace('#',' ')
text = commands.split()

water = int(input())

totalfire = 0
effort = 0
while '=' in text:
    text.remove('=')




gradus = 0

print(f'Cells:')
for i in range(0,len(text),2):
     high_medium_or_low = ''
     gradus = 0


     if i % 2 == 0:
         high_medium_or_low = text[i]

     if (i + 1) < len(text):

         if (i + 1) % 2 !=0:
            gradus = text[i + 1]
            gradus = int(gradus)


     if water < gradus:
         continue

     if high_medium_or_low == 'High' and 81 <= gradus <= 125:
         totalfire += gradus
         effort += (gradus * 0.25)
         print(f' - {gradus}')
         water -= gradus
     elif high_medium_or_low =='Medium' and 51 <= gradus <= 80:

         totalfire += gradus
         effort += (gradus * 0.25)
         print(f' - {gradus}')
         water -= gradus
     elif high_medium_or_low == 'Low' and 1 <= gradus <= 50:
         totalfire += gradus
         effort += (gradus * 0.25)
         print(f' - {gradus}')
         water -= gradus




print(f'Effort: {effort:.2f}')
print(f'Total Fire: {totalfire}')




