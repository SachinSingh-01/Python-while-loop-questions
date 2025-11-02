# Take a number and print the sum of digits that are even.(Example: n = 24863 → even digits = 2+4+8+6 = 20)
n=int(input("Enter the digits: "))
sum=0
while n>0:
    digit=n%10
    if(digit%2==0):
        sum+=digit
    n=n//10
print("Sum of the even digits=",sum)
