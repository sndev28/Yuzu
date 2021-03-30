

                                             ###############################################################################
                                             #                                                                             #
                                             #                                                                             #
                                             #                                                                             #
                                             #                                  YUZU                                       #
                                             #                                                                             #
                                             #                        VERSION CODE : 3.16.89                               #
                                             #                                                                             #
                                             #                                                                             #
                                             #                                                                             #
                                             #                                                                             #
                                             ###############################################################################




import discord
from discord.ext import commands
import os
import asyncio
import io
import time
import math
import re
from urllib.request import Request, urlopen
import json
import requests
import importlib
import file
from bs4 import BeautifulSoup


client = commands.Bot(command_prefix = os.getenv('prefix'), help_command = None)




########################################################################### ASSETS ########################################################################




emojinumbers = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']




########################################################################### END OF ASSETS #################################################################





########################################################################### CLASSES ########################################################################



class colordetail :
    def __init__(self, value, name, command : discord.Color):
        self.value = value
        self.name = name
        self.command = command

class xoplayer :
    def __init__(self, details : discord.Member, mark):
        self.details = details
        self.mark = mark

#------------ data file initializations

jsonbinapitoken = os.getenv('jsonbinapitoken')
jsonbinid = os.getenv('jsonbinid')


getheader = { 'X-Master-Key':jsonbinapitoken }
putheader = { 'X-Master-Key':jsonbinapitoken, 'Content-Type':'application/json' }


#------------ end of data file initilizations





######################################################################## END OF CLASSES ###########################################################################









########################################################################## FUNCTIONS #####################################################################################



async def stringgen(day, hour, min, sec):
    formatstring = " "

    numbers = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

    for char in str(day):
        formatstring = formatstring + f":{numbers[int(char)]}:"

    if(hour == 1):
        formatstring = formatstring + " :regional_indicator_d: :regional_indicator_a: :regional_indicator_y:        "

    else :
        formatstring = formatstring + " :regional_indicator_d: :regional_indicator_a: :regional_indicator_y: :regional_indicator_s:        "


    for char in str(hour):
        formatstring = formatstring + f":{numbers[int(char)]}:"

    if(hour == 1):
        formatstring = formatstring + " :regional_indicator_h: :regional_indicator_r:        "

    else :
        formatstring = formatstring + " :regional_indicator_h: :regional_indicator_r: :regional_indicator_s:        "


    for char in str(min):
        formatstring = formatstring + f":{numbers[int(char)]}:"

    if(min == 1):
        formatstring = formatstring + " :regional_indicator_m: :regional_indicator_i: :regional_indicator_n:        "

    else :
        formatstring = formatstring + " :regional_indicator_m: :regional_indicator_i: :regional_indicator_n: :regional_indicator_s:        "


    for char in str(sec):
        formatstring = formatstring + f":{numbers[int(char)]}:"

    if(sec == 1):
        formatstring = formatstring + " :regional_indicator_s: :regional_indicator_e: :regional_indicator_c:"

    else :
        formatstring = formatstring + " :regional_indicator_s: :regional_indicator_e: :regional_indicator_c: :regional_indicator_s:"


    return formatstring



async def countdownmanager(time_data):


    while(True):

        deadline = int(time_data['deadline'])


        remaining = deadline - time.time()

        initmessage = await client.get_channel(int(time_data['channel_id'])).fetch_message(int(time_data['countdown_id']))
        finalmessage = await client.get_channel(int(time_data['channel_id'])).fetch_message(int(time_data['message_id']))

        messageenddetails = time_data['message']


        if remaining <= 0 :

            await initmessage.edit(content = ":zero: :regional_indicator_d: :regional_indicator_a: :regional_indicator_y: :regional_indicator_s:        :zero: :regional_indicator_h: :regional_indicator_r: :regional_indicator_s:        :zero: :regional_indicator_m: :regional_indicator_i: :regional_indicator_n: :regional_indicator_s:        :zero: :regional_indicator_s: :regional_indicator_e: :regional_indicator_c: :regional_indicator_s:")
            await finalmessage.edit(content = f" \n ` {messageenddetails[0]} ` {messageenddetails[1]}")
            break

        else:

            remaining = math.trunc(deadline - time.time())
            totalminutes = math.trunc(remaining/60)
            totalhours = math.trunc(totalminutes/60)
            minutes = totalminutes % 60
            seconds = remaining % 60
            days = math.trunc(totalhours/24)
            hours = totalhours % 24

            timestring = await stringgen(days, hours, minutes, seconds)

            await initmessage.edit(content = timestring)

        asyncio.sleep(4)






async def run(ctx, client):
    try :
        importlib.reload(file)
        await file.script(ctx, client)

    except Exception as err:
        await ctx.send('```Error :\n' + str(err) + '```')








##########################################################################  COMMANDS #######################################################################################







#------------------------------------------------------------------------ Help menu----------------------------------------------------------------------------

@client.group(invoke_without_command = True)
async def help(ctx):
    help = discord.Embed(title = "This is the help window.", description = "Send e!help <command> to get more information on a specific command.", color = discord.Color.red() )
    help.add_field(name = "help", value = "Opens this help window.", inline = False)
    help.add_field(name = "test", value = "Random crap test code.",  inline = False)
    help.add_field(name = "emojiret", value = "Returns a message with type and number of each reactions to a specific message.", inline = False)
    help.add_field(name = "announce", value = "Lets make an embedded announcement.", inline = False)
    help.add_field(name = "rolesret", value = "Lists all the roles in the server", inline = False)
    help.add_field(name = "xo", value = "Play a game of xo or tic tac toe.", inline = False)
    help.add_field(name = "countdown", value = "Creates a countdown.", inline = False)
    help.add_field(name = "creepy", value = "Creepy stories", inline = False)
    help.add_field(name = "clear", value = "Deletes messages.", inline = False)

    await ctx.send(embed = help)

@help.command()
async def test(ctx):
    help_test = discord.Embed(title = "test", description = "This is a bunch of random test code. All waste. Do anything.", color = discord.Color.red())
    await ctx.send(embed = help_test)

@help.command()
async def emojiret(ctx):
    help_emojiret = discord.Embed(title = "emojiret", description = "This command returns a message with the number and type of reactions a message has. The message at question is the one being replied to", color = discord.Color.red())
    await ctx.send(embed = help_emojiret)

@help.command()
async def announce(ctx):
    help_announce = discord.Embed(title = "announce", description = "This command opens the announcement wizard which lets you make announcements and post it in formatted form as an embedded messsage.", color = discord.Color.red())
    await ctx.send(embed = help_announce)

@help.command()
async def clear(ctx):
    help_clear = discord.Embed(title = "clear", description = "Deletes messages. Default : 10 messages are deleted. To delete custom number of messages use e!clear <number>", color = discord.Color.red())
    await ctx.send(embed = help_clear)

@help.command()
async def rolesret(ctx):
    help_rolesret = discord.Embed(title = "rolesret", description = "This command returns all the roles in the discord server.", color = discord.Color.red())
    await ctx.send(embed = help_rolesret)

@help.command()
async def xo(ctx):
    help_xo = discord.Embed(title = "xo", description = "Play a game of tic tac toe or XO with another player. For usage use the command \"e!xo @person_to_play_with\"", color = discord.Color.red())
    await ctx.send(embed = help_xo)

@help.command()
async def countdown(ctx):
    help_countdown = discord.Embed(title = "countdown", description = "Creates a countdown to a specified time. You can setup up the message to be shown at the end of the countdown as well.", color = discord.Color.red())
    await ctx.send(embed = help_countdown)

@help.command()
async def creepy(ctx):
    help_creepy = discord.Embed(title = "creepy", description = "Gives you a random creepy story, fresh from CreepyPasta", color = discord.Color.red())
    await ctx.send(embed = help_creepy)


#-----------------------------------------------------------------------end of Help menu----------------------------------------------------------------------------




#------------------------------------------------------------------------ clear----------------------------------------------------------------------------

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, count=(10+1)):
    await ctx.channel.purge(limit = count+1)

#-----------------------------------------------------------------------end of clear----------------------------------------------------------------------------




#------------------------------------------------------------------------ minitest----------------------------------------------------------------------------

@client.command()
async def mini(ctx):

    damn = await ctx.send(":two: :three: :regional_indicator_f:")
    await damn.add_reaction('▶️')

#-----------------------------------------------------------------------end of minitest----------------------------------------------------------------------------




#------------------------------------------------------------------------ rolesret----------------------------------------------------------------------------

@client.command()
async def rolesret(ctx):

    rolestring = ""

    givenroles = ctx.guild.roles
    for mentionable in givenroles :
        rolestring = rolestring + str(mentionable.name) + "\n"

    rolestringfinal = rolestring.replace('@', '')


    roleprompt = discord.Embed(title = "Roles in this server", description = str(rolestringfinal), color = discord.Color.red())
    await ctx.send(embed = roleprompt)

#-----------------------------------------------------------------------end of rolesret----------------------------------------------------------------------------




#------------------------------------------------------------------------ test----------------------------------------------------------------------------

@client.command()
async def test(ctx):

    embed = discord.Embed(title = "This is a  test embed, Love cats", url = "https://www.instagram.com/p/CLO4sfIpk0z/?utm_source=ig_web_copy_link", description = "Cats are the best in the world. Go kill yourself if you dont like cats.", color = discord.Color.red())

    embed.set_author(name=ctx.author.display_name, url = "https://www.instagram.com/shamil_niyas/", icon_url=ctx.author.avatar_url)

    embed.set_thumbnail(url="https://static01.nyt.com/images/2020/04/22/science/22VIRUS-PETCATS1/22VIRUS-PETCATS1-mediumSquareAt3X.jpg")


    embed.add_field(name = "I hate rats", value="BWaaah all rats can die for all I care..!!")


    embed.set_footer(text="#lovecats #cats #catslove #catsbest", icon_url="https://static01.nyt.com/images/2020/04/22/science/22VIRUS-PETCATS1/22VIRUS-PETCATS1-mediumSquareAt3X.jpg")
    await ctx.send(embed=embed)

#-----------------------------------------------------------------------end of test----------------------------------------------------------------------------




#------------------------------------------------------------------------ emojiret----------------------------------------------------------------------------

@client.command()
async def emojiret(ctx):
    messageid = ctx.message.reference.message_id
    message = await ctx.fetch_message(messageid)
    emolist = list(message.reactions)

    result = discord.Embed(title = "This is the query asked", description = "given below is the details.")

    for answer in emolist:
        result.add_field(name = answer.emoji, inline = False, value = answer.count)

    await ctx.send(embed=result)

#-----------------------------------------------------------------------end of emojiret----------------------------------------------------------------------------




#------------------------------------------------------------------------ announce----------------------------------------------------------------------------

@client.command()
async def announce(ctx):

    authorflag = 1
    thumbflag = 0
    fieldflag = 0


    colorlist = []
    colorlist.append(colordetail(value = 1, name = "blue", command = discord.Color.blue()))
    colorlist.append(colordetail(value = 2, name = "blurple", command = discord.Color.blurple()))
    colorlist.append(colordetail(value = 3, name = "dark blue", command = discord.Color.dark_blue()))
    colorlist.append(colordetail(value = 4, name = "dark gold", command = discord.Color.dark_gold()))
    colorlist.append(colordetail(value = 5, name = "dark gray", command = discord.Color.dark_gray()))
    colorlist.append(colordetail(value = 6, name = "dark green", command = discord.Color.dark_green()))
    colorlist.append(colordetail(value = 7, name = "dark grey", command = discord.Color.dark_grey()))
    colorlist.append(colordetail(value = 8, name = "dark magenta", command = discord.Color.dark_magenta()))
    colorlist.append(colordetail(value = 9, name = "dark orange", command = discord.Color.dark_orange()))
    colorlist.append(colordetail(value = 10, name = "dark purple", command = discord.Color.dark_purple()))
    colorlist.append(colordetail(value = 11, name = "dark red", command = discord.Color.dark_red()))
    colorlist.append(colordetail(value = 12, name = "dark teal", command = discord.Color.dark_teal()))
    colorlist.append(colordetail(value = 14, name = "darker grey", command = discord.Color.darker_grey()))
    colorlist.append(colordetail(value = 13, name = "darker gray", command = discord.Color.darker_gray()))
    colorlist.append(colordetail(value = 16, name = "green", command = discord.Color.green()))
    colorlist.append(colordetail(value = 15, name = "gold", command = discord.Color.gold()))
    colorlist.append(colordetail(value = 17, name = "greyple", command = discord.Color.greyple()))
    colorlist.append(colordetail(value = 18, name = "light gray", command = discord.Color.light_gray()))
    colorlist.append(colordetail(value = 19, name = "light grey", command = discord.Color.light_grey()))
    colorlist.append(colordetail(value = 21, name = "lighter grey", command = discord.Color.lighter_grey()))
    colorlist.append(colordetail(value = 20, name = "lighter gray", command = discord.Color.lighter_gray()))
    colorlist.append(colordetail(value = 22, name = "magenta", command = discord.Color.magenta()))
    colorlist.append(colordetail(value = 23, name = "orange", command = discord.Color.orange()))
    colorlist.append(colordetail(value = 24, name = "purple", command = discord.Color.purple()))
    colorlist.append(colordetail(value = 25, name = "red", command = discord.Color.red()))
    colorlist.append(colordetail(value = 26, name = "teal", command = discord.Color.teal()))
    colorlist.append(colordetail(value = 27, name = "random", command = discord.Color.random()))



    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    authorprompt = discord.Embed(title = "Do you want to show author in your announcement?", description = "Like Embedy is the author for this message. Please answer y/n. Any other response will be taken as a yes.", color = discord.Color.red())
    authorprompt.set_author(name = "Embedy", icon_url = "https://drive.google.com/uc?export=view&id=1VzkSsM7ALQG9zta8IOX0b-mrGpdHZPhA")
    await ctx.send(embed = authorprompt)

    try :
        authorres = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 3)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return


    if(authorres.content == 'n'):
        authorflag = 0

    thumbprompt = discord.Embed(title = "Do you want to show thumbnail in your announcement?", description = "Like the thumbnail on the upper left corner of this message. Please answer y/n. Any other response will be taken as a no.", color = discord.Color.red())
    thumbprompt.set_thumbnail(url = "https://c-sf.smule.com/rs-s49/arr/71/9f/be656761-ab54-4064-8a92-b410d73118fe_1024.jpg")

    await ctx.send(embed = thumbprompt)

    try :
        thumbres = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return


    if(thumbres.content == 'y'):
        await ctx.send("Enter the link for the thumbnail pic")
        thumburl = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)
        thumbflag = 1

    titleprompt = discord.Embed(title = "What is the title of your announcement?",description = "It will show up like the above question in the final announcement", color=discord.Color.red() )
    await ctx.send(embed = titleprompt)

    try :
        titleres = await client.wait_for("message", check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return

    descprompt = discord.Embed(title = "What main descrption do you want to add?", description = "You can add fields (new title and description in the same message after this). Descriptions look like this sentence you just read.", color=discord.Color.red())
    await ctx.send(embed = descprompt)

    try :
        descres = await client.wait_for("message", check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return


    colorprompt = discord.Embed(title = "Which color do you want your embed to be?", description = "<---- This color is what I mean. Enter the index of the color.", color = discord.Color.red())
    for obj in colorlist:
        colorstring = str(obj.value) + " " + str(obj.name)
        colorprompt.add_field(name = colorstring, value = '\u200b', inline = False)

    await ctx.send(embed = colorprompt)

    try :
        colorres = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return

    finalcolorobj = colordetail(name = "dummy", value = 0, command = discord.Color.random())

    for obj in colorlist:
        if obj.value == int(colorres.content):
            finalcolorobj = obj


    announcement = discord.Embed(title = str(titleres.content), description = str(descres.content), color = finalcolorobj.command)

    if (authorflag == 1):
        announcement.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)

    if (thumbflag == 1):
        announcement.set_thumbnail(url = thumburl.content)

    fieldprompt = discord.Embed(title = "Do you want to add additional field?", description = "Additional fields look like the ones below. Please enter y/n. Any other response will be taken as a no.", color = discord.Color.red())
    fieldprompt.add_field( name = "This is an additional field", value = "You can add info here as well.")

    await ctx.send(embed = fieldprompt)

    try :
        fieldres = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return



    if (fieldres.content == 'y'):
        fieldflag = 1
        fieldtitle = discord.Embed(title = "Enter the title of the field",color = discord.Color.red() )
        fielddetail = discord.Embed(title = "Enter the details of the field",color = discord.Color.red() )

    while (fieldflag == 1) :
        fieldflag = 0
        await ctx.send(embed = fieldtitle)

        try :
            temptitle = await client.wait_for('message', check = check, timeout = 300.0)
            await ctx.channel.purge(limit = 2)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")
            return


        await ctx.send(embed = fielddetail)

        try :
            tempvalue = await client.wait_for('message', check = check, timeout = 300.0)
            await ctx.channel.purge(limit = 2)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")
            return


        announcement.add_field( name = str(temptitle.content), value = str(tempvalue.content))

        await ctx.send(embed = fieldprompt)

        try :
            fieldres = await client.wait_for('message', check = check, timeout = 300.0)
            await ctx.channel.purge(limit = 2)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")
            return


        if (fieldres.content == 'y'):
            fieldflag = 1

    rolestring = "Roles : \n"

    tomention = ctx.guild.roles
    for mentionable in tomention :
        rolestring = rolestring + str(mentionable.name) + "\n"


    footerdescription = "Mention the roles to be mentioned in your message. \n" + rolestring

    footerdescriptionfinal = footerdescription.replace('@', '')

    footerprompt = discord.Embed(title = "Who all do you want to address with this announcement?", description = str(footerdescriptionfinal), color = discord.Color.red())
    await ctx.send(embed = footerprompt)

    try :
        roleres =  await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return


    announcement.set_footer(text = str(roleres.content))


    await ctx.send(embed = announcement)



#-----------------------------------------------------------------------end of announcement---------------------------------------------------------------------------





#------------------------------------------------------------------------ XO Game----------------------------------------------------------------------------



@client.command()
async def xo(ctx, player : discord.Member) :
    p1 = xoplayer(ctx.author, ':x:')
    p2 = xoplayer(player, ':o:')


    board = [['᲼᲼','᲼᲼','᲼᲼'],['᲼᲼','᲼᲼','᲼᲼'],['᲼᲼','᲼᲼','᲼᲼']]

    win = 'n'

    currentplayer = p2

    def iswin(board) :

        count = 0
        flag = 'n'

        for i in range(3):
            for j in range(3):
                if board[i][j] == '᲼᲼':
                    count += 1

        if count > 5:
            return 'n'

        for i in range(3):
            if ((board[i][0] == board[i][1]) and (board[i][0] == board[i][2])):
                return board[i][0]


        for i in range(3):
            if ((board[0][i] == board[1][i]) and (board[0][i] == board[2][i])):
                return board[0][i]

        if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
            return board[0][0]

        if(board[0][2] == board[1][1] and board[0][2] == board[2][0]):
            return board[0][2]

        if count == 0:
            return 'd'

        return 'n'




    await ctx.channel.purge(limit = 1)

    final = ""

    while win == 'n':

        if currentplayer == p1:
            currentplayer = p2
        else :
            currentplayer = p1

        currentstate = f"᲼{board[0][0]}᲼┃᲼{board[0][1]}᲼┃᲼{board[0][2]}\n― ― + ― ― + ― ― \n᲼{board[1][0]}᲼┃᲼{board[1][1]}᲼┃᲼{board[1][2]}\n― ― + ― ― + ― ―\n᲼{board[2][0]}᲼┃᲼{board[2][1]}᲼┃᲼{board[2][2]}\n"
        xoprompt = discord.Embed(title = "Where do you want to mark?", description = currentstate + "\n" + currentplayer.details.mention + "play your turn. Enter the row and column numbers seperated by space.", color = discord.Color.red())

        await ctx.send(embed = xoprompt)

        try :
            xores = await client.wait_for('message', check = lambda message : (message.author.id == currentplayer.details.id and message.channel == ctx.channel), timeout = 60.0)
            await ctx.channel.purge(limit = 2)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")
            return


        mark = xores.content.split(' ')

        board[int(mark[0]) - 1][int(mark[1]) - 1] = currentplayer.mark

        win = iswin(board)

        final = f"᲼{board[0][0]}᲼┃᲼{board[0][1]}᲼┃᲼{board[0][2]}\n― ― + ― ― + ― ― \n᲼{board[1][0]}᲼┃᲼{board[1][1]}᲼┃᲼{board[1][2]}\n― ― + ― ― + ― ―\n᲼{board[2][0]}᲼┃᲼{board[2][1]}᲼┃᲼{board[2][2]}\n"

    if win == 'd':
        result = discord.Embed(title = str(f"The match is a draw!!" ),description = final + f"\n\nGG {p1.details.mention} and {p2.details.mention}", color = discord.Color.green())

    else :
        result = discord.Embed(title = str("The game is over!! "),description = final + "\nThe winner is " + currentplayer.details.mention + " !!", color = discord.Color.green())

    await ctx.send(embed = result)



#-----------------------------------------------------------------------end of XO game---------------------------------------------------------------------------





#------------------------------------------------------------------------ countdown-----------------------------------------------------------------------

@client.command()
async def countdown(ctx):

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel





    timeprompt = discord.Embed(title = "Countdown wizard", description = "Enter the time to countdown as per the given example. \n 20 Nov 2021 @ 11:23:59", color = discord.Color.red())

    await ctx.send(embed = timeprompt)

    try :
        timeres =  await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 3)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return

    messageprompt = discord.Embed(title = "Countdown wizard", description = "What message do you want me to show with the countdown?", color = discord.Color.red())

    await ctx.send(embed = messageprompt)

    try:
        messageres = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return

    messageendprompt = discord.Embed(title = "Countdown wizard", description = "What message do you want me to send at the end of the countdown? Anyone to be mentioned can be added to this message as well at the end of the message seperated by a |", color = discord.Color.red())
    messageendprompt.add_field(name = "Example", value = "Hi everyone, this is the end of the countdown | @mentions", inline = False)

    await ctx.send(embed = messageendprompt)

    try:
        messageendres = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return


    messageenddetails = messageendres.content.split('|')

    deadlinedetails = time.strptime(timeres.content,'%d %b %Y @ %H:%M:%S' )

    deadline = math.trunc(time.mktime(deadlinedetails))

    #initialization message

    remaining = math.trunc(deadline - time.time())
    totalminutes = math.trunc(remaining/60)
    totalhours = math.trunc(totalminutes/60)
    minutes = totalminutes % 60
    seconds = remaining % 60
    days = math.trunc(totalhours/24)
    hours = totalhours % 24

    timestring = await stringgen(days, hours, minutes, seconds)

    await ctx.send(f" ` {messageres.content} ` ")
    initmessage = await ctx.send(timestring)
    finalmessage = await ctx.send("*")

    time_data = {}

    time_data['channel_id'] = str(ctx.channel.id)
    time_data['countdown_id'] = str(initmessage.id)
    time_data['message_id'] = str(finalmessage.id)
    time_data['deadline'] = str(deadline)
    time_data['message'] = messageenddetails

    edit_data = json.loads(requests.get(f"https://api.jsonbin.io/v3/b/{jsonbinid}/latest", headers = getheader).text)["record"]

    edit_data['countdown'].append(time_data)

    requests.put(f"https://api.jsonbin.io/v3/b/{jsonbinid}", json = edit_data, headers = putheader)

    await countdownmanager(time_data)







#----------------countdown restart


async def countdownrestart():


    countdownlist = json.loads(requests.get(f"https://api.jsonbin.io/v3/b/{jsonbinid}/latest", headers = getheader).text)["record"]


    for time_data in countdownlist['countdown']:
        asyncio.create_task(countdownmanager(time_data))










#-------------end of coutndown restart






#-----------------------------------------------------------------------end of countdown---------------------------------------------------------------------------




#------------------------------------------------------------------------ creepy----------------------------------------------------------------------------

@client.command()
async def creepy(ctx):

    ncrtochar = {'&#8211;':'–', '&#8212;':'—', '&#8216;':'‘', '&#8217;':'’', '&#8218;':'‚', '&#8220;':'“', '&#8221;':'”', '&#8222;':'„', '&#8224;':'†', '&#8225;':'‡', '&#8226;':'•', '&#8230;':'…', '&#8240;':'‰', '&#8364;':'€', '&#8482;':'™'  }

    url = Request("https://www.creepypasta.com/random/", headers={'User-Agent': 'Mozilla/5.0'})

    page_object = urlopen(url)

    page = page_object.read().decode("utf8")


    pagetitle = re.findall("<title>.*?</title>", page)[0][7:-22]



    cut = re.findall("<p>.*?</p>", page)

    finalindex = len(cut)

    for i in range(len(cut)):
        if cut[i][3:9].lower() == "credit":
            finalindex = i
            break

    unedittedstory = cut[0:finalindex]

    story = " "

    for string in unedittedstory:
        story = story + string[3:-4] + "\n"


    formattedstory = re.sub("<.*?>", "\n", story)

    while(re.search("&#.*?;", formattedstory) != None):
        instance = re.search("&#.*?;",formattedstory).start()

        character = formattedstory[instance:instance+7]
        formattedstory = formattedstory[0:instance] + ncrtochar[character] + formattedstory[instance+7:]


    noofchars = len(formattedstory)

    noofembeds = int(noofchars / 2000) + 1

    if(noofchars % 2000 == 0):
        noofembeds -= 1




    if noofchars <= 2000 :

        storyembed = discord.Embed(title = pagetitle, description = formattedstory, color = discord.Color.green())
        storyembed.set_footer(text = f"Taken from CreepyPasta. Story name : {pagetitle}")

        storymessage = await ctx.send(embed = storyembed)

    else :
        pointer = 2000
        previous = 0
        splitstory = []

        while(pointer < noofchars):


            while(formattedstory[pointer] != '.'):
                pointer -= 1

            splitstory.append(formattedstory[previous+1:pointer+1])

            previous = pointer
            pointer += 2000

        splitstory.append(formattedstory[previous+1:])


        storyembed = discord.Embed(title = pagetitle, description = splitstory[0], color = discord.Color.green())

        storyembed.set_footer(text = f"Page {1}/{noofembeds}. Taken from CreepyPasta. Story name : {pagetitle}")

        storymessage = await ctx.send(embed = storyembed)

        await storymessage.add_reaction('❌')
        await storymessage.add_reaction('▶️')

        tosave = {}
        tosave['message_id'] = str(storymessage.id)
        tosave['currentpage'] = 1
        tosave['lastpage'] = noofembeds
        tosave['title'] = pagetitle
        tosave['story'] = splitstory

        toupdate = {}

        toupdate = json.loads(requests.get(f"https://api.jsonbin.io/v3/b/{jsonbinid}/latest", headers = getheader).text)["record"]

        toupdate['stories'].append(tosave)

        requests.put(f"https://api.jsonbin.io/v3/b/{jsonbinid}", json = toupdate, headers = putheader)








#-----------------------------------------------------------------------end of creepy---------------------------------------------------------------------------




#-------------------------------------------------------------------------dispython-----------------------------------------------------------------------------




@client.command()
@commands.has_permissions(administrator = True)
async def runcode(ctx):


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel



    await ctx.send("```Enter the entire code you want to test: (discord library and extensions are available by default. Import any other installed library you might need.)```")

    try:
        scriptres = await client.wait_for("message", check = check, timeout = 300.0)

    except asyncio.TimeoutError:
        await ctx.send("`TimeOut`")
        return

    if len(scriptres.attachments) != 0:
        script = requests.get(scriptres.attachments[0].url).text

    else :
        script = scriptres.content

    scriptlines = script.split("\n")

    scriptfunc = "import discord\nfrom discord.ext import commands\nasync def script(ctx, client):\n    try:\n"

    for line in scriptlines:
        scriptfunc = scriptfunc + "        " + line + "\n"

    scriptfunc = scriptfunc + "    except Exception as err:\n        await ctx.send(str(err))"

    with open('file.py', 'w') as file:
        file.write(scriptfunc)

    await ctx.send("```Running :```\n")

    asyncio.create_task(run(ctx,client))




#-----------------------------------------------------------------------end of dispython---------------------------------------------------------------------------



#----------------------------------------------------------------------------cricket-------------------------------------------------------------------------------

@client.command()
async def cricket(ctx):

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    url = 'https://www.cricbuzz.com/cricket-match/live-scores'

    page = BeautifulSoup(requests.get(url).text, 'lxml')

    live = page.find('div', class_ = 'cb-col cb-col-100 cb-rank-tabs')

    live_matches = live.find_all('div', class_ = 'cb-mtch-lst cb-col cb-col-100 cb-tms-itm')

    matches = discord.Embed(title = 'Live cricket matches : ', description = 'React to the index of the match you want to follow.', color = discord.Color.green())

    for index, item in enumerate(live_matches):
        pieces = item.find_all('div', class_ = 'cb-col-100 cb-col cb-schdl')

        teams = pieces[1].find_all('div', class_ = 'cb-ovr-flo cb-hmscg-tm-nm')
        score = pieces[1].find_all('div', class_ = 'cb-ovr-flo')
        live_status = pieces[1].find('div', class_ = 'cb-text-live')
        complete_status = pieces[1].find('div', class_ = 'cb-text-complete')

        if complete_status:
            status = complete_status
        else :
            status = live_status

        matches.add_field(name = str(index+1) + '. ' + pieces[0].h3.text.strip() + pieces[0].span.text.strip() , value = f'{teams[0].text}    {score[2].text}\n{teams[1].text}    {score[4].text}\n{status.text}')

    matches_message = await ctx.send(embed = matches)

    for index, item in enumerate(live_matches):
        if index > 8:
            break

        await matches_message.add_reaction(emojinumbers[index+1])









##################################################################### END OF COMMANDS ##########################################################################




####################################################################### EVENTS ################################################################################










#On Ready event

@client.event
async def on_ready():
    await client.wait_until_ready()
    await countdownrestart()
    print('bot bread')


#end of On Ready event





#ReactionEvents


@client.event
async def on_raw_reaction_add(message):

    #creepy

    if not message.member.bot:
        creepy = {}


        creepy = json.loads(requests.get(f"https://api.jsonbin.io/v3/b/{jsonbinid}/latest", headers = getheader).text)["record"]

        for story_object in creepy['stories']:


            if int(story_object['message_id']) == message.message_id:

                storymessage = await client.get_channel(int(message.channel_id)).fetch_message(int(message.message_id))

                if str(message.emoji) == '▶️' :
                    if story_object['currentpage'] != story_object['lastpage']:
                        story_object['currentpage'] += 1

                elif str(message.emoji) == '◀️' :
                    if story_object['currentpage'] != 1:
                        story_object['currentpage'] -= 1

                elif str(message.emoji) == '❌' :
                    story_object['currentpage'] = 1


                await storymessage.clear_reactions()



                storyembed = discord.Embed(title = story_object['title'], description = story_object['story'][story_object['currentpage']-1], color = discord.Color.green())

                storyembed.set_footer(text = f"Page {story_object['currentpage']}/{story_object['lastpage']}. Taken from CreepyPasta. Story name : {story_object['title']}")

                await storymessage.edit(embed = storyembed)

                if story_object['currentpage'] != 1 and story_object['currentpage'] != story_object['lastpage'] :
                    await storymessage.add_reaction('❌')
                    await storymessage.add_reaction('◀️')
                    await storymessage.add_reaction('▶️')

                elif story_object['currentpage'] == 1 :
                    await storymessage.add_reaction('❌')
                    await storymessage.add_reaction('▶️')

                elif story_object['currentpage'] == story_object['lastpage'] :
                    await storymessage.add_reaction('❌')
                    await storymessage.add_reaction('◀️')


                requests.put(f"https://api.jsonbin.io/v3/b/{jsonbinid}", json = creepy, headers = putheader)


                return






    #end of creepy






#end of Reactionevents








############################################################## END OF EVENTS ################################################################################


#bot run
client.run(os.getenv('TOKEN'))
