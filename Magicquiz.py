#Global texts obtained from wikipedia.com. This is not my own text
easy_text = "This era relies on _1_ technology. _2_ is a device, which can move and sensor the input. With the application of _3_ and machine learning. _4_ is common programming language to program a robot. Robot is more helpful and efficient."
easy_answer = ["modern","Robot","AI", "Python"]
#String2
standard_text = "software engineer is a person who applies the principles of software engineering to the _1_, _2_, _3_, _4_, and evaluation of computer software"
standard_answer = ["design", "development","maintenance", "testing"]
#String3
advance_text ="The IEEE stands for _1_ of _2_ and _3_ _4_, is a professional association with its corporate office in New York City and its operations center in Piscataway, New Jersey."
advance_answer = ["Institute", "Electrical","Electronics","Engineers"]
#Spaces
spaces_of_speech = ["_1_", "_2_","_3_","_4_"]
#blanks with number appear on text.
#start_playing function allow user playing game at different levels. For each empty blank, user has up to 3 times to guess. if correct, move to the next blank. Else it will deduct the chances.
def start_playing(level_text, answers):
    '''start_playing function is the main funcstion to run the program. it has two inputs: text and answers. it allows player to play by level. if correct, text will be updated with answer.
    Otherwise, it will be printed again for another try.
    @param text is the paragraph player will play, it contains four blanks user has to fill inself.
    @param answers is a list of answer, user\'s answer will be compared with this list. '''
    user_chances= 3 # user has up to 3 chances for each empty spaces
    index =0# keep track of the list of empty blanks
    user_answer=""# the varibale stores user answers
    print level_text
    while index< len(answers) and user_chances>0:
        user_answer = raw_input("\nWhat is the posible word for " + spaces_of_speech[index] + " ? ")
        if user_answer.lower()== answers[index].lower():
            level_text=level_text.replace(spaces_of_speech[index],answers[index])
            print "Correct!"
            print level_text
            index = index + 1
            user_chances = 3
        else:
            user_chances = user_chances -1
            if user_chances==0:
                print "Game over"
            else:
                print "That's incorrect!"
                print "You have " + str(user_chances)+ " chance(s) remaining"
                print level_text
                continue
       # user_answer = raw_input("\nWhat is the posible word for " + spaces_of_speech[index] + " ? ")
                # if user_answer.lower()== answers[index].lower():
                #     text=text.replace(spaces_of_speech[index],answers[index])
                #     print "Correct!"
                #     print text
                #     index = index + 1
                #     user_chances = 3
                #     break
############################
#play_game function contains three different levels allowing player to pick one of those and play_game.
# it will play at depend on player choice either easy, Standard, or advance.
def prompt():
    '''prompt will prompt player to select level. if level is valid, player can start play game. '''
    userinput = raw_input() #userinput is variable store player input, input help determine what level player want to play
    list_userinput =["easy", "standard", "advance"]
    if userinput.lower() in list_userinput:
        print "You chose "+ userinput +" level, let's play"
    else:
        while userinput not in list_userinput:
            print "Please enter one of the game levels: Easy, Standard, Advance"
            userinput = raw_input()
            if userinput.lower() in list_userinput:
                break
    print "You have 3 chances for each empty blanks!"
    if userinput.lower() =="easy":
        start_playing(easy_text, easy_answer)
    elif userinput.lower() == "standard":
        start_playing(standard_text, standard_answer)
    elif userinput.lower() == "advance":
        start_playing(advance_text, advance_answer)

def play_game():
    '''play_game is a main function running the game. Depend on user input, it will start_playing with text and answers associated with that level '''
    print "Welcome to Magic Quiz. Magic Quiz is a fill-in-the-blanks game testing player knowledge about modern technology. Let's play!\n"
    print "Please enter one of the game levels: Easy, Standard, Advance"
    prompt()

play_game()
############################
