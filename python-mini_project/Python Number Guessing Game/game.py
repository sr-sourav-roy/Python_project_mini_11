import random

RandomNumber = random.randrange(1,200) # randrange uses for if_elif_else so do't use for while loop
print(RandomNumber) # you undersantad
UserInpur = int(input("Guess tge number:__"))

if UserInpur > RandomNumber:
    print(RandomNumber)# you undersantad
    print("the number is high")
elif RandomNumber > UserInpur:
    print(RandomNumber) # you undersantad
    print("the number is low")

else:
    print(RandomNumber) # you undersantad

    print("the number is macth")
