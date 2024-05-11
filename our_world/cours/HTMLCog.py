import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

class HTMLCog(commands.Cog, name="HTMLCog"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.role1_id = 1232422284921147535
        self.role2_id = 1232423486501425213
        self.role3_id = 1232423509435875550
        self.role4_id = 1232423526917734462
        self.role5_id = 1232423550623809608
        self.role6_id = 1232423568835350690
        self.role2 = None
        self.role3 = None
        self.role4 = None
        self.role5 = None
        self.role6 = None
    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(1196194673623044286)
        if guild:
            self.role = guild.get_role(id=self.role1_id)
            self.role2 = guild.get_role(id=self.role2_id)
            self.role3 = guild.get_role(id=self.role3_id)
            self.role4 = guild.get_role(id=self.role4_id)
            self.role5 = guild.get_role(id=self.role5_id)
            self.role6 = guild.get_role(id=self.role6_id)
        else:
            print("Guild not found!")
    
    @commands.hybrid_command(
        name="cours_html1",
        description="This is a testing command that does nothing.",
    )
    @commands.is_owner()
    async def cours_html1(self, context: Context) -> None:
        """
        This is a testing command that does nothing.
        :param context: The application command context.
        """    
        
    @commands.hybrid_command(
        name="cours_html2",
        description="This is a testing command that does nothing.",
    )
    @commands.is_owner()
    async def cours_html2(self, context: Context) -> None:
        """
        This is a testing command that does nothing.
        :param context: The application command context.
        """    
        
    @commands.hybrid_command(
        name="cours_html3",
        description="This is a testing command that does nothing.",
    )
    @commands.is_owner()
    async def cours_html3(self, context: Context) -> None:
        """
        This is a testing command that does nothing.
        :param context: The application command context.
        """    
        
    @commands.hybrid_command(
        name="cours_html4",
        description="This is a testing command that does nothing.",
    )
    @commands.is_owner()
    async def cours_html4(self, context: Context) -> None:
        """
        This is a testing command that does nothing.
        :param context: The application command context.
        """    
        
    @commands.hybrid_command(
        name="cours_html5",
        description="This is a testing command that does nothing.",
    )
    @commands.is_owner()
    async def cours_html5(self, context: Context) -> None:
        """
        This is a testing command that does nothing.
        :param context: The application command context.
        """    
        
    @commands.hybrid_command(
        name="cours_html6",
        description="This is a testing command that does nothing.",
    )
    @commands.is_owner()
    async def cours_html6(self, context: Context) -> None:
        """
        This is a testing command that does nothing.
        :param context: The application command context.
        """    

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(HTMLCog(bot))