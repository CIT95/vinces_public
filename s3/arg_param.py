#I want to create a program where side lengths can be used to decide if one can form a rectangle with lengths given
def PromptRectangle(a=3, b=6, c=6, d=3):
    global side1, side2, side3, side4
    def side1 == a
    def side2 == b
    def side3 == c
    def side4 == d
#Sides 1 and 4 must be equal as they are the sides, and sides 2 and 3 must be equal as they are the top and bottom
    if (a == d and b == c):
        return True
    else:
        return False
#Now I need to establish the results
def resultRectangle(bol):
    if (bol):
        print('\n ==> The numbers ' + str(side1) + ', ' + str(side2) + ', ' + str(side3) + ',' + str(side4) + ' can be the sides of a rectangle.')
    else:
        print('\n ==> The numbers ' + str(side1) + ', ' + str(side2) + ', ' + str(side3) + ',' + str(side4) + ' can not be the sides of a rectangle.')

resultRectangle(PromptRectangle(3,6,6,3))