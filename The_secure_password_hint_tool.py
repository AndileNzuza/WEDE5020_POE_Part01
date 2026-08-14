#Creating a secure hint
password = input("Please input your secret password : ")
clean_password = password.strip()
first_letter_of_password = "The first letter of the password is " + clean_password[0]
last_letter_of_password = "The last letter of the password is " + clean_password[-1]
print(f"Your password hint : It starts with {first_letter_of_password.upper()} and ends with {last_letter_of_password.upper()}.")