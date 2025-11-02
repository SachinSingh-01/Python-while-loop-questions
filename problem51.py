# Take a number and print the sum of all even numbers up to that number.(Example: if n = 10 → 2+4+6+8+10 = 30)
n=int(input("Enter the number: "))
i=1
sum=0
print("Even number")
while i<=n:
    if(i%2==0):
        print(i)
        sum+=i
    i+=1
print("Sum of the even number=",sum)
    