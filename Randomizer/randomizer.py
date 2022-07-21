import random

from redbot.core import commands


class Rater(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random(self, ctx, a: int, b: int):
        """Send a random integer N such that a <= N <= b."""
        await ctx.send(random.randint(a, b))
