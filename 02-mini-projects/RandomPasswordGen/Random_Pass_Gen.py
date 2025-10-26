import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')',',','.','?']

print("Welcome to random password generator")
nLetters = int(input("How many characters ?\n"))
nNumbers = int(input("How many numbers ?\n"))
nSymbols = int(input("How many symbols ?\n"))

password = [] #declare as list
for letter in range(nLetters): #0(default start with 0) to inputted numbers dont need to plus one since we want the counting not the numbers in the range
    password.append(random.choice(letters))
    # print(password) #try to always test your system
for number in range(nNumbers):
    password.append(random.choice(numbers))
for symbol in range(nSymbols):
    password.append(random.choice(symbols))

#print(password) #this is done but you can push it more
random.shuffle(password)
#print(password) #this is done but you can go for more
CompPass = "" #set as string
for passchar in password: #generate the output in better format
    CompPass += passchar
print(f"Your generated password = {CompPass}")

#alternative and shorter answer
altpass = random.choices(letters, k = nLetters) + random.choices(numbers, k = nNumbers) + random.choices (symbols, k = nSymbols)
random.shuffle(altpass)
CompAltPass = "" #set as string
for passchar in altpass: #generate the output in better format
    CompAltPass += passchar
print("--Alternate Answer--")
print(f"Your generated password = {CompAltPass}")