# Method 1st Very simple
# def login(user, password):
#     if user == 'kanhaiya' and password == 123:
#         return "Login Successfull👍"
#     else:
#         return "Invalid Crediantials✖️"

# print(login('kanhaiya',123))


# Method 2nd Advanced

users_list = []

def Login():
    
    user = input("Enter your name :")
    user_password = input(f"{user} enter your Password :")

    if user_password not in users_list:
        users_list.append(user)
        users_list.append(user_password)
        print("Saved in list")
        print("Login successfull👍")
    else:
        print("You are already Logined👍")

def Logout():
    name = input("Enter your name for Logout :")
    user_pass = input(f"{name} enter you Password for Logout :")

    if name in users_list and user_pass in users_list:
        users_list.remove(name)
        users_list.remove(user_pass)
        print("Logout Successfull👍")
    else:
        print("User is not Exist")

def show_users_list():
    if len(users_list) == 0:
        print("Empty Record")
    else:
        print("Users Record :",users_list)

while(True):
    print("1. Login\n2. Logout\n3. Show User Records\n4. Exit")

    ch = int(input("Enter your choice :"))

    if ch == 1:
        Login()
    elif ch == 2:
        Logout()
    elif ch == 3:
        show_users_list()
    elif ch == 4:
        break
    else:
        print("Invalid Input !")

