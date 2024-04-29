#define the function calculating how many chocolate bars the user is able to afford at the supermarket
def buy(total_money,price):
    #calculate
    number=total_money//price
    left_money=total_money%price
    #print the result
    print('You can buy',str(number),'chocolate bars and',str(left_money),'will be left.')
    return()
#example of calling the function
buy(100,3)