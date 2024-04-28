from metaapi_cloud_sdk import MetaApi
from asyncio import run, gather, sleep

# Your MetaApi API token
api_token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIxOGM2ZTc1MjUyMzVkNWYyYzA1ODNkMGRiMTRlYWM0NSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6ImJpbGxpbmctYXBpIiwibWV0aG9kcyI6WyJiaWxsaW5nLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19XSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6IjE4YzZlNzUyNTIzNWQ1ZjJjMDU4M2QwZGIxNGVhYzQ1IiwiaWF0IjoxNzA3NzAxNDg0fQ.HeO1TVSdA9JZhrFgYiqKQ2OqCd-uPCzwIS7UPqzcs6DrswicHQqaNtFVPvydXt3AvCk75T7-ILehIhooyZFQXd7yeV_ds4mLk4eT_nHEUNwEk5Oi4BaKwjlQwQ8TNLO0oUFnlKMVURiqlPx0zH_7bm8gJSGPuTcQMzGiIcojZoW5E-6PqlGH7f9RGIZ2bUSC-LPbYbHM9VJW8kVfzMmdITofUCcdZdn-ofVTbazQepzZYFXMvuWLg2d5xP6HcbdohFAjkLDNeDPrD8GIxopr2tCv8BwOeZ_ek3Gjiswy_ESbu32Ayp06oE3ds9CmFi2YlA-Nu4FG3ZbPRXfvX_Z9GgGkRRJAdvb5dEl-W2lanN5VFSiDTQVgtbg5rj9XkfggOWWZ3LxV9UKbj2-k7knhwVVBZCOATApdLiZrrafomDisvOn0nppn83Y2s1kTV3qHAw-IWqHdYlt8jWuJ2gFgM6MLo1XRu9o-mEa_XJdkuAAajVQXlwvQPzCSM0-yubp0PDxCfjzuBNZ5ndseQ87Y6Y3Mr3bEVwr_ZiJ4iHmfM_UyEe6iPz4WonmdYFz-kqVf1MQb91u-tRomgBir4xq_DKSX7-OsU3ABYFHo1O0Un7U57qBFMLAt4JfHhYrR8_vaOnjsFk1_x_X-Fz-aZyToH5mum7ZCnD7xqKNy9r7ggnQ'
# Your MetaTrader account id
account_id = '5731616'

# A coroutine to subscribe to and print real-time forex quotes
async def stream_forex_quotes():
    # Instantiate the MetaApi API
    metaapi = MetaApi(api_token)
    
    try:
        # Retrieve your MetaTrader account
        account = await metaapi.metatrader_account_api.get_account(account_id)
        
        # Connect to MetaTrader account
        connection = await account.connect()
        
        # Wait for the connection to be established and synchronized
        print('Waiting for API server to connect to MetaTrader terminal...')
        await connection.wait_synchronized()
        
        # Define a handler to process quotes
        def on_quote(quote):
            print(f'Received quote: {quote}')
        
        # Subscribe to quotes for the USD/EUR currency pair
        await connection.subscribe_to_quotes(['EURUSD'], 1)
        connection.add_synchronization_listener(on_quote)
        
        # Keep the script running to continue receiving quotes
        print('Subscribed to EURUSD quotes, waiting for updates...')
        while True:
            await sleep(1)
    
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    finally:
        # It's important to gracefully close the connection when done
        await connection.unsubscribe_from_quotes(['EURUSD'])
        await connection.close()

# Run the coroutine
if __name__ == '__main__':
    run(stream_forex_quotes())

