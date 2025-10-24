print("=== Temperature Converter System ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

Converter = int(input("Choose what you want to use (1-6)?\n ="))
temperature = float(input("Enter the temperature value: \n ="))

#if user give answer outside of the system it will not run
if 1 <= Converter <= 6 :
    if Converter == 1:
        print("Celsius to Fahrenheit converter")
        ConvTemp = (temperature * 9/5) + 32 #conversion formula from uncle google
        ConvTemp = round(ConvTemp, 2)
        ConvTemp = round(ConvTemp, 2) #rounding numbers if it is too long
        ConvTemp = "{:.2f}".format(ConvTemp) #making the output always return with 2 decimal(extra knowledge)(just making this extra step)
        print("Results :-")
        print(f"{temperature} C = {ConvTemp} F")
    elif Converter == 2:
        print("Fahrenheit to Celsius converter")
        ConvTemp = (temperature - 32) * 5/9
        ConvTemp = round(ConvTemp, 2)
        ConvTemp = "{:.2f}".format(ConvTemp) 
        print("Results :-")
        print(f"{temperature} F = {ConvTemp} C")
    elif Converter == 3:
        print("Celsius to Kelvin converter")
        ConvTemp = temperature + 273.15
        ConvTemp = round(ConvTemp, 2)
        ConvTemp = "{:.2f}".format(ConvTemp) 
        print("Results :-")
        print(f"{temperature} C = {ConvTemp} K")
    elif Converter == 4:
        print("Kelvin to Celsius converter")
        ConvTemp = temperature - 273.15
        ConvTemp = round(ConvTemp, 2)
        ConvTemp = "{:.2f}".format(ConvTemp) 
        print("Results :-")
        print(f"{temperature} K = {ConvTemp} C")
    elif Converter == 5:
        print("Fahrenheit to Kelvin converter")
        ConvTemp = (temperature - 32) * 5/9 + 273.15 
        ConvTemp = round(ConvTemp, 2)
        ConvTemp = "{:.2f}".format(ConvTemp) 
        print("Results :-")
        print(f"{temperature} F = {ConvTemp} K")
    else:
        print("Kelvin to Fahrenheit converter")
        ConvTemp = (temperature - 273.15) * 9/5 + 32
        ConvTemp = round(ConvTemp, 2)
        ConvTemp = "{:.2f}".format(ConvTemp) 
        print("Results :-")
        print(f"{temperature} K = {ConvTemp} F")
else:
    print("Invalid option. Please choose a number between 1 and 6.")