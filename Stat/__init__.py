from .stat import Stat


def setup(bot):
    bot.add_cog(Stat(bot))
