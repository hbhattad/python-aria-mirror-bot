from pyrogram import Client

API_KEY = int(input("Enter API KEY:1512546 "))
API_HASH = input("Enter API HASH:c87b9fb36da0ff6b8c9127d5e7dae2dd ")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
