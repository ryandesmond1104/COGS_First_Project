
import string

"""This is a collection of functions for my project. Most of these functions
   are original functions, except for the last function which is an extension
   of the A3 chatbots end_chat function which is modified to fit my game.
"""

def launch_game():
    
    """Initiates and launches the game; displays main menu and user input
       Returns
       -------
               function
           preliminary function that starts game for the route chosen
    """
    
    #Displays the main menu and gives options to choose from
    route_options = print("Please choose a route: " + \
                            "\u001b[35;1mSouth Campus\u001b[0m ," + \
                            " \u001b[34mNorth Campus\u001b[0m , or " + \
                            "\u001b[33mHillcrest\u001b[0m")
    print("To exit the game please type 'exit game'.")
    
    route_choice = input("")
    #Lowercase and stripped input choice returns first level of game route
    if route_choice.lower().strip() == "south campus":
        return south_campus()
    elif route_choice.lower().strip() == "north campus":
        return north_campus()
    elif route_choice.lower().strip() == "hillcrest":
        return hillcrest()
    elif route_choice.lower().strip() == "exit game":
        pass
    else:
        print("Please pick a route indicated in the list.\n")
        return launch_game()
                            

def south_campus():
    
    """The first user choice in the game for the route "South Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #This is the first "level" of the route with two different user choices
    response = input("\u001b[0mOn your schedule it says your shift starts at 10:15." + \
                     "Do you want to meet the shuttle at \u001b[35;1m'Mandeville' or 'P785 South'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to next "level" or main menu 
    if response.lower().strip() == "mandeville":
        print("\u001b[31mYou were 30 minutes late to your shift and you were fired! :(\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "p785 south":
        print("\u001b[32mYou made it to your shift on time!\u001b[0m " + \
              "You check the bus and everything works properly.\n" + \
              "\u001b[0mYou get in the driver's seat and adjust your mirrors and seat.\n" + \
              "After doing all necessary pre-trip preparations, it's time to go!\n" + \
              "Turn off your hazards and use your blinker to move off the curb!\n" + \
              "You are approaching a four-way intersection with a stop sign.\n")
        return south_campus_2()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return south_campus()
    
def south_campus_2():
    
    """The second user choice in the game for the route "South Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Second "level" of the route with three user choices
    response = input("Do you want to go \u001b[35;1m'left', 'right', or 'straight'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to next "level" or main menu
    if response.lower().strip() == "left":
        print("\u001b[31mWrong way! What are you, North Campus? :(\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "straight":
        return south_campus_3()
    elif response.lower().strip() == "right":
        return shortcut_south_campus_3()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return south_campus_2()

def south_campus_3():
    
    """The third user choice in the game for the route "South Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Third "level" of the route with three user choices
    response = input("You approach a three-way intersection.\n" + \
                     "Do you want to go \u001b[35;1m'left' or 'right'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to next "level" or main menu
    if response.lower().strip() == "left":
        print("\u001b[31mWrong way! Passengers call your manager. :(\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "right":
        print("After waiting through some traffic, " + \
              "you arrive at a four-way light.\n")
        return south_campus_4()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return south_campus_3()
        
def shortcut_south_campus_3():
    
    """An alternate third user choice in the game for the route "South Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Alternate third "level" of the route with three user choices
    response = input("\u001b[32mCONGRATULATIONS YOU FOUND A SHORTCUT!!!\n\u001b[0m" + \
                     "Do you want to go \u001b[35;1m'left' or 'right'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to next "level" or main menu
    if response.lower().strip() == "left":
        print("\u001b[31mYou scrape your bus against a Tesla. Try Again. :(\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "right":
        print("After you go through and end on Regents...\n" + \
              "you arrive at a four-way light.\n")
        return south_campus_4()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return shortcut_south_campus_3()
    
def south_campus_4():
    
    """A fourth user choice in the game for the route "South Campus"
       Returns
       -------
               function
           either the end, the main menu, or the same part
    """
    
    #Fourth "level" of the route with three user choices
    response = input("Do you want to go \u001b[35;1m'left', 'right', or 'straight'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the end or the main menu
    if response.lower().strip() == "left":
        out_points = 0
        print("\u001b[31mWe don't have time for Starbucks!!! >:(\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "right":
        out_points = 0
        print("\u001b[32mWelcome to the Mesa Apartments!\u001b[0m")
        return end_game()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)")
        return south_campus_4()
     
def north_campus():
    
    """The first user choice in the game for the route "North Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #First "level" of the route with two user choices
    response = input("Your shift starts at 11:00.\n" + \
                     "Do you meet the bus at \u001b[34m'P704' or 'Price Center'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "price center":
        print("\u001b[31mYou missed the bus and you are fired for being late.\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "p704":
        print("After waiting for your time stop it is time to start your shift!")
        return north_campus_2()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return north_campus()
    
def north_campus_2():
    
    """Second user choice in the game for the route "North Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Second "level" of the route with two user choices
    response = input("Do you want to go \u001b[34m'left' or 'straight'?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "straight":
        print("\u001b[31mAre you trying to park the bus??? Try again.\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "left":
        return north_campus_3()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return north_campus_2()
    
def north_campus_3():
    
    """Third user choice in the game for the route "North Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Third "level" of the route with two user choices
    response = input("Do you want to go towards \u001b[34m'Price Center' or 'Warren'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "warren":
        print("\u001b[31mWhy didn't you pick up people at Price Center? " + \
              "Now your manager is mad. :(\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "price center":
        print("\u001b[32mYou successfully picked up everyone at Price Center!\u001b[0m\n")
        return north_campus_4()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return north_campus_3()
    
def north_campus_4():
    
    """Fourth user choice in the game for the route "North Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Fourth "level" of the route with three user choices
    response = input("After going through Warren, you arrive at a four-way stop sign.\n" + \
                     "Do you want to go \u001b[34m'left', 'right', or 'straight'?\u001b[0m\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "straight":
        print("\u001b[31mEveryone at Goody's stares at you and takes pictures... :(\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "left":
        print("\u001b[31mYou take a detour through the library. " + \
              "Your passengers are mildly upset.\u001b[0m")
        return north_campus_5()
    elif response.lower().strip() == "right":
        print("\u001b[32mYou are now on your way to the Gilderport stop!\u001b[0m")
        return north_campus_5()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return north_campus_4()
    
def north_campus_5():
    
    """Fifth user choice in the game for the route "North Campus"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Fifth "level" of the route with three user choices
    response = input("You are at a four-way light.\n" + \
                     "Do you want to go \u001b[34m'left', 'right', or 'straight'?\u001b[0m\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "right":
        print("\u001b[31mAre you trying to go on the freeway?!?!\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "straight":
        print("\u001b[31mOh... I didn't realize this was West Campus?\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "left":
        print("\u001b[32mYou successfully drop off passengers at Gliderport!\u001b[0m\n")
        return north_campus_6()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return north_campus_5()
    
def north_campus_6():
    
    """Sixth user choice in the game for the route "North Campus"
       Returns
       -------
               function
           either the end, the main menu, or the same part
    """

    #Sixth "level" of the route with three users
    response = input("You turn left on Pangea and arrive at a four-way stop sign. " + \
                     "Would you like to go \u001b[34m'left', 'right', or 'straight'?\u001b[0m")
    
    #Lowercase and stripped user response decides if the user moves on to the end or the main menu
    if response.lower().strip() == "right":
        print("\u001b[31mThat street is under construction. :(\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "straight":
        print("\u001b[31mOh no! Dead end! I don't think we can get the bus out! :O\u001b[0m")
        return launch_game()
    elif response.lower().strip() == "left":
        print("\u001b[32mWelcome to The Village!\u001b[0m")
        return end_game()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return north_campus_6()

def hillcrest():
    
    """The first user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """

    #First "level" of the route with two user choices
    response = input("Your shift starts at 11:30. " + \
                     "Do you want to meet the bus at \u001b[33m'Gliderport' or 'P785 North'\u001b[0m?\n")

    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "gliderport":
        print("\u001b[31mHave you ever even seen the Hillcrest bus???\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "p785 north":
        print("\u001b[32mOff we go!!!\u001b[0m\n")
        return hillcrest_2()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m")
        return hillcrest()
    
def hillcrest_2():
    
    """Second user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """

    #Second "level" of the route with three user choices
    response = input("You approach a four-way stop sign. " + \
                     "Do you want to go \u001b[33m'left', 'right', or 'straight'\u001b[0m?\n")

    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "right":
        print("\u001b[31mYou know ECC is done right?\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "left":
        return hillcrest_3()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_2()
    
def hillcrest_3():
    
    """Third user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """

    #Third "level" of the route with two user choices
    response = input("You approach another stop sign. " + \
                     "Do you want to go \u001b[33m'straight' or 'right'\u001b[0m?\n")

    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "straight":
        print("\u001b[31mYeah you wish this loop was over...\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "right":
        print("You make it to the Mandeville stop, picking up passengers on the way.\n")
        return hillcrest_4()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_3()   
    
def hillcrest_4():
    
    """Fourth user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """

    #Fourth "level" of the route with two user choices
    response = input("You drive under a bridge. " + \
                     "Do you want to go \u001b[33m'left' or 'straight'\u001b[0m?\n")

    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "left":
        print("\u001b[32mCONGRATULATIONS YOU FOUND A SHORTCUT\u001b[0m\n")
        return hillcrest_shortcut_5()
    elif response.lower().strip() == "straight":
        print("You go all the way down the street and arrive at a four-way light.\n")
        return hillcrest_5()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_4()
    
def hillcrest_5():
    
    """Fifth user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Fifth "level" of the route with three user choices
    response = input("You approach a four-way stoplight. " + \
                     "Do you want to go \u001b[33m'left', 'right', or 'straight'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "right":
        print("\u001b[31mWhere does that even go???\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "straight":
        print("\u001b[31mAre you lost?\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "left":
        print("\u001b[32mYou made it to the freeway!\u001b[0m\n")
        return hillcrest_6()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_5()
    
def hillcrest_shortcut_5():
    
    """Fifth alternate user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Alternate fifth "level" of the route with three user choices
    response = input("You approach a four-way stoplight. " + \
                     "Do you want to go \u001b[33m'left', 'right', or 'straight'\u001b[0m?\n")

    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "left":
        print("\u001b[31mHeading back to campus already?\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "right":
        print("I can't tell if you are trying to get your nails done " + \
              "or pick up groceries...\n")
        return launch_game()
    elif response.lower().strip() == "straight":
        print("\u001b[32mYou made it to the freeway!\u001b[0m\n")
        return hillcrest_6()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_shortcut_5()
    
def hillcrest_6():
    
    """Sixth user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """

    #Sixth "level" of the route with two user choices
    response = input("Do you want to take the 5 \u001b[33m'North' or 'South'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "north":
        print("\u001b[31mDid you think this was Coaster?\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "south":
        return hillcrest_7()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_6()
    
def hillcrest_7():
    
    """Seventh user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Seventh "level" of the route with two user choices
    response = input("Do you want to get off on \u001b[33m'Sea World Drive' or 'Washington Street'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "washington street":
        print("\u001b[31mYou're driving morning Hillcrest, remember?\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "sea world drive":
        print("\u001b[32mGood job!\u001b[0m\n")
        return hillcrest_8()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_7()
    
def hillcrest_8():
    
    """Eighth user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Eighth "level" of the route with two user choices
    response = input("You approach a three-way stoplight. " + \
                     "Do you want to go \u001b[33m'left' or 'straight'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "straight":
        print("\u001b[31mI wish we could take a trip to Sea World... :(\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "left":
        print("The view from over the bridge looks beautiful!")
        return hillcrest_9()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_8()
    
def hillcrest_9():
    
    """Ninth user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Ninth "level" of the route with three user choices
    response = input("You approach a four-way light. " + \
                     "Do you want to go \u001b[33m'left', 'right', or 'straight'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "right":
        print("\u001b[31mI don't think the bus needs gas...\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "straight":
        print("\u001b[31mWhat about the people at Old Town?\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "left":
        print("\u001b[32mGood job! Don't forget to turn right and pick up people from Old Town.\u001b[0m\n")
        return hillcrest_10()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_9()
    
def hillcrest_10():
    
    """Tenth user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Tenth "level" of the route with two user choices
    response = input("You pick up people from Old Town and go straight. " + \
                     "You get to the end of the street. " + \
                     "Do you want to go \u001b[33m'right' or 'straight'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "straight":
        print("\u001b[31mWrong way! You're lucky you can detour around the gas station.\u001b[0m\n")
        return hillcrest_11()
    elif response.lower().strip() == "right":
        print("\u001b[32mAlmost there!\u001b[0m\n")
        return hillcrest_11()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_10()

def hillcrest_11():
    
    """Eleventh user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the next part of the game, the main menu, or the same part
    """
    
    #Eleventh "level" of the route with three user choices
    response = input("You approach a four-way light. " + \
                     "Do you want to go \u001b[33m'left', 'right', or 'straight'\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the next "level" or the main menu
    if response.lower().strip() == "right":
        print("\u001b[31mAre you trying to get hit by a train?\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "straight":
        print("\u001b[31mIt's not time to go back on the freeway yet!\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "left":
        return hillcrest_12()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_11()

def hillcrest_12():
    
    """Twelfth user choice in the game for the route "Hillcrest"
       Returns
       -------
               function
           either the end of the game, the main menu, or the same part
    """
    
    #Twelfth "level" of the route with two user choices
    response = input("Do you want to go left on \u001b[33m'First' or 'Second' street\u001b[0m?\n")
    
    #Lowercase and stripped user response decides if user moves on to the end or the main menu
    if response.lower().strip() == "second":
        print("\u001b[31mYou should have payed attention during route training...\u001b[0m\n")
        return launch_game()
    elif response.lower().strip() == "first":
        print("\u001b[32mWelcome to Hillcrest!!!\u001b[0m\n")
        return end_game()
    else:
        print("\u001b[31mPlease check your spelling and spacing. :)\u001b[0m\n")
        return hillcrest_12()

def end_game():
    
    """Congratulatory statement and options after game completion
       Returns
       -------
               function
           congratulatory message again, main menu, or passes out of game
    """

    #End of any route results in this statement and option for user input
    print("\u001b[32mCONGRATULATIONS YOU DID IT!!!!\n\u001b[0m")
    response = input("Please type the word 'quit' to go back to the main menu. :)\n" + \
                     "Please type 'exit game' to exit out of the game.\n")
    
    #Lowercase and stripped user response decides if user moves exits game or goes to main menu
    if response.lower().strip() == "quit":
        return launch_game()
    elif response.lower().strip() == "exit game":
        pass
    else:
        return end_game()
    
               