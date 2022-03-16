def problem1_7():
    b1 = input("Enter the length of one of the bases:")
    b2 = input("Enter the length of the other base:")
    h = input("Enter the height:")
    b1 = float(b1)
    b2 = float(b2)
    h = float(h)
    base_sum = b1 + b2
    avg_base = base_sum / 2
    area = avg_base * h
    
    print("The area of a trapezoid with bases",b1,"and",b2,"and height",h,"is",area)