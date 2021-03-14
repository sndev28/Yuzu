import discord
from discord.ext import commands
import os
import asyncio
from PIL import Image
import io
import time
import math

client = commands.Bot(command_prefix = 'e!', help_command = None)


class colordetail :
    def __init__(self, value, name, command : discord.Color):
        self.value = value
        self.name = name
        self.command = command

class xoplayer :
    def __init__(self, details : discord.Member, mark):
        self.details = details
        self.mark = mark


@client.event
async def on_ready():
    print('bot bread')

#Help menu

@client.group(invoke_without_command = True)
async def help(ctx):
    help = discord.Embed(title = "This is the help window.", description = "Send e!help <command> to get more information on a specific command.", color = discord.Color.red() )
    help.add_field(name = "help", value = "Opens this help window.", inline = False)
    help.add_field(name = "test", value = "Random crap test code.",  inline = False)
    help.add_field(name = "emojiret", value = "Returns a message with type and number of each reactions to a specific message.", inline = False)
    help.add_field(name = "announce", value = "Lets make an embedded announcement.", inline = False)
    help.add_field(name = "rolesret", value = "Lists all the roles in the server", inline = False)
    help.add_field(name = "xo", value = "Play a game of xo or tic tac toe.", inline = False)
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


#end of Help menu


#Clear

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, count=(10+1)):
    await ctx.channel.purge(limit = count+1)

#end of Clear

#Minitest

@client.command()
async def mini(ctx, player : discord.Member):

    xoplayer.details = player

    roleprompt = discord.Embed(title = "XO", description = xoplayer.details.mention, color = discord.Color.red())
    await ctx.send(embed = roleprompt)

#end of minitest

#Rolesret

@client.command()
async def rolesret(ctx):

    rolestring = ""

    givenroles = ctx.guild.roles
    for mentionable in givenroles :
        rolestring = rolestring + str(mentionable.name) + "\n"

    rolestringfinal = rolestring.replace('@', '')


    roleprompt = discord.Embed(title = "Roles in this server", description = str(rolestringfinal), color = discord.Color.red())
    await ctx.send(embed = roleprompt)

#end of rolesret

#Test

@client.command()
async def test(ctx):

    embed = discord.Embed(title = "This is a  test embed, Love cats", url = "https://www.instagram.com/p/CLO4sfIpk0z/?utm_source=ig_web_copy_link", description = "Cats are the best in the world. Go kill yourself if you dont like cats.", color = discord.Color.red())

    embed.set_author(name=ctx.author.display_name, url = "https://www.instagram.com/shamil_niyas/", icon_url=ctx.author.avatar_url)

    embed.set_thumbnail(url="https://static01.nyt.com/images/2020/04/22/science/22VIRUS-PETCATS1/22VIRUS-PETCATS1-mediumSquareAt3X.jpg")


    embed.add_field(name = "I hate rats", value="BWaaah all rats can die for all I care..!!")


    embed.set_footer(text="#lovecats #cats #catslove #catsbest", icon_url="https://static01.nyt.com/images/2020/04/22/science/22VIRUS-PETCATS1/22VIRUS-PETCATS1-mediumSquareAt3X.jpg")
    await ctx.send(embed=embed)

#end of Test

#emojiret

@client.command()
async def emojiret(ctx):
    messageid = ctx.message.reference.message_id
    message = await ctx.fetch_message(messageid)
    emolist = list(message.reactions)

    result = discord.Embed(title = "This is the query asked", description = "given below is the details.")

    for answer in emolist:
        result.add_field(name = answer.emoji, inline = False, value = answer.count)

    await ctx.send(embed=result)

#end of emojiret

#announce

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

#end of announcement


#XO game



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


#end of XO game


#countdown

@client.command()
async def countdown(ctx):

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    def stringgen(hour, min, sec):
        formatstring = " "

        numbers = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


        for char in str(hour):
            formatstring = formatstring + f":{numbers[int(char)]}:"

        if(hour == 1):
            formatstring = formatstring + " :regional_indicator_h: :regional_indicator_r:        "

        else :
            formatstring = formatstring + " :regional_indicator_h: :regional_indicator_r: :regional_indicator_s:        "


        for char in str(min):
            formatstring = formatstring + f":{numbers[int(char)]}:"

        if(min == 1):
            formatstring = formatstring + " :regional_indicator_m: :regional_indicator_i: :regional_indicator_n: "

        else :
            formatstring = formatstring + " :regional_indicator_m: :regional_indicator_i: :regional_indicator_n: :regional_indicator_s:        "


        for char in str(sec):
            formatstring = formatstring + f":{numbers[int(char)]}:"

        if(sec == 1):
            formatstring = formatstring + " :regional_indicator_s: :regional_indicator_e: :regional_indicator_c:"

        else :
            formatstring = formatstring + " :regional_indicator_s: :regional_indicator_e: :regional_indicator_c: :regional_indicator_s:"


        return formatstring





    timeprompt = discord.Embed(title = "Countdown wizard", description = "Enter the time to countdown as per the given example. \n 20 Nov 2021 @ 11:23:59", color = discord.Color.red())

    await ctx.send(embed = timeprompt)

    try :
        timeres =  await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 3)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return

    messageprompt = discord.Embed(title = "Countdown wizard", description = "What message do you want me to send at the end of the countdown? Anyone to be mentioned can be added to this message as well at the end of the message seperated by a |", color = discord.Color.red())
    messageprompt.add_field(name = "Example", value = "Hi everyone, this is the end of the countdown | @mentions", inline = False)

    await ctx.send(embed = messageprompt)

    try:
        messageres = await client.wait_for('message', check = check, timeout = 300.0)
        await ctx.channel.purge(limit = 2)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")
        return


    messagedetails = messageres.content.split('|')

    deadlinedetails = time.strptime(timeres.content,'%d %b %Y @ %H:%M:%S' )

    deadline = time.mktime(deadlinedetails)

    #initialization message

    remaining = math.trunc(deadline - time.time())
    totalminutes = math.trunc(remaining/60)
    hours = math.trunc(totalminutes/60)
    minutes = totalminutes % 60
    seconds = remaining % 60

    timestring = stringgen(hours, minutes, seconds)

    initmessage = await ctx.send(timestring)
    finalmessage = await ctx.send("*")


    while(True):
        remaining = deadline - time.time()


        if remaining <= 0 :

            await initmessage.edit(content = timestring)
            await finalmessage.edit(content = f" \n ` {messagedetails[0]} ` {messagedetails[1]}")
            break

        else:

            remaining = math.trunc(deadline - time.time())
            totalminutes = math.trunc(remaining/60)
            hours = math.trunc(totalminutes/60)
            minutes = totalminutes % 60
            seconds = remaining % 60

            timestring = stringgen(hours, minutes, seconds)

            await initmessage.edit(content = timestring)




#end of countdown




#bot run
client.run(os.getenv('TOKEN'))
