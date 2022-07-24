import asyncio
from typing import Optional

import discord
from redbot.core import commands


class Rater(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def rate(self, ctx, message_id: Optional[int] = None):
        """Create a rating for a message"""
        channel = ctx.channel

        if message_id:
            try:
                message = await channel.fetch_message(message_id)
            except discord.NotFound:
                return await ctx.send("Message not found.")
        elif ref := ctx.message.reference:
            message = await channel.fetch_message(ref.message_id)
        else:
            return await ctx.send("Message not found.")

        await message.add_reaction("\u2795")
        await asyncio.sleep(0.5)
        await message.add_reaction("\u2796")
