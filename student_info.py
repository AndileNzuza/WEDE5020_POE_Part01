#User information
name = input("Enter first name : ")
surname = input("Enter surname : ")
age = int(input("Enter age : "))
favourite_number = float(input("Enter favourite number : "))
text = 'personal information data' 
print(text.title()) 
print(f'Welcome, {name.upper()} {surname.upper()}!')
age_in_months = age * 12 
print(f"Age in months: {age_in_months}") 
rounded_number = round(favourite_number, 2) 
print(f"Rounded favourite number: {rounded_number}") 
print("Data type of first name:", type(name)) 
print("Data type of surname:", type(surname)) 
print("Data type of age:", type(age)) 
print("Data type of favourite_number:", type(favourite_number))