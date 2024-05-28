import asyncio
from Servicio import Servicio
import discord
from discord.ext import commands
import youtube_dl

# Configurar el cliente de Discord
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)
servicio = Servicio()
# Eventos
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("No estás en un canal de voz.")
        return

    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def play(ctx, *, url=None):
    if not ctx.voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("Debes estar en un canal de voz.")
            return

    voice = ctx.voice_client

    if voice.is_playing():
        if url:
            servicio.add_song(url)
            await ctx.send(f"La canción '{url}' ha sido agregada a la lista.")
        else:
            await ctx.send("Ya estoy reproduciendo una canción. Envía el enlace de la canción que deseas agregar a la lista.")
        return

    if not servicio.songs:
        if url:
            servicio.add_song(url)
        else:
            await ctx.send("No hay canciones en la lista. Envía el enlace de la canción que deseas reproducir.")
            return

    while servicio.songs:
        song_info = servicio.songs.pop(0)

        with ytdl:
            player = await ytdl.extract_info(song_info.path, download=False)
        source = await discord.FFmpegOpusAudio.from_probe(player['url'], **ffmpeg_options)
        voice.play(source)

        await ctx.send(f"Reproduciendo: {song_info.title}")

        while voice.is_playing():
            await asyncio.sleep(1)

        print(f"La canción '{song_info.title}' ha sido reproducida.")

    await ctx.send("No hay más canciones en la lista.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!'):
        await bot.process_commands(message)
    else:
        print(f'Mensaje: {message.content} (Canal: {message.channel})')

# Ejecutar el bot
bot.run('TU_TOKEN_DE_BOT')