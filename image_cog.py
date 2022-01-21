import discord
from discord.ext import commands
import os , shutil
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command
from google_images_download import google_images_download
import random
 
class image_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.download_folder = 'downloads'
        
        
        self.keywords = 'Lamborghini'
        
        self.response = google_images_download.googleimagesdownload()
        
        self.arguements = {
            "keywords": self.keywords,
            "limit": 20,
            "size": "medium",
            "no_directory": True
        }
        
        self.image_names = []
        
        self.update_images()
        
    def update_images(self):
        for filename in os.listdir(self.download_folder):
            self.image_names.append(os.path.join(self.download_folder, filename))
            
    def clear_folder(self):
        for filename in os.listdir(self.download_folder):
            file_path = os.path.join(self.download_folder , filename)
            try: 
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s, Reason %s" % (file_path, e))
                
    @commands.command(name="Get", help="This command is to get the images you have searched for")
    async def get(self, ctx):
        images_size = len(self.image_names) - 1
        random_image = random.randint(0, images_size)
        img_path = self.image_names[random_image]

        await ctx.send(file=discord.File(img_path))

    @commands.command(name="Search", help="This command is to search online and get the images on the mentioned topic")
    async def search(self , ctx , *args):
        search_args = " ".join(args)

        self.clear_folder()
        self.arguements['keywords'] = search_args
        self.response.download(self.arguements)

        self.update_images()

        
                