def problem1_5(age):
    age = int(age)
    if age <= 6:
        print("Have a glass of milk.")
    elif age in range(7, 21):
        print("Have a coke.")
    else:
        print("Have a martini.")