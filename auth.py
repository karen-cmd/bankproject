#registration
#username,email and password
#generate user Account

#login
#username or email and password
#initializing the system

import random
database = {} #dictionary

def init():



    isValidOptionSelected = False
    print('Welcome to bank V')
    
    

    while isValidOptionSelected == False:
        haveAccount= int(input('Do you have an account with us? 1(yes) 2(no)')) 

        if(haveAccount == 1):
            isValidOptionSelected = True

            login ()  
    

    
            
        elif(haveAccount == 2):

            isValidOptionSelected = True

            register()
            
        else:
        print('Invalid option selected!')
        


def login():
    
    print('login to your account!')

    isLoginsuccessful = False
    while isLoginsuccessful == False:
        accountNumberFromUser = int(input("Enter your account Number\n"))
        password= input("What is your password \n")

        for accountNumber, userDetails in database.item():
            if(accountNumber == accountNumberFromUser):
                if(userDetails == password):
                    isLoginsuccessful == True


    print('Invalid account please try Again!')


    bankOperations(userDetails)


def register():
    print('Please Register for an Account!')
    email =input('What is your email address?\n')
    first_name=input('What is your first_name?\n')
    last_name=input('What is your last_name?\n')
    password=input('create your password!\n')

    accountNumber = generateAccountNumber()

    database[accountNumber]=[first_name,last_name,email,password]

    print('Your account has been created!')
    print("your account number is %d" accountNumber)
    print("Always remember your pin is private!")

    login()

def bankOperations(user):
    print('welcome %s %s'%(user[0],user[1]))

def generateAccountNumber():

    print('Generating Account Number!')
    return random.randrange(1111111111,9999999999)


    

##My Bank System ##

init ()



