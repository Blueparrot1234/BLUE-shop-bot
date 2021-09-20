# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, pytz, datetime

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("관리"))

@client.event
async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    if message.content.startswith ("!공지"):
        await message.delete()
        if message.author.guild_permissions.administrator:
            notice = message.content[4:]
            channel = client.get_channel(875664353477681172)
            embed = discord.Embed(title="**BLUE shop 공지*", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n\n\n{}\n\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000ff)
            embed.set_footer(text="Bot Made by. 파란앵무새#7973 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/889430099575857182/889430170979680256/2.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/889430099575857182/889431014655557672/Blue_shop.png")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        else:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("관리"))

@client.event
async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    if message.content == "특정입력":
        ch = client.get_channel(875666490458775573)
        await ch.send ("{} | {}, User, Hello".format(ch.author, ch.author.mention))

    if message.content == "!프로필 GIF": # 메세지 감지
        embed = discord.Embed(title="GIF 프로필", description="**PRICE**",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name=":credit_card: : 계좌이체", value="계좌이체는 디엠으로 알려드립니다", inline=False)
        embed.add_field(name=":dollar: : 문화상품권", value="문화상품권은 디엠으로 주시면 됩니다", inline=False)

        embed.add_field(name="**[ :credit_card: : 0.3 ]  [ :dollar: : 0.4 ]**", value="환불 불가", inline=False)

        embed.set_footer(text="Bot Made by. 파란앵무새#7973", icon_url="https://cdn.discordapp.com/attachments/889430099575857182/889430170979680256/2.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/889430099575857182/889431014655557672/Blue_shop.png")
        await message.channel.send (embed=embed)

    if message.content == "!프로필 PNG": # 메세지 감지
        embed = discord.Embed(title="PNG 프로필", description="**PRICE**",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name=":credit_card: : 계좌이체", value="계좌이체는 디엠으로 알려드립니다", inline=False)
        embed.add_field(name=":dollar: : 문화상품권", value="문화상품권은 디엠으로 주시면 됩니다", inline=False)

        embed.add_field(name="**[ :credit_card: : 0.3 ]  [ :dollar: : 0.4 ]**", value="환불 불가", inline=False)

        embed.set_footer(text="Bot Made by. 파란앵무새#7973", icon_url="https://cdn.discordapp.com/attachments/889430099575857182/889430170979680256/2.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/889430099575857182/889431014655557672/Blue_shop.png")
        await message.channel.send (embed=embed)

    if message.content == "!프로필 커스텀": # 메세지 감지
        embed = discord.Embed(title="CUSTOM 프로필", description="**PRICE**",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name=":credit_card: : 계좌이체", value="계좌이체는 디엠으로 알려드립니다", inline=False)
        embed.add_field(name=":dollar: : 문화상품권", value="문화상품권은 디엠으로 주시면 됩니다", inline=False)

        embed.add_field(name="**[ :credit_card: : 0.5 ]  [ :dollar: : 0.6 ]**", value="환불 불가", inline=False)

        embed.set_footer(text="Bot Made by. 파란앵무새#7973", icon_url="https://cdn.discordapp.com/attachments/889430099575857182/889430170979680256/2.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/889430099575857182/889431014655557672/Blue_shop.png")
        await message.channel.send (embed=embed)
    
    if message.content == "!프로필 커스텀 GIF": # 메세지 감지
        embed = discord.Embed(title="커스텀 GIF 프로필", description="**PRICE**",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name=":credit_card: : 계좌이체", value="계좌이체는 디엠으로 알려드립니다", inline=False)
        embed.add_field(name=":dollar: : 문화상품권", value="문화상품권은 디엠으로 주시면 됩니다", inline=False)

        embed.add_field(name="**[ :credit_card: : 0.5 ]  [ :dollar: : 0.6 ]**", value="환불 불가", inline=False)

        embed.set_footer(text="Bot Made by. 파란앵무새#7973", icon_url="https://cdn.discordapp.com/attachments/889430099575857182/889430170979680256/2.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/889430099575857182/889431014655557672/Blue_shop.png")
        await message.channel.send (embed=embed)

        

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODg2NTgxNTI0NDEyMTMzNDY2.YT3rYw.lJXye_Y8fUjP3CdVUIevkFe8J2s')