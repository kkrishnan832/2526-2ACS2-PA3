'''
to do:
readme
create alternatives for all the other currencies
do more try/except
figure out what's wrong w to_or_from
loop what happens when file_not_found_error
'''

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

view_options = ["view", "view purchases", "view past purchases", "view my purchases"]
convert_to_options = ["convert to another currency", "to other currency", "to another currency", "convert to other currency", "convert dollars to another currency", "convert from dollars to another currency", "convert from dollars to other currency"]
convert_from_options = ["convert from another currency", "from other currency", "from another currency", "convert from other currency", "convert to dollars from another currency", "convert to dollars from other currency"]
exit_options = ["exit", "quit", "to exit", "exiting", "e"]
    
def calculations(to_or_from):
    if to_or_from == "convert to":
        currency_name = input("What is currency you would like to convert to? ")
        if currency_name.lower in ['euro', 'euros']:
            currency_name = "Euro"
        elif currency_name.lower in ['yen', 'yens', 'japanese yen', 'japanese yens', 'japanese', 'japan']:
            currency_name = "Japanese yen"
        #do the same for all the other currencies        
        initial_value = input("What is the original cost? (In dollars) ")
        currency_rate = convert_to_other_currencies[currency_name] 
    elif to_or_from == "convert from":    
        currency_name = input("What is currency you would like to convert from? ")
        initial_value = input("What is the original cost? (In another currency) ")
        currency_rate = convert_from_other_currencies[currency_name]
    final_currency = initial_value * currency_rate    
    print(f"The final answer is {final_currency} {currency_name}.")

def saving_history():
    username = input("What is your username?")
    try:
        open('{username}.txt', 'x') 
    except FileExistsError:
        open('{username}.txt', 'a')    

def show_history():
    try:
        user_file = open('{username}.txt', 'r')
        file_content = user_file.read()
        print(file_content)
    except FileNotFoundError:
        print("Sorry, I couldn't find anything under that username. Please try again.")
        #loop it    


def main():
    print("Hi, welcome to Katie's currency!")
    options = input("Would you like to view past purchases, convert dollars to another currency, convert to dollars from another currency, or exit the program? ")
    while options.lower not in exit_options:
        while options.lower not in view_options and options.lower not in convert_to_options and options.lower not in convert_from_options:
            to_or_from = input("Sorry, I didn't catch that. Would you like to view past purchases, convert dollars to another currency, or convert from dollars to another currency?")
        if options.lower in view_options:
            show_history()
        elif options.lower in convert_to_options:
            to_or_from = "convert to"
            calculations()
        elif options.lower in convert_from_options:      
            to_or_from = "convert from"
            calculations()
        saving_history()      
    print("Bye bye!")