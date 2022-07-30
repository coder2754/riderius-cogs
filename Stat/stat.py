import time

from redbot.core import commands
import discord


class Stat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        """Get Discord user avatar"""
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        await ctx.send(userAvatar)

    @commands.guild_only()
    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
        """Get Discord user statistic"""
        if not member:
            member = ctx.message.author
        if member.nick:
            stat = discord.Embed(title=f"{member} aka {member.nick} stat")
        else:
            stat = discord.Embed(title=f"{member} stat")
        stat.set_thumbnail(url=member.avatar_url)

        stat.add_field(name="User id:", value=member.id)
        created_at = time.strptime(str(member.created_at), '%Y-%m-%d %H:%M:%S.%f')
        created_at = time.strftime('%a, %d %b %Y %H:%M:%S +0000', created_at)
        stat.add_field(name="Account created:", value=str(created_at))
        joined_at = time.strptime(str(member.joined_at), '%Y-%m-%d %H:%M:%S.%f')
        joined_at = time.strftime('%a, %d %b %Y %H:%M:%S +0000', joined_at)
        stat.add_field(name="Joined at:", value=joined_at)
        await ctx.send(embed=stat)
