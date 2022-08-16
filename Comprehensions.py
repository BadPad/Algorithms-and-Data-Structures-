'''
item = [n*2 for n in range(10)]
print (item)

l1 = ['a', 'b', 'c', 'n', 'e', 'd', 'n', 'e', 'n', 'h', 'y', 'n', 'w', 'g', 'd', 'n', 'r']

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print (prices)


##GCD

def gcd(n1, n2):
    if n1>n2:
        n1, n2 = n2, n1

    for x in range(n1, 0, -1):
        if n1 % x == 0 and n2 % x == 0:
            return x


print("GCD for 60, 48 is : ", gcd(60, 48))
'''

def fibonacci(n):
   ## write base case
   ## write recursive case
   if (n < 2):
      return n
   else:
      return (n*fibonacci(n-1))

print(fibonacci(5))
