def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    
    
n = int(input("Enter a number: "))
print(n)
while n != 1:
        n = collatz(n)
        print(n)