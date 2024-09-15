# question 1 task 1

temp = int(input("Enter a temperature in Fahrenheit: "))

# question 1 task 2
try:
    temp_celsius = (temp - 32) * (5/9)

except ValueError:
    print("Please enter a valid integer")

else:        # question 1 task 3
    print(f"{temp} degrees Fahrenheit is {temp_celsius:.2f} degrees Celsius.") 

finally:           # question 1 task 4
    print("Thank you for using the weather forecast application :)")

