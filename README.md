# Stock_Alert

The goal of this project was to build a simple Stock Alert written in Python, which can be also extended by code for sending  e-mail alerts (see the hashed code example at the end of main.py). To automate this program as an e-mail stock alert, you need to host it in the cloud (e.g. pythonanywhere).

## Step One: Get your API Keys

First you need to get two own API keys for this project.
   
Visit https://www.alphavantage.co/support/#api-key. After filling in the form, click on 'Get Free API Key'. Keep your now generated key somewhere save. In main.py pass it either directly as a string to the variable `stock_api_key` instead of `os.environ.get("STOCK_API_KEY")` or create an environment variable (e.g. `STOCK_API_KEY`) with your API key and pass it to `stock_api_key` like in the code example.  

For generating an API key for the variable `news_api_key` visit https://newsapi.org/register. After you registered for the API key, you'll be forwarded to a new page and the key will be displayed. You'll receive also an e-mail with your API-key. Pass your key to the `news_api_key` variable like described in the 'stock_api_key' paragraph above.

## Step Two: Choose a Company and their Symbol 

In main.py customize the global variables `STOCK_SYMBOL` and `COMPANY_NAME`. 
The required symbol is the symbol of the equity of your choice. For example: `symbol=IBM`. You can find the symbol for your equity e.g. at https://www.tradingview.com/markets/.

## Step Three: Run main.py 

Run main.py to get hold of the current difference of yesterday's closing price of your stock and the previous closing price (in percentage). 
If your stock increases/decreases by 5 % or more, get the three latest news about the company.



