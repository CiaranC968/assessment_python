import re

#This checks if the first index of 
#string is a capital Letter
def capitalLetter(s):
    if(s[0].isupper()):
        return True
    else:
        return False


#checks if the last index of the string is a ., ? or !
#also checks if there is more than 1 full stop
def fullStop(s):
    if '.' not in s[0:-1]:
        if(s[-1] == '.' or s[-1] ==  '?'  or s[-1] ==  '!'):
            return True
    else:
        return False
    
def qMarks(s):
    #adds up the number of " in the String and divides it by 2
    #Checks if there is any remainder in the division
    if s.count('"') % 2 == 0:
        return True
    else:
        return False
    
#Using regular expresion to check if string contains certain values    
def containsNumber (s):
    numbers = bool(re.search('r, [1-9]|1[0-2]', s))
    return numbers
    
         
#Checks if the string is valid by calling several functions
def isValid(s):
    if(capitalLetter(s) is True and fullStop(s) is True and qMarks(s) is True and containsNumber(s) is False):
        print("That Statement is Valid")
    else: 
        print("That Statement is not Valid")



if __name__ == "__main__":
   
    #Main code for testing String
    s = 'The quick brown fox said “hello Mr lazy dog”.'
    print(f"Capital Letter: {capitalLetter(s)}")
    print(f"Full Stop: {fullStop(s)}")
    print(f"Qoutation Marks: {qMarks(s)}")
    print(f"Contains Number: {containsNumber(s)}")
    isValid(s)
    