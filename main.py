
import discord

client = discord.Client()


@client.event
async def on_ready():
    print("ready")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
        await message.channel.send("Hello!")


@client.event
async def on_message(message):
    if message.content == "/create":
        ch = await message.channel.category.create_text_channel(name="ch")
        await message.channel.send(ch.mention + " を作成しました。")


@client.event
async def on_message(message):
    if message.content == "/servers":
        await message.channel.send(len(client.guilds))
        await message.channel.send(len(message.guild.members))
        

# load token
print("Loading bottoken.txt")
file = open('bottoken.txt', 'r', encoding='UTF-8')
token = file.read()
file.close()
print("Loaded bottoken.txt")

print(token)

# bot ready
client.run(token)
