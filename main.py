from details import spy, Spy,ChatMessage #import details.py file to maintain spy details.
from steganography.steganography import Steganography   #using steganography encoding and decoding the text with the help of images.
import csv  #importing csv file.
from termcolor import colored       #to using colorfull output.


print (colored("hello spy !!","green"))     #color is use in print function.
print (colored("let's get started","green"))

status_message = ["hello guys", "i'm busy","only call don't text me " "i'm busy"]   #predefine status messages.
direct=['emergency','accedent','sos','help','save','save me']
friends=[]
new_chat = []
def load_friends():
    with open('friends.csv', 'rU') as friends_data:
        reader = list(csv.reader(friends_data,dialect='excel'))
        for row in reader[1:]:
            if row:
                name = row[0]
                age = row[1]
                rating = row[2]
                online = row[3]
                spy = Spy(name, age, rating, online)
                friends.append(spy)
load_friends()


def add_status(current_status_message):     #create function to create a status messages.
    updated_status = None
    if current_status_message != None:      #check the condition of status messages.
        print colored("your current status message is ","blue") + current_status_message
    else:
        print colored("you don't have any current status message","blue")
    default = raw_input(colored("do you want old status(y/n)","blue"))
    if default.upper() == "N":      #upper() is use to convert case sensitive.
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

def add_friend():       #function create to adding friend with the help of dictionary.

    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = input("Age?")

    new_friend.rating = input("Spy rating?")

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.rating, new_friend.age, new_friend.is_online])
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)



def select_friend():        #function create to select a friend to friend list.
    serial_no = 1
    for friend in friends:
        print str(serial_no) + " " + friend.name
        serial_no = serial_no + 1
    select_user_friend = input("select your friend")
    user_index = select_user_friend-1
    return user_index


def send_message():     #function create to send a message to friend.
    user_selected_friend = select_friend()
    original_image = raw_input("what is your image ")
    text = raw_input("what is secret message ")
    output_path =  "output.jpg"     #output image is creating.
    Steganography.encode(original_image, output_path, text)    #incoding the text message with the help of images.

    new_chat = ChatMessage(text, True)
    with open('chats.csv', 'a') as chat_data:
        writer = csv.writer(chat_data)
        writer.writerow([friends[spy.name,user_selected_friend].name ,new_chat.message,new_chat.time])
    friends[user_selected_friend].chats.append(new_chat)     #append a new chat in status messages.
    print "Your secret message is ready! "


def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    try:
        secret_text = Steganography.decode(output_path)
    except TypeError:
        print 'error'
        exit()
    if len(secret_text) == 0:
        print "No secret mesage"
    else:
        temp = secret_text.split()
        for i in direct:
            if i in temp:
                temp[temp.index(i)] = "help me"
        secret_text = str.join(" ", temp)
        if len(temp) > 100:
            del friends[sender]
            print 'Message length exceeded. Message was not saved.'
            print 'Your friend is deleted'
        else:

            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)
            print "Your secret message has been saved"

def chat_history():         #function create for read a chat history
    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            # The message is printed in red
            print(colored("You said:", 'red')),
            print str(chat.message)
        else:
            # The date and time is printed in blue
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            # The message is printed in red
            print(colored(str(friends[read_for].name) + " said:", 'red')),
            # Black color is by default
            print str(chat.message)


def start_chat(spy_name,spy_age, spy_rating,spy_is_online):     #function create to chat start.
    current_status_message = None
    menu_list = True
    while menu_list:        #while loop is use to show the menu list
        menu_choice = input(colored("What do you want to do? \n 1. Add a status update\n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 5. Chat History \n 0. Exit \n","red"))
        if (menu_choice == 1):
            current_status_message = add_status(current_status_message)
            print "your next status message is update:- " + current_status_message
        elif (menu_choice == 2):
            number_of_friend = add_friend()
            print "you have %d friends" % (number_of_friend)
        elif (menu_choice==3):
            send_message()
        elif (menu_choice == 4):
            read_message()
        elif(menu_choice == 5):
            chat_history()
        elif (menu_choice == 0):
            menu_list = False
        else:
            print "invalid number press "


spy_exist = raw_input("Do you want to continue " + spy.salutation + " " + spy.name + " (Y/N)? ")   #already existing user.

if spy_exist.upper() == 'Y':
    print "you are already existing %s your age %d your rating %f"%(spy.name,spy.age,spy.rating)
    start_chat(spy.name,spy.age,spy.rating,spy.is_online)
elif spy_exist.upper() == 'N':
    spy.name= raw_input("welcome in SpyChat. tell me your first name-: ")
    if len(spy.name)>=2:
        print "welcome " + spy.name
        spy.salutation = raw_input("should i call you Mr. or Miss. ")
        spy.name = spy.salutation + " " + spy.name
        print "ohk " + spy.name

        spy.age = raw_input("what is your age")
        spy.age=int(spy.age)
        if spy.age > 12 and spy.age < 50:
            print "you are applicable"
            spy.rating = input("please enter your rating ")
            if spy.rating>=5:
                print "you are Great spy"
            elif spy.rating>=3.5 and spy.rating<5:
                print 'You are one of the good ones.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
            spy_online = True

            print "Authentication complete. Welcome %s your age %d and your rating in spychat %f" %(spy.name,spy.age,spy.rating)
            start_chat(spy.name,spy.age,spy.rating,spy.is_online)
        else:
            print "your age is not applicable"
    else:
        print "Spy name does not exist please try again"
else:
    print "wrong input please type correct input from keyboard"
