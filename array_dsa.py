# Creating array that stores monthly expenses
arr = [2200,2350,2600,2130,2190]
print("In feb extra spend compared to Jan was : ", arr[1]- arr[0])
print("Expense of first quarter : ", arr[0] + arr[1] + arr[2])
print("Did I spend 2000$ in any month ? ", 2000 in arr)
print("Expense at end of june :")
arr.append(1980)
print(arr)
# refund an item purchased on April and
# got refund of 200$
arr[3] = arr[3] + 200
print("Expenses after 200$ return in April")
print(arr)


# list of marvel super heroes
heros = ['spider man','thor','hulk','iron man','captain america']
print("Length of list : ",len(heros))
#Adding black panther at the end of list 
heros.append("black panther")
print(heros)
heros.remove("black panther")
print(heros)
#Adding black panther after hulk
heros.insert(3,"black panther")
print(heros)
# removing thor and hulk and replacing with doctor strange
# in one line of code
heros[1:3] = ['doctor strange']
print(heros)
# sorting list in alphabetical order
heros.sort()
print(heros)


# creating list of all odd numbers between 1 and max 
# max is taken by user
list = []
max = int(input("Enter maximum number : "))
for i in range(1,(max+1)):
    if i%2 == 1:
        list.append(i)

print("List of odd numbers between 1 and max :")
print(list)