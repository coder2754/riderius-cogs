from .rater import Rater


def setup(bot):
    bot.add_cog(Rater(bot))
