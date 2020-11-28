# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import discord





# Press the green button in the gutter to run the script.
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
        print("[INFO] judgeBot is ready!")


    client.run(token)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


