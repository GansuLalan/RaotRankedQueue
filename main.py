import nextcord
import random, time, asyncio
from nextcord.ext import commands
from nextcord.ui import Button, View
import Token
QueueChat_Channel_ID = '994225283496431639'
Queue_Channel_ID = '994311273250562130'

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
TOKEN = Token.ID
intents = nextcord.Intents().all()
Queue = ['brewskii',
      'aris',
      'madz',
      'tropic']
class aclient(nextcord.ext.commands.Bot(command_prefix='-', intents=intents)):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False
        self.added = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await setup.sync(guild=nextcord.Object(id=nextcord.utils.get(aclient.guilds, name="guild's name").id))
            self.synced = True
        if not self.added:
            self.add_view(button_view())
            self.added = True
        print(f"logged in as {self.user}.")

#def join_queue(player):

class button_view(nextcord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @nextcord.ui.button(label='Join', style=nextcord.ButtonStyle.green, custom_id='Join_Queue_ID')
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('Joined the Queue', ephermal = True)
    @nextcord.ui.button(label='Leave', style=nextcord.ButtonStyle.red, custom_id='Leave_Queue_ID')
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        print(interaction.user)
        await interaction.response.send_message('left the Queue')
        self.value = True
        self.stop()
@aclient.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    userid = str(message.author.id)
    print(f'{username}: {user_message} ({channel})')
    if message.author == client.user:
        print('1')
        return
#    channel_id = nextcord.utils.get(client.get_all_channels(), name=message.channel)
#    print(client.get_all_channels())
    if str(message.channel) == 'testing':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello <@{userid}>')
            return
    await aclient.process_commands(message)

@aclient.command(pass_context=True)
async def setup(ctx):

    embed = nextcord.Embed(
        title = '5v5 Ranked Queue',
        description='description',
        colour = nextcord.Colour.blue()
    )
    embed.set_footer(text='Use the buttons below to join the queue for a Team elimination 5v5')
    embed.set_image(url='https://cdn.nextcordapp.com/attachments/994225283496431639/994344182544080956/Ranked_Guide.png')
    embed.set_thumbnail(url='https://cdn.nextcordapp.com/attachments/994225283496431639/994346170149257348/Insane4.png')
    embed.set_author(name='RAoT Competitive Official',
                     icon_url='https://cdn.nextcordapp.com/icons/876201792457801758/237d8502b900233ddcfadd4e5111b6f3.png')
    embed.add_field(name='info', value='Information goes here', inline=True)
    embed.add_field(name='Players in queue', value=Queue,inline = False)
    QueueControls = View()
    JoinQueue=Button(label='Join', style=nextcord.ButtonStyle.green)
    QueueControls.add_item(JoinQueue)

    await ctx.send(embed=embed, view=QueueControls)

#@client.listen()
#async def on_button(interaction):

client.run(TOKEN)