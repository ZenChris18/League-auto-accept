# lcu_connector.py
from lcu_driver import Connector

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

def start_connector():
    client.start()

def stop_connector():
    client.stop()
