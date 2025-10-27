print("Welcome! Please enter username and password")
username = ''
password = ''
i = 0
while not username == "DarthVader12" and not password == "Handsome123":
    if i > 0 and not username == "DarthVader12" and not password == "Handsome123": #only print out when it is second time and above
        print("Wrong username or password!!")
    username = input("Username = ")
    password = input("Password = ")
    i+=1 #iterator for counting tries

print(f"Welcome {username}!")

#few other ways of making this just keeping this for reference

print("Welcome! Please enter username and password")

username = ""
password = ""

while username != "DarthVader12" or password != "Handsome123":
    if username != "" or password != "": #this for making sure it not executed in first round and after it will keep executed if user input something 
        #and if the password and username are true it will not get into the loop anymore so it will not print the wrong message
        print("Wrong username or password!!")
    username = input("Username = ")
    password = input("Password = ")

print(f"Welcome {username}!")

######

print("Welcome! Please enter username and password")

while True:
    username = input("Username = ")
    password = input("Password = ")

    if username == "DarthVader12" and password == "Handsome123":
        print(f"Welcome {username}!")
        break #break from the while loop not the if statement(if statement already finish executed this break is inside while loop already?)
    else:
        print("Wrong username or password!!")
