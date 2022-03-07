import discord, asyncio, os
from discord.ext import commands

from datetime import datetime
import requests as rq
import random

from menuCrawler import *


game = discord.Game("Primary Bot")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game, intents=intents)

token_path = os.path.dirname(os.path.abspath(__file__))+'/token.txt'
t = open(token_path, "r", encoding="utf-8")
token = t.read()

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.command(aliases=['도움', '도움말', '사용법'])
async def Help(ctx):
    embed = discord.Embed(title="Jeeves", description="Here I stand for you!")
    embed.add_field(name="1. 인사", value="!hello", inline=False)
    embed.add_field(name="2. 업다운", value="!updown", inline=False)
    embed.add_field(name="3. 학식", value="!dodam", inline=False)
    embed.add_field(name="4. 고양이", value="!cat", inline=False)

    await ctx.send(embed=embed)

@bot.command(aliases=['인사', '안녕', 'hi', '안녕하세요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!')

@bot.command(aliases=['도담', '도담식당', '학식', '밥'])
async def dodam(ctx):
    todayDate = datetime.today().strftime("%Y-%m-%d")
    embed = discord.Embed(title=f"🗓 {todayDate}", description="학식 정보를 불러옵니다. 잠시만 기다려주세요", color=0xd5d5d5)

    await ctx.send(embed=embed)
    menu = mainFunc(1)
    embed = discord.Embed(title=f"도담식당", description=menu, color=0xd5d5d5)

    await ctx.send(embed=embed)
  
@bot.command(aliases=['업다운', '업다운게임', 'updown'])
async def Updown(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    embed = discord.Embed(title="업다운 게임을 시작합니다", description="1~100 사이 숫자를 입력해주세요.", color=0xd5d5d5)
    await ctx.send(embed=embed)
    randnum = random.randrange(1,100)
    print(randnum)
    hp = 4
    while True:
        msg = await bot.wait_for("message", check=check)
        answer = int(msg.content)
        if hp <= 0:
            break
        if answer < randnum:
            embed = discord.Embed(title="UP!", description=f"{answer} 보다 더 큰 수를 입력해주세요! ({hp}/5)", color=0xd5d5d5)
            await ctx.send(embed=embed)
        elif answer > randnum:
            embed = discord.Embed(title="DOWN!", description=f"{answer} 보다 더 작은 수를 입력해주세요! ({hp}/5)", color=0xd5d5d5)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="CORRECT", description="정답입니다!", color=0xFFFF99)
            await ctx.send(embed=embed)
            return
        hp -= 1
    embed = discord.Embed(title="GAME OVER", description=f"정답은 {randnum} 입니다.", color=0xff0000)
    await ctx.send(embed=embed)
        

@bot.command(aliases=['고양이', '냥이', '고먐미', '고영희', '야옹이'])
async def cat(ctx):
    embed = discord.Embed(title="🐱", description="랜덤 냥이 사진 가져오기")
    url = "https://source.unsplash.com/random/?cat"
    result = rq.get(url)
    print(result.url)
    embed.set_image(url=result.url)
    await ctx.send(embed=embed)

bot.run(token)