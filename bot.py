#AND I AM IRONMAN!!

import discord
from discord.ext import commands
from music_cog import music_cog
from image_cog import image_cog

import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")

Bot = commands.Bot(command_prefix='$')

Bot.add_cog(image_cog(Bot))
Bot.add_cog(music_cog(Bot))

###########################COMMAND TO REPEAT YOUR STATEMENT "$echo"#########################
@Bot.command()
async def echo(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)

@Bot.command(name="Introduce_Yourself", help="The bot introduces himself")
async def tell_me_about_yourself(ctx):
    text = "My name is Cheems Music Bot\n I was built by Kaif Ahmed AKA OrionAlpha.\nAt present I have limited features like:\n1. Search images on a given topic and get it for you.\n2. Play your favourite music!! "
    await ctx.send(text)

if __name__ == "__main__":
    Bot.run(DISCORD_TOKEN)
    



