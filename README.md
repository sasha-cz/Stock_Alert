# Stock_Alert

The goal of this project was to develop a stock alert program using Python that calculates the percentage change in a stock's value. The percentage change is determined by comparing yesterday's closing price to the closing price two days ago. If the stock's value increases or decreases by more than 5%, the program will output the three latest news articles about the corresponding company. 

The program can be also extended by code for sending e-mail alerts (see the hashed code example at the end of main.py). To automate this program as an e-mail stock alert, you need to host it in the cloud (e.g. pythonanywhere).

## Step One: Get your API Keys

First you need to get two own API keys for this project.
   
Visit https://www.alphavantage.co/support/#api-key. After filling in the form, click on 'Get Free API Key'. Keep your now generated key somewhere save. In main.py pass it either directly as a string to the variable `stock_api_key` instead of `os.environ.get("STOCK_API_KEY")` or create an environment variable (e.g. `STOCK_API_KEY`) with your API key and pass it to `stock_api_key` like in the code example.  

For generating an API key for the variable `news_api_key` visit https://newsapi.org/register. After you registered for the API key, you'll be forwarded to a new page and the key will be displayed. You'll receive also an e-mail with your API-key. Pass your key to the `news_api_key` variable like described in the 'stock_api_key' paragraph above.

## Step Two: Choose a Company and their Symbol 

Customize the global variables `STOCK_SYMBOL` (in main.py) and `COMPANY_NAME` (in news_request.py). 
The required symbol is the symbol of the equity of your choice. For example: `symbol=IBM`. You can find the symbol for your equity e.g. here: [https://www.tradingview.com/markets/](https://www.tradingview.com/markets/).

## Step Three: Run main.py 

Run main.py to obtain the percentage change that your stock increased / decreased and receive eventually the latest news.



