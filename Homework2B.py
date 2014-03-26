#This is Ralph Miller's Homework #2B for Programming for Absolute Beginners with Mark Lassoff, completed March 25, 2014
import locale
locale.setlocale( locale.LC_ALL, '' )


itemPrice = input('What is the price of the item?: ')
salesTax = input('What is the sales tax? (expressed as 0.XX)?: ')
totalPrice = itemPrice + (itemPrice * salesTax)
print 'The full price of your item is' , locale.currency(totalPrice)