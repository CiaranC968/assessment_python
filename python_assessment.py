import re

#This checks if the first index of 
#string is a capital Letter
def capitalLetter(s):
    if(s[0].isupper()):
        return True
    else:
        False

#checks if the last index of the string is a ., ? or !
#also checks if there is more than 1 full stop
def fullStop(s):
    if '.' not in s[0:-1]:
        if(s[-1] == '.' or '?' or '!'):
            return True
    else:
        return False
    
def qMarks(s):
    #adds up the number of " in the String and divides it by 2
    #Checks if there is any remainder in the division
    if s.coutn('"') % 2 == 0:#
        return True
    else:
        return False
    
def containsNumber(s):
    return bool(re.search('r,0[1-9|1[0-2]', s))

         
#Checks if the string is valid by calling several functions
def isValid(s):
    if(capitalLetter(s) is True and fullStop(s) is True):
        print("That Statement is Valid")
    else: 
        print("Invalid Staement")



if __name__ == "__main__":
    print("Hello")
    