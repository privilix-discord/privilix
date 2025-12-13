import discord
from discord.ext import commands
import random
import aiohttp
from app.core.constants.colors import BLUE


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball", help="Ask a question to the magic ball")
    async def _8ball(self, ctx: commands.context, *, question: str):
        answers = [
            "No",
            "Likely not",
            "Yes",
            "Ask your question again",
            "Very likely",
            "Impossible",
            "Without a doubt",
            "It's No",
            "Yes definitely",
        ]
        answer = random.randint(0, len(answers) - 1)

        ball = discord.Embed(color=0xA865B5, title="8ball 🔮")
        ball.add_field(name="Question", value=question)
        ball.add_field(name="Answer", value=answers[answer])

        await ctx.reply(embed=ball)

    @commands.command(name="fact", help="Get a random useless fact.")
    @commands.guild_only()
    async def _fact(self, ctx: commands.Context):
        url = "https://uselessfacts.jsph.pl/random.json"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                data = await res.json()

        embed = discord.Embed(color=BLUE, title="Random Fact", description=data["text"])

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Fun(bot))
