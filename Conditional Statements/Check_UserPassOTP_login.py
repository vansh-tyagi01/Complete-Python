username = input("Enter your Name :").lower()
password = input("Enter your Password :")
otp = int(input("Enter OTP :"))

if username == 'kanhaiya':
    if password == 'pbka123':
        if otp == 815023:
            print("Login Successfull👍")
        else:
            print("Invalid OTP")
    else:
        print("Invalid Password")
else:
    print("Invalid username")