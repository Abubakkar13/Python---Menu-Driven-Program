#Code_on_List_Oprn

myList = []
choice = 0
sortedd = []

while True:
    print('\n1. Insert integer e at position i\n2. Print the list\n3. Delete the first occurrence of integer\n4. Insert integer e at the end of the list\n5. Sort the list\n6. Pop the last element from the list\n7. Reverse the list\n')
    choice = int(input())

    #insert to list
    if choice == 1:
        element = int(input('Enter the element to insert : '))
        pos = int(input('Enter the position to insert : '))
        myList.insert(pos, element)

    #print the list
    elif choice == 2:
        print(myList)

    #delete first element from list
    elif choice == 3:
        del myList[0]

    #insert at last position
    elif choice == 4:
        element = int(input('Enter the element to insert : '))
        pos = len(myList)
        myList.insert(pos, element)

    #Sorting list
    elif choice == 5:
        x = myList.sorted()
        print(x)

    #Pop last element from list
    elif choice == 6:
        myList.pop()
        print(myList)

    #Sort list by reverse order
    elif choice == 7:
        myList.sort(reverse = True)
        sortedd.append(myList)

    elif choice == 0:
        exit()
    #input is only Integer
    else:
        print('Enter valid Number .')
