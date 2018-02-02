print "hello Spy !!"
print "let's get started"
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

        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating)
    else:
        print "your age is not applicable"
else:
    print "Spy name does not exist please try again"
