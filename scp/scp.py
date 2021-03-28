import discord
from discord.colour import Color
from discord.errors import Forbidden, HTTPException
import pyscp # Installed On Cog install, using https://github.com/NorthWood-Cogs/pyscp
import asyncio
import aiohttp
import os

from redbot.core import commands, Config, data_manager
from typing import Optional
from redbot.core.commands import Cog

cromURL = "https://api.crom.avn.sh/"

class SCP(commands.Cog):
    """ SCP Cog that utilises Crom - https://crom.avn.sh/"""
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier="3957890832758296589023290568043")
        self.config.register_global(
                isthisjustawayofsavingmytime=True,
                configLocation=str(data_manager.cog_data_path(self) / "scp.db")
        )    

    @commands.command(name="scp")
    async def _scp(self, ctx, *, scp):
        await self.CromRequest(scp=scp)




    async def CromRequest(scp):
        async with aiohttp.ClientSession() as session:
            json = ("""searchPages(query: "{querytarget}") 
            {url
                wikidotInfo {
                    title
                    rating
                    thumbnailUrl
                }
                alternateTitles {
                    type
                    title
                }
                attributions {
                    type
                    user {
                        name
                    }
                }
            }
        }""".format(querytarget=scp)) # Ye gods
            async with session.get(cromURL+json) as response:
                print(response)

