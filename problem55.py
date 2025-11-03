# Take a number and check whether it is Harshad number or not.(A number is Harshad if it is divisible by the sum of its digits — e.g., 18 ÷ (1+8)=2 → yes)
n=int(input("Enter the number to check Harshad number:"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
if temp % sum==0:
    print("Harshad")
else:
    print("Not Harshad")
   