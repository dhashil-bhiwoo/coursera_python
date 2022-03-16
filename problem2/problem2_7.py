def problem2_7():
    """ computes area of triangle using Heron's formula. """
    s1 = float(input("Enter length of side one:"))
    s2 = float(input("Enter length of side two:"))
    s3 = float(input("Enter length of side three:"))
    s = 0.5 * (s1+s2+s3)
    area = ((s-s1)*(s-s2)*(s-s3)*s)**0.5
    print("Area of a triangle with sides",s1,s2,s3,"is",area)