'''
to do:
readme
in line comments
fix whatever is happening with initial input

'''
import datetime

convert_to_other_currencies = {
    "Euro": 0.87,
    "Japanese yen": 154.19,
    "Pound sterling": 0.76,
    "Canadian dollar": 1.41,
    "Mexican peso": 18.50,
    "Chinese yuan": 7.12,
    "South African rand": 17.31,
    "Indian rupee": 88.74
}

convert_from_other_currencies = {
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
    
    if to_or_from == "convert to":
        currency_name = input("What is currency you would like to convert to? ")     
        while currency_name.lower() not in currency_options:
            currency_name = input("Sorry, I didn't recognize that currency. Please try again. ")
        initial_value = input("What is the original cost? (In dollars) ")
        while True:
            try:
                int(initial_value)
                break
            except ValueError:
                initial_value = input("I didn't recognize that as a number. Please try again. What is the original cost? (In dollars) ")       
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
        currency_rate = convert_to_other_currencies[currency_name] 
    elif to_or_from == "convert from":    
        currency_name = input("What is currency you would like to convert from? ")
        while currency_name.lower() not in currency_options:
            currency_name = input("Sorry, I didn't recognize that currency. Please try again. ")
        initial_value = input("What is the original cost? (In another currency) ")
        while True:
            try:
                int(initial_value)
                break
            except ValueError:
                initial_value = input("I didn't recognize that as a number. Please try again. What is the original cost? (In dollars) ")   
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
    final_currency = int(initial_value) * int(currency_rate)    
    print(f"The final answer is {final_currency} in {currency_name}.")
    return final_currency, currency_name

def saving_history(final_currency, currency_name):
    username = input("What is your username? ")
    filename = f"{username}.txt"
    try:
        file = open(filename, 'x') 
    except FileExistsError:
        file = open(filename, 'a')
    x = datetime.datetime.now()  
    todays_date = (x.strftime("%m/%d/%Y"))  
    file.write(f"{todays_date} - {final_currency}, {currency_name}\n")       
    file.close()     
    return filename

def show_history(filename):
    while True:
        try:
            user_file = open(filename, 'r')
            break
        except FileNotFoundError:
            username = input("Sorry, I couldn't find anything under that username. Please try another. ") 
            filename = f"{username}.txt"
    file_content = user_file.read()
    print(file_content)


def main():
    view_options = ["view", "view purchases", "view past purchases", "view my purchases"]
    convert_to_options = ["convert to another currency", "to other currency", "to another currency", "convert to other currency", "convert dollars to another currency", "convert from dollars to another currency", "convert from dollars to other currency"]
    convert_from_options = ["convert from another currency", "from other currency", "from another currency", "convert from other currency", "convert to dollars from another currency", "convert to dollars from other currency"]
    exit_options = ["exit", "quit", "to exit", "exiting", "e"]

    print("Hi, welcome to Katie's currency!")
    options = input("Would you like to view past purchases, convert dollars to another currency, convert to dollars from another currency, or exit the program? ")
    while options.lower() not in exit_options:
        while options.lower() not in view_options and options.lower() not in convert_to_options and options.lower() not in convert_from_options:
            options = input("Sorry, I didn't catch that. Would you like to view past purchases, convert dollars to another currency, or convert from dollars to another currency? ")
        if options.lower() in view_options:
            username = input("What is your username? ")
            fn = f"{username}.txt"
            show_history(fn) #repeats
        elif options.lower() in convert_to_options:
            to_or_from = "convert to"
            fc, cn = calculations(to_or_from)
            saving_history(fc, cn) 
        elif options.lower() in convert_from_options:      
            to_or_from = "convert from"
            fc, cn = calculations(to_or_from)
            saving_history(fc, cn) 
    print("Bye bye!")

if __name__ == "__main__":
    main()    