import discord
import pyscp
from redbot.core import commands
from typing import Optional

from redbot.core.commands import Cog


SCPWiki = pyscp.wikidot.Wiki('scp-wiki.wikidot.com')
ObjectClass = ["Safe", "Euclid", "Keter", "Thaumiel", "Neutralized", "Explained"]
class SCP(commands.Cog):
    """ SCP Cog that utilises an especially adapted wikidot api""" # Their Claim, not mine
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def scp(self, ctx, scpID: str):
        """Finds an SCP based on their number. Standard Content warning applies."""
        target = SCPWiki(f'scp-{scpID}')
        BaseContentText = target.text
        Content = BaseContentText[:300] + (BaseContentText[300:] and '..')
        Heck = Content.find("Special Containment")

        #TODO So because I like colours we're going to make the embed colour based off the object class
        await ctx.send(f"{Heck}")
        scpEM = discord.Embed(
            titlle=f"{target.title}",
            url=f"{target.url}",
            description=f"{Content}"

        )


