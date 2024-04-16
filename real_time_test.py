import csv
import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime

# Note: for information on how to use this example code please read https://metaapi.cloud/docs/client/usingCodeExamples/

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIxOGM2ZTc1MjUyMzVkNWYyYzA1ODNkMGRiMTRlYWM0NSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6ImJpbGxpbmctYXBpIiwibWV0aG9kcyI6WyJiaWxsaW5nLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19XSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6IjE4YzZlNzUyNTIzNWQ1ZjJjMDU4M2QwZGIxNGVhYzQ1IiwiaWF0IjoxNzA3NzAxNDg0fQ.HeO1TVSdA9JZhrFgYiqKQ2OqCd-uPCzwIS7UPqzcs6DrswicHQqaNtFVPvydXt3AvCk75T7-ILehIhooyZFQXd7yeV_ds4mLk4eT_nHEUNwEk5Oi4BaKwjlQwQ8TNLO0oUFnlKMVURiqlPx0zH_7bm8gJSGPuTcQMzGiIcojZoW5E-6PqlGH7f9RGIZ2bUSC-LPbYbHM9VJW8kVfzMmdITofUCcdZdn-ofVTbazQepzZYFXMvuWLg2d5xP6HcbdohFAjkLDNeDPrD8GIxopr2tCv8BwOeZ_ek3Gjiswy_ESbu32Ayp06oE3ds9CmFi2YlA-Nu4FG3ZbPRXfvX_Z9GgGkRRJAdvb5dEl-W2lanN5VFSiDTQVgtbg5rj9XkfggOWWZ3LxV9UKbj2-k7knhwVVBZCOATApdLiZrrafomDisvOn0nppn83Y2s1kTV3qHAw-IWqHdYlt8jWuJ2gFgM6MLo1XRu9o-mEa_XJdkuAAajVQXlwvQPzCSM0-yubp0PDxCfjzuBNZ5ndseQ87Y6Y3Mr3bEVwr_ZiJ4iHmfM_UyEe6iPz4WonmdYFz-kqVf1MQb91u-tRomgBir4xq_DKSX7-OsU3ABYFHo1O0Un7U57qBFMLAt4JfHhYrR8_vaOnjsFk1_x_X-Fz-aZyToH5mum7ZCnD7xqKNy9r7ggnQ'
login = os.getenv('LOGIN') or '5731616'
password = os.getenv('PASSWORD') or '1w4I8U6w'
server_name = os.getenv('SERVER') or 'OANDA-Demo-1'


async def meta_api_synchronization():
    api = MetaApi(token)
    try:
        # Add test MetaTrader account
        accounts = await api.metatrader_account_api.get_accounts_with_infinite_scroll_pagination()
        account = None
        for item in accounts:
            if item.login == login and item.type.startswith('cloud'):
                account = item
                break
        if not account:
            print('Adding MT4 account to MetaApi')
            account = await api.metatrader_account_api.create_account(
                {
                    'name': 'Test account',
                    'type': 'cloud',
                    'login': login,
                    'password': password,
                    'server': server_name,
                    'platform': 'mt4',
                    'magic': 1000,
                }
            )
        else:
            print('MT4 account already added to MetaApi')

        #  wait until account is deployed and connected to broker
        print('Deploying account')
        await account.deploy()
        print('Waiting for API server to connect to broker (may take couple of minutes)')
        await account.wait_connected()

        # connect to MetaApi API
        connection = account.get_streaming_connection()
        await connection.connect()

        # wait until terminal state synchronized to the local state
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await connection.wait_synchronized()

        # access local copy of terminal state
        print('Testing terminal state access')
        terminal_state = connection.terminal_state
        print('connected:', terminal_state.connected)
        print('connected to broker:', terminal_state.connected_to_broker)
        print('account information:', terminal_state.account_information)
        print('positions:', terminal_state.positions)
        print('orders:', terminal_state.orders)
        print('specifications:', terminal_state.specifications)
        print('EURUSD specification:', terminal_state.specification('EURUSD'))
         # Function to handle price updates
        def on_price_update(symbol, price):
            print(f"Price update for {symbol}: {price}")

        # Subscribe to EURUSD price updates
        async def subscribe_to_eurusd():
            # Define the event handler for price updates
            def price_update_listener(quote):
                on_price_update(quote['symbol'], quote)

            # Add the event listener for price updates
            connection.add_price_listener(price_update_listener)

            # Subscribe to EURUSD quotes
            await connection.subscribe_to_market_data('EURUSD')

        # Run the subscription function
        await subscribe_to_eurusd()

        # Keep the script running to listen for price updates
        while True:
            await asyncio.sleep(1)  # Sleep to prevent the script from exiting

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # It's a good practice to disconnect and cleanup on script termination
        await connection.unsubscribe_from_market_data('EURUSD')
        await connection.close()

if __name__ == "__main__":
    asyncio.run(meta_api_synchronization())
       

#        # finally, undeploy account after the test
#        print('Undeploying MT4 account so that it does not consume any unwanted resources')
#        await connection.close()
#        await account.undeploy()
#
#    except Exception as err:
#        # process errors
#        if hasattr(err, 'details'):
#            # returned if the server file for the specified server name has not been found
#            # recommended to check the server name or create the account using a provisioning profile
#            if err.details == 'E_SRV_NOT_FOUND':
#                print(err)
#            # returned if the server has failed to connect to the broker using your credentials
#            # recommended to check your login and password
#            elif err.details == 'E_AUTH':
#                print(err)
#            # returned if the server has failed to detect the broker settings
#            # recommended to try again later or create the account using a provisioning profile
#            elif err.details == 'E_SERVER_TIMEZONE':
#                print(err)
#        print(api.format_error(err))
#    exit()
#

asyncio.run(meta_api_synchronization())
