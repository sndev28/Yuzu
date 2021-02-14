import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = 'e!', help_command = None)


@client.event
async def on_ready():
    print('bot bread')

#Help menu

@client.group(invoke_without_command = True)
async def help(ctx):
    help = discord.Embed(title = "This is the help window.", description = "Send e!help <command> to get more information on a specific command.", color = discord.Color.red() )
    help.add_field(name = "helpwindow", value = "Opens this help window.", inline = False)
    help.add_field(name = "test", value = "Random crap test code.",  inline = False)
    help.add_field(name = "emojiret", value = "Returns a message with type and number of each reactions to a specific message.", inline = False)
    help.add_field(name = "announce", value = "Lets make an embedded announcement.", inline = False)
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

#end of Help menu

#Clear

@client.command()
async def clear(ctx, count=(10+1)):
    await ctx.channel.purge(limit = count+1)

#end of Clear

#Test

@client.command()
async def test(ctx):
    embed = discord.Embed(title = "This is a  test embed, Love cats", url = "https://www.instagram.com/p/CLO4sfIpk0z/?utm_source=ig_web_copy_link", description = "Cats are the best in the world. Go kill yourself if you dont like cats.", color = discord.Color.blue())

    embed.set_author(name=ctx.author.display_name, url = "https://www.instagram.com/shamil_niyas/", icon_url=ctx.author.avatar_url)

    embed.set_thumbnail(url="https://static01.nyt.com/images/2020/04/22/science/22VIRUS-PETCATS1/22VIRUS-PETCATS1-mediumSquareAt3X.jpg")


    embed.add_field(name = "I hate rats", value="BWaaah all rats can die for all I care..!!")


    embed.set_footer(text="THIS IS ME SHAMILLLLL!!", icon_url=ctx.author.avatar_url)
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

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    authorprompt = discord.Embed(title = "Do you want to show author in your announcement?", description = "Like Embedy is the author for this message. Please answer y/n. Any other response will be taken as a yes.", colour = discord.Color.red())
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

    thumbprompt = discord.Embed(title = "Do you want to show thumbnail in your announcement?", description = "Like the thumbnail on the upper left corner of this message. Please answer y/n. Any other response will be taken as a no.", colour = discord.Color.red())
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


    announcement = discord.Embed(title = str(titleres.content), description = str(descres.content), colour = discord.Color.green())

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
        print("check1")
        fieldtitle = discord.Embed(title = "Enter the title of the field",color = discord.Colour.red() )
        fielddetail = discord.Embed(title = "Enter the details of the field",color = discord.Colour.red() )

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
        rolestring += str(mentionable.position) + " " + mentionable.name + "\n"

    footerdescription = "Mention the roles to be mentioned in your message. \n" + rolestring


    footerprompt = discord.Embed(title = "Who all do you want to address with this announcement?", descritption = str(footerdescription), colour = discord.Color.red())
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

#bot run
client.run(os.getenv('TOKEN'))
