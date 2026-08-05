# program to count no of digits in an integer

n = int(input("Enter an integer -- "))
print("Entered number is -- ",n)
count = 0
num = n
while num > 0:
  count += 1
  num = num//10
print("No of digits are - ",count)