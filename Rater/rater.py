import asyncio

from redbot.core import commands


class Rater(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start_rating(self, ctx, message_id: int):
        message = await ctx.fetch_message(message_id)
        await message.add_reaction("\u2795")
        await asyncio.sleep(0.5)
        await message.add_reaction("\u2796")
