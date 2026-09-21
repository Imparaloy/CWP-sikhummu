password = "Python is awesome"

try:
    user_input = input()
    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
except EOFError:
    print("ACCESS DENIED")