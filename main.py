import random

def bubble():
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
def selection():
    for i in range(len(list)):
        a = list[i]
        for j in range(len(list)-i):
            if list[j+i]<a:
                a = list[j+i]
                toSwap = j+i
        temp = list[i]
        list[i] = a
        list[toSwap]=temp
    print("smallest is, ", a)
    
print ("How long do you want your list to be?")
x = int(input())
list = []
for i in range(x):
    list.append(random.randrange(0,100))
print(list)

bubble()
print(list)

random.shuffle(list)

selection()

print(list)
