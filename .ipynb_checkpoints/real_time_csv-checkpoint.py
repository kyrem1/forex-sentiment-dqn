import csv
import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime

# Note: for information on how to use this example code please read https://metaapi.cloud/docs/client/usingCodeExamples/

api_token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIxOGM2ZTc1MjUyMzVkNWYyYzA1ODNkMGRiMTRlYWM0NSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ODMyY2YxMjQtODU3My00ZjdiLWI4ZTQtNDZmYzkyNmVhMDAzIl19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDo4MzJjZjEyNC04NTczLTRmN2ItYjhlNC00NmZjOTI2ZWEwMDMiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjgzMmNmMTI0LTg1NzMtNGY3Yi1iOGU0LTQ2ZmM5MjZlYTAwMyJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjgzMmNmMTI0LTg1NzMtNGY3Yi1iOGU0LTQ2ZmM5MjZlYTAwMyJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDo4MzJjZjEyNC04NTczLTRmN2ItYjhlNC00NmZjOTI2ZWEwMDMiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ODMyY2YxMjQtODU3My00ZjdiLWI4ZTQtNDZmYzkyNmVhMDAzIl19LHsiaWQiOiJtZXRhYXBpLXJlYWwtdGltZS1zdHJlYW1pbmctYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ODMyY2YxMjQtODU3My00ZjdiLWI4ZTQtNDZmYzkyNmVhMDAzIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDo4MzJjZjEyNC04NTczLTRmN2ItYjhlNC00NmZjOTI2ZWEwMDMiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiMThjNmU3NTI1MjM1ZDVmMmMwNTgzZDBkYjE0ZWFjNDUiLCJpYXQiOjE3MDc3MDUzMjgsImV4cCI6MTcxMDI5NzMyOH0.dw4NqvIwxAoKjcticvcB-NWaH-88izlW-W2yUX-y6Z6gdM6mqn194pnNys10xkKM6pi-DtlkFx5b73mveQQYjUCd2KWeKu9Z1Z1S9FqtLbSUeRYJhSFxNjujAjOHLvERKXCJvPANxaH244Mp7ZA8RF6yWNuqbGREPgapSzK13QVB-fD9enuDruic6MVBiuTVqV7Kz1BljYOZzXUIxYMWCDuN_vJvFfH35Zd-3bbmy4hOd6BAQAEFzm7BaGkrwNwD9SEW2xtcbJwSAi9BMFqy6v7SA-hmOeyDRbyV-gFU_KB7TqWjXOAWc1NvKj9XreBm8gm85gO-9MwoAgZS9vzawVLTfyQeTfCI1Q6PfPXubh_a6aNJIahMrKVitubnWZDpOsymQeI69nHsS8iSDYzhgzaBTgXaNzLeR4AeJL0nRK-NhMu31dbz83-aKZRIiPzUggHXlBQqpv2umh1pBNb47UnK1GRmoAikFnJytLNOSSVdyNr1vaO6fUtJ2ElvM8egOEbBMi76tAZkMJuljwBvdTGG9n-Xj_i6fEnOOwDEN9wqGlsgZE_zCsXu058SDCx_75dNku1DiBE9mV7RNXEW0ov844oHnelGSiV_BxjfpqHi1Q7LDsc6_iAbRqPBe4fyP9MzQga98ouwg6F7W2Q5r-E9UEqy_Ozu2-amX5OERa8'
account_id ='832cf124-8573-4f7b-b8e4-46fc926ea003'
password = os.getenv('PASSWORD') or '1w4I8U6w'
server_name = os.getenv('SERVER') or 'OANDA-Demo-1'




# Path to your CSV file
csv_file_path = 'eurusd_prices.csv'

# Function to write data to CSV
def write_to_csv(data):
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Async function to stream USD/EUR data
async def stream_usdeur_data():
    api = MetaApi(api_token)
    account = await api.metatrader_account_api.get_account(account_id)
    connection = account.get_streaming_connection()
    await connection.connect()
    await connection.wait_synchronized()

    # Define a listener to handle price updates
    class PriceListener:
        async def on_symbol_price_updated(self, symbol, prices):
            if symbol == 'EURUSD':
                print(f"Received EUR/USD price update: {prices}")
                # Write the timestamp and price to CSV
                write_to_csv([datetime.now(), prices['bid'], prices['ask']])

    # Add the listener to the connection
    listener = PriceListener()
    connection.add_synchronization_listener(listener)

    # Subscribe to EUR/USD market data
    await connection.subscribe_to_market_data('EURUSD')

    # Keep the script running to continue receiving updates
    while True:
        await asyncio.sleep(1)

# Initialize and run the async function
if __name__ == '__main__':
    # Write CSV headers
    write_to_csv(['Timestamp', 'Bid', 'Ask'])
    asyncio.run(stream_usdeur_data())
