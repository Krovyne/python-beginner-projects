import random
#import itertools #only import if you use

attempttime = 0
print("====Welcome to guessing number game!====")
print("------------difficulty level------------")
print("1.Easy mode :-\n -Number range between 1 to 10")
print("2.Medium mode :-\n -Number range between 1 to 50")
print("3.Hard mode :-\n -Number range between 1 to 100")
print("4.Extra Hard mode :-\n -Number range between 1 to 1000")
print("5.Impossible mode :-\n -Number range between 1 to 1000 \n -With 20 attempts ")

difficulty = int(input("Choose difficulty 1. Easy 2. Medium 3. Hard 4. Extra Hard 5. Impossible\n"
                    "Enter required difficulty number = "))
if 1 <= difficulty <= 5:
    if difficulty == 1:
        print("------------Easy Mode------------")
        targetnum = random.choice(range(10))
        #print(targetnum)
        
        for attempt in range(100):#you can just make 100 guess if you want but to achieve infinite loop using for loops 
            #in python(you can use while loops since python for loop not same as other language)
            #(it designed to iterate over a finite sequence)
            #(In Python 3 range() can go much higher, though not to infinity) 
            #we need to use itertools.count and break can refer at the bottom of this file
            attempttime = attempt
            guessnum = int(input("Guess the number!!\n"
                            "Your guess = "))
            if guessnum == targetnum:
                print("Congratulations You win!!")
                break #use break for to stop the loop
            elif guessnum > 10: #if people guess outside of the range
                print("Didn't you read the level description?")
            elif guessnum < targetnum:
                print("Give higher!")
            elif guessnum > targetnum:
                print("Give lower!")
            else:
                print("Game over!!!!You inputted wrong data type")
    elif difficulty == 2:
        print("-----------Medium Mode-----------")
        targetnum = random.choice(range(100))
        #print(targetnum)
        
        for attempt in range(50):
            attempttime = attempt
            guessnum = int(input("Guess the number!!\n"
                                "Your guess = "))
            if guessnum == targetnum:
                print("Congratulations You win!!")
                break 
            elif guessnum > 50: 
                print("Didn't you read the level description?")
            elif targetnum - 11 < guessnum < targetnum + 11 :#since the range is bigger we need to help the user more 
                #and need to put above so that this is checked first since code are executed from top to bottom
                if guessnum < targetnum:
                    print("Close but give higher!")
                elif guessnum > targetnum:
                    print("Close but give lower!")            
            elif guessnum < targetnum:
                print("Give higher!")
            elif guessnum > targetnum:
                print("Give lower!")
            else:
                print("Game over!!!You inputted wrong data type")
    elif difficulty == 3:
        print("------------Hard Mode------------")
        targetnum = random.choice(range(100))
        #print(targetnum)
        
        for attempt in range(100):
            attempttime = attempt
            guessnum = int(input("Guess the number!!\n"
                                "Your guess = "))
            if guessnum == targetnum:
                print("Congratulations You win!!")
                break
            elif guessnum > 100:
                print("Didn't you read the level description?")
            elif targetnum - 11 < guessnum < targetnum + 11 :
                if guessnum < targetnum:
                    print("Close but give higher!")
                elif guessnum > targetnum:
                    print("Close but give lower!")               
            elif guessnum < targetnum:
                print("Give higher!")
            elif guessnum > targetnum:
                print("Give lower!")
            else:
                print("Game over!!!You inputted wrong data type")
    elif difficulty == 4:
        print("---------Extra Hard Mode---------")
        targetnum = random.choice(range(1000))
        #print(targetnum)
        
        for attempt in range(1000):
            attempttime = attempt
            guessnum = int(input("Guess the number!!\n"
                                "Your guess = "))
            if guessnum == targetnum:
                print("Congratulations You win!!")
                break
            elif guessnum > 1000:
                print("Didn't you read the level description?")
            elif targetnum - 11 < guessnum < targetnum + 11 :
                if guessnum < targetnum:
                    print("Close but give higher!")
                elif guessnum > targetnum:
                    print("Close but give lower!")               
            elif targetnum - 101 < guessnum < targetnum + 101 :
                if guessnum < targetnum:
                    print("Give higher!")
                elif guessnum > targetnum:
                    print("Give lower!")
            elif guessnum < targetnum:
                print("Too far!!Give higher!")
            elif guessnum > targetnum:
                print("Too far!!Give lower!")
            else:
                print("Game over!!!You inputted wrong data type")        
    else:
        print("---------Impossible Mode---------")
        targetnum = random.choice(range(1000))
        #print(targetnum)
        
        for attempt in range(10):
            attempttime = attempt
            guessnum = int(input("Guess the number!!\n"
                                "Your guess = "))
            if guessnum == targetnum:
                print("Congratulations You win!!")
                break
            elif guessnum > 1000:
                print("Didn't you read the level description?")
            elif targetnum - 11 < guessnum < targetnum + 11 :
                if guessnum < targetnum:
                    print("Close but give higher!")
                elif guessnum > targetnum:
                    print("Close but give lower!")               
            elif targetnum - 101 < guessnum < targetnum + 101 :
                if guessnum < targetnum:
                    print("Give higher!")
                elif guessnum > targetnum:
                    print("Give lower!")
            elif guessnum < targetnum:
                print("Too far!!Give higher!")
            elif guessnum > targetnum:
                print("Too far!!Give lower!")
            else:
                print("Game over!!!You inputted wrong data type")
        if attempttime + 1 == 10:
            print("Game over!!!You Have exceed 20 attempts")
            print(f"The number is {targetnum}")
else:
    print("Wrong input!!")

if difficulty == 5:
    print("You are goated you actually complete the impossible challenge!!")
    print(f"You win with {attempttime + 1} attempts")
else:
    print(f"Congratulations you have win with {attempttime + 1} attempts")
# for i in itertools.count():
#     print(f"Current count: {i}")
#     # Add a condition to break the loop if needed, otherwise it will run forever
#     if i >= 10:
#         break
