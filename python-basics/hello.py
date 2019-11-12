#first_name = input("What is your first name?  ")
##print(first_name)
##print("These", "will be", "joined together by spaces.")
#
##print("Hello, Myron")
#print("Hello,", first_name)
#
#if first_name == "Myron":
#    #print("Myron is learning Python")
#    print(first_name, "is learning Python")
#elif first_name == "Maximiliane"
#    print(first_name, "is learning with fellow students in the community! Me too!")
#else:
#    age = int(input("How old are you? "))
#    if age <= 6:
#        print("Wow you're {}! If you're confidewnt with your reading aleady...".format(age))
#    print("You should totally learn Python, {}!".format(first_name))
#print("Have a great day {}!".format(first_name))

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4)
    print(result)

praise = "You are doing great"
#praise = praise.upper()
#number_of_characters = len(praise)
#result = praise + "!" * (number_of_characters // 2)
#print(result)
yell(praise)

advice = "Don't forget to ask for help"
#advice = advice.upper()
#number_of_characters = len(advice)
#result = advice + "!" * (number_of_characters // 2)
#print(result)
yell(advice)

advice2 = "Don't Repeat Yourself. Keep things DRY"
#advice2 = advice2.upper()
#number_of_characters = len(advice2)
#result = advice2 + "!" * (number_of_characters // 2)
#print(result)
yell(advice2)