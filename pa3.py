'''
Block comment here
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

    
def calculations(to_or_from):
    if to_or_from = "convert to":
        #use convert to dict
    elif to_or_from = "convert from":    
        #use convert from dict

def saving_history():
    username = input("What is your username?")
    add_user = open('history.txt', 'a')
    add_user.write(username)

def show_history():
    #print ts    



def main():
    print("Hi, welcome to Katie's currency!")
    options = input("Would you like to view past purchases, convert dollars to another currency, or convert to dollars from another currency?")
    if options.lower in view_options:
        show_history()
    elif options.lower in convert_to_options:
        to_or_from == "convert to"
        calculations()
    elif options.lower in convert_from_options:      
        to_or_from == "convert from"
        calculations()
    else:
        to_or_from = input("Sorry, I didn't catch that. Would you like to view past purchases, convert dollars to another currency, or convert from dollars to another currency?")
        #loop it
    saving_history()     
    print("Bye bye!")