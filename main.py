# インストールした discord.py を読み込む
import discord

# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print("discord bot started.")


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')



# load token
print("Loading bottoken.txt")
file = open('bottoken.txt', 'r', encoding='UTF-8')
token = file.read()
file.close()
print("Loaded bottoken.txt")

print(token)

# Botの起動とDiscordサーバーへの接続
client.run(token)
