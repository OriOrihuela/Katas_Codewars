'''Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. 
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.'''

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    if flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    


    # TEST CASES #

    print(lovefunc(1,4), ", result should be True")
    print(lovefunc(2,2), ", result should be False")
    print(lovefunc(0,1), ", result should be True")
    print(lovefunc(0,0), ", result should be False")