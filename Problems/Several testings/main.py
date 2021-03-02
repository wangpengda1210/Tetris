def check(string: str):
    if not string.isdigit():
        print("It is not a number!")
    elif int(string) >= 202:
        print(int(string))
    else:
        print("There are less than 202 apples! You cheated on me!")
