# Program to check whether a number is armstrong or not i.e
# 153 = 1*3 + 5*3 + 3*3 
#     = 1 + 125 + 27 = 1634
# 1634 = 1*4 + 6*4 + 3* 4 + 4*4
#      = 1 + 1296 + 81 + 256 = 1634

num = int(input("Enter a number --"))
print("Entered number is -- ", num)
n = num
result = 0
count = 0
# for getting length of a number
while n > 0:
  count += 1
  n = n // 10
n = num
# for checking armstrong no
while n> 0:
  last_digit = n % 10
  result += last_digit**count
  n = n//10
print("result = ",result)
print(num == result)

# time complexity = O(log10(N))
# space complexity = O(1)