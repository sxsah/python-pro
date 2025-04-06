import os
import random
import discord
import requests
from discord.ext import commands

 

intents = discord.Intents.default()

intents.message_content = True

 

bot = commands.Bot(command_prefix='$', intents=intents)

 

@bot.event

async def on_ready():

    print(f'We have logged in as {bot.user}')

 

@bot.command()

async def hello(ctx):

    await ctx.send(f'Hola, soy un bot {bot.user}!')

 

@bot.command()

async def heh(ctx, count_heh = 5):

    await ctx.send("he" * count_heh)



@bot.command()

#str -> string : pablo,pedro 

async def saludo(ctx, name : str):

    await ctx.send(f"Hola, {name} bienvenido a mi canal de discord")

@bot.command()

async def add(ctx, left: int, right: int):

    """Adds two numbers together."""

    await ctx.send(left + right)
@bot.command()

async def mem(ctx):

    with open('imagenes/meme1.jpeg', 'rb') as f:

        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!

        picture = discord.File(f)
    await ctx.send(file=picture)




@bot.command()

async def meme1(ctx):

    imagenes = os.listdir('imagenes')

    with open(f'imagenes/{random.choice(imagenes) }', 'rb') as f:

            picture = discord.File(f)

    # A continuación, podemos enviar este archivo como parámetro.

    await ctx.send(file=picture)

    # A continuación, podemos enviar este archivo como parámetro.


@bot.command()

async def repeat(ctx, times: int, content='repeating...'):

    """Repeats a message multiple times."""

    for i in range(times):

        await ctx.send(content)
def get_duck_image_url():    

    url = 'https://random-d.uk/api/random'

    res = requests.get(url)

    data = res.json()

    return data['url']

 

 

@bot.command('duck')

async def duck(ctx):

    '''Una vez que llamamos al comando duck, 

    el programa llama a la función get_duck_image_url'''

    image_url = get_duck_image_url()

    await ctx.send(image_url)

@bot.command()

async def poke(ctx,arg):

    try:

        pokemon = arg.split(" ",1)[0].lower()

        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)

        if result.text == "Not Found":

            await ctx.send("Pokemon no encontrado")

        else:

            image_url = result.json()["sprites"]["front_default"]

            print(image_url)

            await ctx.send(image_url)

    except Exception as e:

        print("Error:", e)

@poke.error

async def error_type(ctx,error):

    if isinstance(error,commands.errors.MissingRequiredArgument):

        await ctx.send("Tienes que darme un pokemon")
@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)# esta linea saluda
    await ctx.send("Quieres que te hable acerca de la contaminación del agua?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == 'si':
            await ctx.send("""La contaminación del agua es la alteración de la calidad del agua por la presencia de sustancias o agentes contaminantes.
                        """)   
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre otros juegos, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("Quieres conocer algunas ejemplo de contaminación, responde 'sí' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("1. Contaminación organica")
            await ctx.send("1. Contaminación de quimica") 
        else:
            await ctx.send("Está bien, si alguna vez quieres conocer ejemplos de contaminacion estamos en contacto")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
