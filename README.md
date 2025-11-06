# 2526-2ACS2-PA3
Design Thinking Final Passion Project

# Empathize: 
Someone struggles to easily convert between their home country's currencies and the others they encounter. (could be travel, immigration, etc)

# Research
https://www.ig.com/en/trading-strategies/what-are-the-top-10-most-traded-currencies-in-the-world-200115
    - Euros, yen, pounds, CAD, pesos, yuan, South African rand, Indian rupees

https://www.reddit.com/r/AskAnAmerican/comments/18vwq4v/do_americans_think_about_exchange_rates/    
    - exchange rates change over time
    - value of currency differs depending on type
    - USD determines cost of many daily goods 
    - Americans think about exchange rates when traveling
        - others find it useful due to value of USD
    - immigrants acclimating to American life often translate USD back to their home currency to get a better feel for its value    

https://www.riamoneytransfer.com/en/blog/how-exchange-rates-can-impact-you-when-living-abroad/
    - rates can change by the minute
    - foreign exchange market runs 24 hours a day, five days a week
    - economic conditions, inflation, interest rates, and supply and demand all effect exchange rates
    - Euro and USD are fixed by governments' central banks
    - airports overcharge

# HMW
How might we help our client calculate the exchange rates between currencies?

# Ideate
- A program that supplies updated exchange rates for user's convenience.
- A program that predicts whether your currency's value is going up or down.
- A program that converts other currencies to and from USD.
- A program that helps users budget in multiple currencies. 

# Prototype
This program can convert between USD and eight other common currencies. It saves a history of each user's purchases in a separate file. The user chooses whether to start or end in USD and inputs a currency and monetary value. The program creates a file under their username and stores the date, the amount, and the currencies converted between. The user can perform more conversions, view their history, or exit the program.

# Reflect
WWW: I think error handling went well! I was not able to break the program, and neither was my peer tester. Try/except definitely came in handy.

EBI: I wish I could make it so that the exchange rates are updated correctly over time, like if the program got the value from an online source.

IMT: If I had more time, I would add more currencies. I would also make it so that the user didn't have to input their username so often, but I didn't have time to move the variables around and do that (shoutout week five!). I would also do nicer formating. I'd also make the rates more standardized so that the user doesn't need to go between USD when converting.