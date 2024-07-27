import asyncio
import nest_asyncio
from lcu_driver import Connector

# Apply nest_asyncio to allow nested use of asyncio
nest_asyncio.apply()

client = Connector()

@client.ready
async def lcu_ready(connection):
    try:
        # Fetch current summoner
        summoner_response = await connection.request("get", '/lol-summoner/v1/current-summoner')
        summoner_data = await summoner_response.json()
        print("Summoner Data:", summoner_data)
    except Exception as e:
        print(f"Error fetching summoner data: {e}")

@client.ws.register('/lol-matchmaking/v1/ready-check', event_types=("UPDATE",))
async def auto_accept_match(connection, event):
    try:
        if event.data['playerResponse'] == "None":
            await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')
            print("Match Accepted!")
    except Exception as e:
        print(f"Error handling match acceptance: {e}")

async def start_client():
    try:
        await client.start()
        # Keep the client running indefinitely
        while True:
            await asyncio.sleep(3600)  # Sleep for an hour; adjust as needed
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        # Ensure proper shutdown
        if hasattr(client, 'close'):
            await client.close()  # Properly close the client
        else:
            print("Client does not have a close method.")

if __name__ == "__main__":
    asyncio.run(start_client())
