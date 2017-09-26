#  Don't mess with me ;)

name = input("Enter your name ")
cap = name.title()
arr = cap.split(" ")
if len(arr)  == 2:
    first = arr[0]
    second = arr[1]
    print (first[0:1] + ". " + second)
elif len(arr) == 3:
    first = arr[0]
    second = arr[1]
    third = arr[2]
    print (first[0:1] + ". " + second[0:1] + ". " + third)
