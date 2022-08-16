def bubble_sort(mylist):
    swapped = True
    while swapped:
        swapped= False
        for i in range (len(mylist)-1):
            if mylist[i]>mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                swapped = True


list_sort = [1, 2, 4, 2, 1, 6, 4, 3 ]
bubble_sort(list_sort)
print(list_sort)
