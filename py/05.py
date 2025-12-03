# # For Loop
# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(0,10,2):
#     print(i)


# # While Loop - Don't know when the conditon will settle. 
# count = 0
# while count < 5:
#     print(count)
#     count += 2


# # Loop Control Statement:
# for i in range(10):
#     if i == 3:
#         continue    # Skip this iteration
#     if i == 7:
#         break       # Exit the loop 
#     print(i)


# # Nested Loop:
# for i in range(2):
#     for j in range(3):
#         for k in range(4):
#             print(f"({i}, {j}, {k})")


# # Ex 1: 
# for i in range(5, 50, 5):
#     print(i)


# Ex 2: 
limit = 20

print(f"Prime number up to {limit} are: ")

for num in range(2, limit + 1):   # start from 2
    is_prime = True               # assume number is prime

    # check if num is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False          # divisible -> not prime
            break                     # no need to check further

    if is_prime:
        print(num) 

