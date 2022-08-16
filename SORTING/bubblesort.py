def bubblesort(mylist):
    for i in range(0, len(mylist)-1):
        for j in range(0, len(mylist)-1-i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

    return mylist

mylist = ['d', 'c', 't', 'a', 'e', 'w', 'g']

print(bubblesort(mylist))
