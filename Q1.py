def sum_total():
    lst=[]
    length = int(input("enter the length of the list: "))
    for i in range(length):
        elements = int(input("enter the element: "))
        lst.append(elements)
    print(lst)

    sum = 0
    for i in lst:
        sum += i 
    print("Sum of the element of a list is: ",sum)
sum_total()