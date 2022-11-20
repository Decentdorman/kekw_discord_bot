import discord
from discord.ext import commands
import secrets
import wavelink

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = 'MTA0MzY3NDkwNDMyODk0MTU3OQ.GbzDGP.xrVLa8HWIdU4nkFOuQWhHZojhs5dhIFClB9ET0'


class CustomPlayer(wavelink.Player):
    
    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()


@client.event
async def on_ready():
    client.loop.create_task(connect_nodes())

async def connect_nodes():
    await client.wait_until_ready()
    await wavelink.NodePool.create_node(
        bot=client,
        host='localhost',
        port=2333,
        password='youshallnotpass'
    )


@client.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f'Node: <{node.identifier}> is ready!')



@client.command()
async def connect(ctx):
    vc = ctx.voice_client
    try:
        channel = ctx.author.voice.channel
    except AttributeError:
        return await ctx.send("Please join a voice channel to connect")

    if not vc:
        await ctx.author.voice.channel.connect(cls=CustomPlayer())
    else:
        await ctx.send("The bot is alreadt connected to a voice channel")


@client.command()
async def disconnect(ctx):
    vc = ctx.voice_client
    if vc:
        await vc.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def play(ctx, *, search: wavelink.YouTubeTrack):
    vc = ctx.voice_client
    if not vc:
        custom_player = CustomPlayer()
        vc : CustomPlayer = await ctx.author.voice.channel.connect(cls=custom_player)

    if vc.is_playing():

        vc.queue.put(item=search)

        await ctx.send(embed=discord.Embed(
            title=search.title,
            url=search.uri,
            author=ctx.author,
            description=f"Queued {search.title} in {vc.channel}")
        )
        
    else:
        await vc.play(search)

        await ctx.send(embed=discord.Embed(
            title=vc.source.title,
            url=vc.source.uri,
            author=ctx.author,
            description=f"Playing {vc.source.title} in {vc.channel}")
        )

client.run(TOKEN)
