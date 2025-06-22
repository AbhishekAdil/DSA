# Data stuctres are building blocks or raw material for any software programs

# One can't become a good programmer without sound understanding of data structures

# Use right data structure for a problem

# Some of data stuctures are - Array, Linklists, trees etc..
# They are containers storing data in a specific memory layout

# Exaple:

'''        1)
Store apple's stock price for 5 days and answer,
1. What was the price on day 1
2. What was the price on day 3

#Store using list

stock_price = [298, 305, 320, 301, 292]

stock_price[0]   <---- Stock price on day 1

stock_price[2]   <---- Stock price on day 3
'''

stock_price = [298, 305, 320, 301, 292]

print(stock_price[0])  # <---- Stock price on day 1

print(stock_price[2])  # <---- Stock price on day 3


'''        2)
Store apple's stock price from march 4 to march 7 and answer,
1. What was the price on march 7
2. What was the price on march 5

# Store using dictionary

stock_price = {
            'march 4' : 298,
            'march 5' : 305,
            'march 6' : 320,
            'march 7' : 301
            }

stock_price['march 7']    <--- march 7 price

stock_price['march 5']    <--- march 5 price
'''

stock_price = {
            'march 4' : 298,
            'march 5' : 305,
            'march 6' : 320,
            'march 7' : 301
            }

print(stock_price['march 7'])    #<--- march 7 price

print(stock_price['march 5'])    #<--- march 5 price


# we use different data stuctures according to the data and our requirements