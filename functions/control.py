def even_numbers():
    x = range(2,10,2)
    for i in x:
        print(i)
def odd_numbers():
    x = range(20)
    for i in x:
        if(i %2 != 0):
            print(i)
def divisible_by_5():
    x = range(50)
    for i in x:
        if i % 5 == 0:
            print(f'{i} is divisible by 5')
        else:
           print(f'{i} is not divisible by 5')
def multiple_comparision():
    x = range(50)
    for i in x:
        if i % 5 == 0: 
            print(f'{i} is divisible by 5')
        elif i % 7 == 0: 
            print(f'{i} is divisible by 7')
        elif i % 9 == 0: 
            print(f'{i} is divisible by 9')
        else: 
            print(f'{i} is not divisible by 5, 7 or 9')



def odd_and_even():
    x = range(50)
    for i in x:
        if i % 2 == 0 and i % 3 == 0:
            print(f'{i} is divisible by both 2 and 3')
        elif i % 2 == 0 or i % 3 == 0:
            print(f'{i} is divisible by either 2 or 3')
        else:
            print(f'{i} is not divisible by 2 or 3')
def while_loop():
    x = 1
    while(x < 10):
        print(f'{x} Hello')
        x += 1
        if x == 5:
            break
# def while_sub_loop():
#     x = 9
#     while(x < 10):
#         print(x)
#         x -= 1
    
def while_continue_loop():
    x = 0
    while(x <= 20):
        # print(f'{x} Hello')
        x += 1
        if x % 3 == 0:
            continue
        print(f'{x} Hello')
        
###########ASSIGNMENT####################      
        
# Write a function that uses while, if and continue 
# statements to print all the even numbers between 0 and 50.
def print_even_nums():
    x = 0
    while x < 50:
        x +=1
        if x % 2 != 0:
            continue
        print(x)
# Write a function that takes an integer argument and
# prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def checks_prime(num):
    if num <= 1:
        print(f"{num} is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f'{num} "Not prime"')
                break
        else:
                print(f'{num} "a Prime"')

# Write a function that takes a list of integers as input and
# prints the sum of all the even numbers in the list
def sum_even_nums(nums):
    sum = 0
    for i in nums:
        if i % 2 == 0:
         sum+=i
    print(sum)


# Write a function that takes any two integers as input, and prints t
# he sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_numbers(d,c):
    sum = 0
    x = range(d,c +1)
    for i in x:
        if i % 3 == 0:
         sum+=i
    print(sum)



