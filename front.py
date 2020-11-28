import discord
from main import logic

if __name__ == '__main__':
    print("[INFO] judgeBot Python is ready!")

    # GetToken
    text_file = open("token.txt", "r")
    token = text_file.readlines()[0]
    client = discord.Client()


    @client.event
    async def on_ready():
        activity = discord.Game(name="Who Is The Evil", type=3)
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print("[INFO] judgeBot DiscordBot is ready!")



    @client.event
    async def on_message(message):
        print(message)
        print(message.content)
        reply = logic.getQuote(message.content)
        if reply:
            await message.channel.send(reply)


    logic = logic()
    client.run(token)


