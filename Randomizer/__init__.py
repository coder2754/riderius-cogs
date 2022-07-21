from .randomizer import Randomizer


def setup(bot):
    bot.add_cog(Randomizer(bot))
