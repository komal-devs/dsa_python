# program to print factors of a given number

# brute force code
num = int(input("Enter a number--"))
print("Entered number is - ",num)
result = []
i = 1
while i <= num :
  if num% i  == 0:
    result.append(i)
  i += 1
print(f"factors of {num} are {result}")
# time complexity - O(n)
# space complexity - O(k) where k is total number of factors


# Better solution 
# 36- 1,2,3,4,6,9,12 ,18,36{half of 36 - 18}
#20 - 1,2,4,5,10 ,20 { half of 20 - 10}
num = int(input("Enter a number--"))
print("Entered number is - ",num)
result = []
for i in range(1,int(num//2)+1):
  if num%i == 0:
    result.append(i)
result.append(num)
print(f"factors are {result}")
#time complexity = O(n/2)= approx. O(n)
#Space complexity = O(k)

#optimal solution
# 36 - 1,36
#    - 2,18
#    - 3,12
#     - 4,9
#      - 6,6  # it goes repeated from 6 
# 6 is sqrt of 36
from math import sqrt
num = int(input("Enter a number --"))
print("Entered number is - ",num)
result = []
for i in range(1,int(sqrt(num))+1):
  if num%i == 0:
    result.append(i)
    if num//i != i :
      result.append(num//i)
print("Factors are ",result)

# time complexity - O(sqrt(n)) 
# space complexity - O(k)
# if we have
# to sort this result we can use result.sort()
# but time complexity is O(nlogn) so its increasing
# or we can use the code
