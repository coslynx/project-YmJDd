import discord
from discord.ext import commands

class RoleAssignment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Assign role based on behavior
        # Add your role assignment logic here
        pass

def setup(bot):
    bot.add_cog(RoleAssignment(bot))