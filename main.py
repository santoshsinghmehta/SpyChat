from details import spy_salutation, spy_name, spy_age, spy_rating,spy_is_online
print "hello Spy !!"
print "let's get started"

status_message = ["hello guys", "i'm busy","only call don't text me " "i'm busy"]

friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []

def add_status(current_status_message):
    updated_status = None
    if current_status_message != None:
        print "your current status message is " + current_status_message
    else:
        print "you don't have any current status message"
    default = raw_input("do you want old status(y/n)")
    if default.upper() == "N":
        new_status = raw_input("what is your next status")
        if len(new_status)>0:
            updated_status = new_status
            status_message.append(updated_status)
    elif default.upper() == "Y":
        status_position =1
        for message in status_message:
            print "%d %s " %(status_position,message)
            status_position = status_position+1
        message_select = int(raw_input("choose a message"))

        if len(status_message)>= message_select:
            updated_status = status_message[message_select-1]
    else:
        print "this is invalid option please try again"
    if status_message:
        print "your status message is :%s" % (updated_status)
    else:
        print "you did not update status"
    return updated_status

def add_friend():
    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = input("Age?")
    new_rating = input("Spy rating?")
    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        # Add Friend
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print "friend added.."
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends_name)


def start_chat(spy_name,spy_age, spy_rating,spy_is_online):
    current_status_message = None
    menu_list = True
    while menu_list:
        menu_choice = input("What do you want to do? \n 1. Add a status update\n 2. Add a friend \n 0. Exit \n")
        if (menu_choice == 1):
            current_status_message = add_status(current_status_message)
            print "your next status message is update" + current_status_message
        elif (menu_choice == 2):
            number_of_friend = add_friend()
            print "you have %d friends" % (number_of_friend)
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
