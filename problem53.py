'''Print numbers from 1 to 50, but:
print “Fizz” if divisible by 3,
print “Buzz” if divisible by 5,
print “FizzBuzz” if divisible by both.'''
i=1
while i<=50:
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
    i+=1
    