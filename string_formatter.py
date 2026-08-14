name = input("Enter your fist name : ")
surname = input("Enter your last name : ")
bio_message = input("Enter a short bio : ")
full_name = f"{name.strip()} {surname.strip()}" 
username = f"{name[0].lower()}{surname.lower()}" 
user_bio =bio_message.strip().lower().replace("i am ", "i'm ") 
bio_len = len(bio_message.strip()) 
print(f"Your full name is: {full_name.title()}") 
print(f"Your username is: {username}") 
print(f"Your bio is: {user_bio}") 
print(f"Your bio is {bio_len} characters long")
