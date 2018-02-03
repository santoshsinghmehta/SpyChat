from details import spy_salutation, spy_name, spy_age, spy_rating,spy_is_online
print "hello Spy !!"
print "let's get started"

def start_chat(spy_name,spy_age, spy_rating,spy_is_online):
    menu_list = True
    while menu_list:
        menu_choice = input("What do you want to do? \n 1. Add a status update\n 0. Exit \n")
        if (menu_choice == 1):
            status = raw_input("hello, %s write your status " % (spy_name))
            print status
        elif (menu_choice == 0):
            menu_list = False
        else:
            print "invalid number press "


spy_exist = raw_input("Do you want to continue " + spy_salutation + " " + spy_name + " (Y/N)? ")
if spy_exist.upper() == 'Y':
    print "you are already existing %s your age %d your rating %f"%(spy_name,spy_age,spy_rating)
    start_chat(spy_name,spy_age,spy_rating,spy_is_online)
elif spy_exist.upper() == 'N':
    spy_name= raw_input("welcome in SpyChat. tell me your first name-: ")
    if len(spy_name)>=2:
        print "welcome " + spy_name
        spy_salutation = raw_input("should i call you Mr. or Miss. ")
        spy_name = spy_salutation + " " + spy_name
        print "ohk " + spy_name

        spy_age = raw_input("what is your age")
        spy_age=int(spy_age)
        if spy_age > 12 and spy_age < 50:
            print "you are applicable"
            spy_rating = input("please enter your rating ")
            if spy_rating>=5:
                print "you are Great spy"
            elif spy_rating>=3.5 and spy_rating<5:
                print 'You are one of the good ones.'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
            spy_online = True

            print "Authentication complete. Welcome %s your age %d and your rating in spychat %f" %(spy_name,spy_age,spy_rating)
            start_chat(spy_name,spy_age,spy_rating,spy_is_online)
        else:
            print "your age is not applicable"
    else:
        print "Spy name does not exist please try again"
else:
    print "wrong input please type correct input from keyboard"
