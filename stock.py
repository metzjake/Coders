# Purpose:  This program will search a dictionary for a stock symbol. If found
#           stock symbol and price will be printed to screen otherwise an error
#           message will be printed

import sys

# Dictionary with stock symbol and price
stock_dict = {
  "GOOGL"  : "96.94",
  "TGT"  : "168.51",
  "MSFT" : "248.16",
  "AMZN" : "102.24",
  "NFLX" : "360.77",
  "INTC" : "28.16",
  "DIS"  : "109.54",
  "KO"   : "60.49",
  "PG"   : "140.57",
  "MRK"  : "105.38",
  "O"    : "66.40"
}
def main():
  
  # Get stock symbol from user and convert input to upper case
  stock_ticker = input("Enter a stock symbol to lookup: ")
  stock_ticker = stock_ticker.upper()

  # Lookup stock symbol in dictionary with get() otherwise print error
  print("\n")
  result = stock_dict.get(stock_ticker, "stock symbol is not found in dictionary!")

  # Print out stock ticker and price
  print(f"{stock_ticker}  {result}")

  # Ask user if they want to run the program again
  print("\n")
  restart = input("Do you wish to enter another conversion? Press Y to continue or any other key to exit: ")
  if restart == "Y" or restart == "y":
    print("\n")
    main()
  else:
    print("\nThanks for using the New York Stock Exchange lookup.")
    sys.exit()
    
print("Welcome to the stock exchange!\n")    
# Call the main function
main()