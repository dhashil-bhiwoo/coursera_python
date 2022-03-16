import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    lis= []
    num = 0
    while num < 10:
        lis.append(random.random()*5+30)
        num = num+1
    print(lis)