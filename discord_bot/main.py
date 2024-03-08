from discord import Intents, Client
from responses import get_response

# SET UP TOKEN
TOKEN = 'MTIxNTA0MzI2NzY2MjU3Nzc2NQ.GOiCMu.A1m9utctCzmJ76dsG6gWebagIbd6RLHjo9Kd2g'

# SET UP BOT
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# READ MESSAGE

async def send_message(message, user_message):
    if not user_message:
        print('No message due to not enabled intents...')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response = str(get_response(user_message))
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{message}')
    await send_message(message, user_message)

def main():
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()
