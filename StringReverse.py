def reverse_string(str):
    return str[::-1]


fname = input("Enter First Name : ")
lname = input("Enter Last Name : ")

print("Hello", reverse_string(fname), " ", reverse_string(lname))
