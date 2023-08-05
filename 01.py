

full_name = input("enter your full name: ")

mobile_number = input("enter your mobile number (05x-xxxx-xxx)")

year_of_birth = int(input("enter your year of birth"))

current_year = 2023
user_age = current_year-year_of_birth


mobile_number_parts = mobile_number.split('-')


print("User Name:", full_name)


print("User Age:", user_age)


print("Mobile Number:", mobile_number_parts)

