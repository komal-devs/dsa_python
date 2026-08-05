# check input number is palindrome or not

n = int(input("Enter a number -- "))
print("Entered number is -- ",n)
num = n
result = 0
while num> 0:
  last_digit = num % 10
  result = (result*10)+ last_digit
  num = num//10
print( n == result)

# Time Complexity - O(log(N))
# Space complexity - O(1)
