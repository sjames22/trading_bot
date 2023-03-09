import alpaca_trade_api as tradeapi

# Set API keys
api_key = 'YOUR_API_KEY'
secret_key = 'YOUR_SECRET_KEY'

# Connect to the API
api = tradeapi.REST(api_key, secret_key, base_url='')
