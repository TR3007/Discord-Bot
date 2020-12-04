# Work with Python 3.6
import discord

TOKEN = 'Nzg0Mzg0Nzk5NzQxNTc1MTc4.X8ohRQ.QPI38k5wgrQ06OwM8DXap2rEt38'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(''):
        msg = 'cazzo dici {0.author.mention}'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
