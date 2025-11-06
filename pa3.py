import datetime #so that when it is creating a history, it knows the date

convert_to_other_currencies = {#exchange rates from dollars to other currencies
    "Euro": 0.87,
    "Japanese yen": 154.19,
    "Pound sterling": 0.76,
    "Canadian dollar": 1.41,
    "Mexican peso": 18.50,
    "Chinese yuan": 7.12,
    "South African rand": 17.31,
    "Indian rupee": 88.74
}

convert_from_other_currencies = {#exchange rates from other currencies to dollars
    "Euro": 1.15,
    "Japanese yen": 0.0065,
    "Pound sterling": 1.31,
    "Canadian dollar": 0.71,
    "Mexican peso": 0.054,
    "Chinese yuan": 0.14,
    "South African rand": 0.058,
    "Indian rupee": 0.011
}

def calculations(to_or_from):
    currency_options = ['euro', 'euros', 'yen', 'yens', 'japanese yen', 'japanese yens', 'pounds', 'british pounds', 'pound', 'british pound', 'pound sterling', 'cad', 'canadian dollar', 'canadian dollars', 'peso', 'pesos', 'mexican pesos', 'mexican peso', 'chinese yuan', 'chinese yen', 'chinese yuans', 'chinese yens', 'yuans', 'rands', 'sad', 'rand', 'south african rand', 'south african rands', 'rupees', 'rupee', 'ruppee', 'ruppees', 'indian rupee', 'indian rupees']
    
    if to_or_from == "convert to":#using the convert_to dict and language
        currency_name = input("What currency would you like to convert to? Your options are euros, Japanese yen, British pounds, Canadian dollars, Mexican pesos, Chinese yuan, South African rand, and Indian rupees.\n")     
        while currency_name.lower() not in currency_options:#if not a valid option
            currency_name = input("Sorry, I didn't recognize that currency. Please try again. ")
        initial_value = input("What is the original cost? (In USD) ")
        while True:#make it into an int, unless if that's not possible (then loop until it is)
            try:
                int(initial_value)
                break
            except ValueError:
                initial_value = input("I didn't recognize that as a number. Please try again. What is the original cost? (In USD) ")       
        if currency_name.lower() in ['euro', 'euros']:#converting to exact key so that i can do key/value stuff later
            currency_name = "Euro"
        elif currency_name.lower() in ['yen', 'yens', 'japanese yen', 'japanese yens']:
            currency_name = "Japanese yen"
        elif currency_name.lower() in ['pounds', 'british pounds', 'pound', 'british pound', 'pound sterling']:
            currency_name = "Pound sterling"
        elif currency_name.lower() in ['cad', 'canadian dollar', 'canadian dollars']:
            currency_name = "Canadian dollar"
        elif currency_name.lower() in ['peso', 'pesos', 'mexican pesos', 'mexican peso']:
            currency_name = "Mexican peso"
        elif currency_name.lower() in ['chinese yuan', 'chinese yen', 'chinese yuans', 'chinese yens', 'yuans']:
            currency_name = "Chinese yuan"    
        elif currency_name.lower() in ['rands', 'sad', 'rand', 'south african rand', 'south african rands']:
            currency_name = "South African rand"
        elif currency_name.lower() in ['rupees', 'rupee', 'ruppee', 'ruppees', 'indian rupee', 'indian rupees']:
            currency_name = "Indian rupee"      
        currency_rate = convert_to_other_currencies[currency_name] #doing key/value stuff to figure out the exchange rate
    elif to_or_from == "convert from":    
        currency_name = input("What currency would you like to convert from? Your options are euros, Japanese yen, British pounds, Canadian dollars, Mexican pesos, Chinese yuan, South African rand, and Indian rupees.\n")
        while currency_name.lower() not in currency_options:
            currency_name = input("Sorry, I didn't recognize that currency. Please try again. ")
        initial_value = input("What is the original cost? (In another currency) ")
        while True:
            try:
                int(initial_value)
                break
            except ValueError:
                initial_value = input("I didn't recognize that as a number. Please try again. What is the original cost? (In USD) ")   
        if currency_name.lower() in ['euro', 'euros']:
            currency_name = "Euro"
        elif currency_name.lower() in ['yen', 'yens', 'japanese yen', 'japanese yens']:
            currency_name = "Japanese yen"
        elif currency_name.lower() in ['pounds', 'british pounds', 'pound', 'british pound', 'pound sterling']:
            currency_name = "Pound sterling"
        elif currency_name.lower() in ['cad', 'canadian dollar', 'canadian dollars']:
            currency_name = "Canadian dollar"
        elif currency_name.lower() in ['peso', 'pesos', 'mexican pesos', 'mexican peso']:
            currency_name = "Mexican peso"
        elif currency_name.lower() in ['chinese yuan', 'chinese yen', 'chinese yuans', 'chinese yens', 'yuans']:
            currency_name = "Chinese yuan"    
        elif currency_name.lower() in ['rands', 'sad', 'rand', 'south african rand', 'south african rands']:
            currency_name = "South African rand"
        elif currency_name.lower() in ['rupees', 'rupee', 'ruppee', 'ruppees', 'indian rupee', 'indian rupees']:
            currency_name = "Indian rupee"        
        while currency_name.lower() not in currency_options:
            currency_name = input("Sorry, I didn't recognize that currency. Please try again. ")      
        currency_rate = convert_from_other_currencies[currency_name]    
    final_currency = int(initial_value) * int(currency_rate)#finding out the end value by multiple user-given initial value by the exchange rate     
    print(f"The final answer is {final_currency} in {currency_name}.")
    return final_currency, currency_name#returning so other functions can use it

def saving_history(final_currency, currency_name, to_or_from):
    username = input("What is your username? ")
    filename = f"{username}.txt"#creating a file under the username
    try:
        file = open(filename, 'x') #creating new file
    except FileExistsError: #if there's already a file under this name, just add to it
        file = open(filename, 'a')
    x = datetime.datetime.now()  
    todays_date = (x.strftime("%m/%d/%Y")) #this is the format i want for the date
    if to_or_from == "convert to":
        file.write(f"{todays_date} - {final_currency}, from USD to {currency_name}\n")  #writing the history down
    elif to_or_from == "convert from":
        file.write(f"{todays_date} - {final_currency}, from {currency_name} to USD\n")           
    file.close()     
    return filename#so other parts of program can use it

def show_history(filename):#like here!
    while True:#looping unless the try runs sucessfully, then the loop breaks
        try:
            user_file = open(filename, 'r')
            break
        except FileNotFoundError:#gives the user a chance to type in a difference file name if this one doesn't exist
            username = input("Sorry, I couldn't find anything under that username. Please try another or enter exit. ") 
            if username in ["exit", "quit", "to exit", "exiting", "e"]:#ORRRR they can just exit if they can't remember the user
                print("Okay, returning to home. \n")
                return#breaks out of helper function
            filename = f"{username}.txt"
    print("Your history is: ")        
    file_content = user_file.read()
    print(file_content)#print history doc (under the username)


def main():
    view_options = ["view", "view purchases", "view past purchases", "view my purchases"]
    convert_to_options = ["convert to another currency", "to other currency", "to another currency", "convert to other currency", "convert dollars to another currency", "convert from dollars to another currency", "convert from dollars to other currency"]
    convert_from_options = ["convert from another currency", "from other currency", "from another currency", "convert from other currency", "convert to dollars from another currency", "convert to dollars from other currency"]
    exit_options = ["exit", "quit", "to exit", "exiting", "e"]

    print("Hi, welcome to Katie's currency!")
    options = input("Would you like to view past purchases, convert USD to another currency, convert to USD from another currency, or exit the program? ")
    while options.lower() not in exit_options:#while not exit
        while options.lower() not in view_options and options.lower() not in convert_to_options and options.lower() not in convert_from_options:#if it's not in the options, no can do
            options = input("Sorry, I didn't catch that. Would you like to view past purchases, convert USD to another currency, or convert from USD to another currency? ")
        if options.lower() in view_options:
            username = input("What is your username? ")
            fn = f"{username}.txt"#basically just filename
            show_history(fn)
            options = input("Would you like to view past purchases, convert USD to another currency, convert to USD from another currency, or exit the program? ")#rerun! this couldn't go outside of the if statements because it would just keep looping, because option would just stay the same
        elif options.lower() in convert_to_options:
            to_or_from = "convert to"
            fc, cn = calculations(to_or_from)
            saving_history(fc, cn, to_or_from) #saves to_or_from so that it knows how to record it in the user's histroy file
            options = input("\nWould you like to view past purchases, convert USD to another currency, convert to USD from another currency, or exit the program? ")
        elif options.lower() in convert_from_options:      
            to_or_from = "convert from"
            fc, cn = calculations(to_or_from)
            saving_history(fc, cn, to_or_from) 
            options = input("\nWould you like to view past purchases, convert USD to another currency, convert to USD from another currency, or exit the program? ")
    print("\nOkay, all done! Your history has been saved. Remember your username to access it again.") #all done!
if __name__ == "__main__":
    main()    