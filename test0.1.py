import discord
import time
import threading
import datetime
from time import perf_counter
token = 'bRuh_69fUcK420YoU_eaTAsSSucKdiCk6969'
uno = False
cah = False
oneVone = False
chess = False
tea = False
ping = True
nitro = True
ready = False

uno_r = True
cah_r = True
ovo_r = True
chess_r = True
tea_r = True

guild = 469335072034652199

client = discord.Client()


@client.event
async def on_ready():
    global ready
    print('We have logged in as {}'.format(client.user))
    print("please work")
    ready = True

@client.event
async def on_message(message):
    global guild
    global ping
    global uno
    global cah
    global oneVone
    global chess
    global tea
    global elapsed
    global tuno_start
    global tcah_start
    global tovo_start
    global tchess_start
    global ttea_start
    global nitro
    global ready

    global uno_r
    global cah_r
    global ovo_r
    global chess_r
    global tea_r


    channel = client.get_channel(494370901463138305)
    
    if (ready is True and uno is False and cah is False and oneVone is False and chess is False and tea is False) or (message.content == 'n!ready'):
        
        rolecah = message.guild.get_role(474654468454219776)
        await rolecah.edit(guild=guild, role=rolecah, mentionable=True)
        print('\ncah mentionable = true\n')

        roleuno = message.guild.get_role(472810185946038272)
        await roleuno.edit(guild=guild, role=roleuno, mentionable=True)
        print('\nuno mentionable = true\n')

        roleovo = message.guild.get_role(618601197817036800)
        await roleovo.edit(guild=guild, role=roleovo, mentionable=True)
        print('\n1v1 mentionable = true\n')

        rolechess = message.guild.get_role(499039071822282762)
        await rolechess.edit(guild=guild, role=rolechess, mentionable=True)
        print('\nchess mentionable = true\n')

        roletea = message.guild.get_role(597141127845642241)
        await roletea.edit(guild=guild, role=roletea, mentionable=True)
        print('\ntea mentionable = true\n')

        ready = False


    if message.content == 'n!ping' or message.content == 'n!Ping':
        await message.channel.send("Pong! `{} ms` of lag".format((client.latency)*1000))
                
    if message.content == 'n!help' or message.content == 'n!Help':
        await message.channel.send("```prefix = n!\nhelp = show this menu\nping = force it to say pong owo\nuno = check if the Uno ping is available\ncah = check if the CAH ping is available\n1v1 = check if the Uno 1v1 ping is available\ntea = check if the Uno Tea ping is available```")

    if message.content == 'n!nitro' and nitro is True:
        await message.channel.send("n/a")
        nitro = False

    #UNO Command
    if message.content == 'n!uno' and uno is True:
        await message.channel.send("You can't Ping for UNO yet!!!")
        tuno_stop = perf_counter()
        print("\nElapsed time: ", tuno_stop, tuno_start)
        await message.channel.send("Calculating elapsed time since the last ping...")
        timeu_elapsed = round(tuno_stop - tuno_start)
        formatted_timeu = str(datetime.timedelta(seconds=timeu_elapsed))
        await message.channel.send(formatted_timeu)

    if message.content == 'n!uno' and uno is False:
        await message.channel.send("You can ping for UNO now!")

    #CAH Command
    if message.content == 'n!cah' and cah is True:
        await message.channel.send("You can't Ping for CAH yet!!!")
        tcah_stop = perf_counter()
        print("Elapsed time: ", tcah_stop, tcah_start)
        await message.channel.send("Calculating elapsed time since the last ping...")
        timec_elapsed = round(tcah_stop - tcah_start)
        formatted_timec = str(datetime.timedelta(seconds=timec_elapsed))
        await message.channel.send(formatted_timec)

    if message.content == 'n!cah' and cah is False:
        await message.channel.send("You can ping for CAH now!")

    #1v1 Command
    if message.content == 'n!1v1' and oneVone is True:
        await message.channel.send("You can't Ping for Uno 1v1 yet!!!")
        tovo_stop = perf_counter()
        print("\nElapsed time: ", tovo_stop, tovo_start)
        await message.channel.send("Calculating elapsed time since the last ping...")
        timeovo_elapsed = round(tovo_stop - tovo_start)
        formatted_timeovo = str(datetime.timedelta(seconds=timeovo_elapsed))
        await message.channel.send(formatted_timeovo)
        
    if message.content == 'n!1v1' and oneVone is False:
        await message.channel.send("You can ping for Uno 1v1 now!")
        
     #chess Command
    if message.content == 'n!chess' and chess is True:
        await message.channel.send("You can't Ping for Chess yet!!!")
        tchess_stop = perf_counter()
        print("\nElapsed time: ", tchess_stop, tchess_start)
        await message.channel.send("Calculating elapsed time since the last ping...")
        timechess_elapsed = round(tchess_stop - tchess_start)
        formatted_timechess = str(datetime.timedelta(seconds=timechess_elapsed))
        await message.channel.send(formatted_timechess)

    if message.content == 'n!chess' and chess is False:
        await message.channel.send("You can ping for Chess now!")

     #tea Command
    if message.content == 'n!tea' and tea is True:
        await message.channel.send("You can't Ping for Tea yet!!!")
        ttea_stop = perf_counter()
        print("\nElapsed time: ", ttea_stop, ttea_start)
        await message.channel.send("Calculating elapsed time since the last ping...")
        timetea_elapsed = round(ttea_stop - ttea_start)
        formatted_timetea = str(datetime.timedelta(seconds=timetea_elapsed))
        await message.channel.send(formatted_timetea)

    if message.content == 'n!tea' and tea is False:
        await message.channel.send("You can ping for Tea now!")

    def unoTimer():
        global uno
        global uno_r
        uno = False
        uno_r = False
        print("\nUNO Timer Ended")

    if uno_r is False:
        roleuno = message.guild.get_role(472810185946038272)
        await roleuno.edit(guild=guild, role=roleuno, mentionable=True)
        print('\nuno mentionable = true\n')
        uno_r = True

    def cahTimer():
        global cah
        global cah_r
        cah = False
        cah_r = False
        print("\nCAH Timer Ended")

    if cah_r is False:
        rolecah = message.guild.get_role(474654468454219776)
        await rolecah.edit(guild=guild, role=rolecah, mentionable=True)
        print('\ncah mentionable = true\n')
        cah_r = True

    def oneVoneTimer():
        global oneVone
        global ovo_r
        oneVone = False
        ovo_r = False
        print('\n1v1 timer has ended')

    if ovo_r is False:
        roleovo = message.guild.get_role(618601197817036800)
        await roleovo.edit(guild=guild, role=roleovo, mentionable=True)
        print('\n1v1 mentionable = true\n')
        ovo_r = True
    
    def chessTimer():
        global chess
        global chess_r
        chess = False
        chess_r = False
        print('\nChess timer has ended')

    if chess_r is False:
        rolechess = message.guild.get_role(499039071822282762)
        await rolechess.edit(guild=guild, role=rolechess, mentionable=True)
        print('\nchess mentionable = true\n')
        chess_r = True

    def teaTimer():
        global tea
        global tea_r
        tea = False
        tea_r = False
        print('\nTea timer has ended')

    if tea_r is False:
        roletea = message.guild.get_role(597141127845642241)
        await roletea.edit(guild=guild, role=roletea, mentionable=True)
        print('\ntea mentionable = true\n')
        tea_r = True

    if message.guild.id == guild:

        #UNO Ping
        if message.role_mentions:
            if message.role_mentions[0].name == 'Ping for Uno' and uno is False:
                await message.channel.send("Pinged for Uno!!\nCounter Started")
                uno = True
                roleuno = message.guild.get_role(472810185946038272)
                await roleuno.edit(guild=guild, role=roleuno, mentionable=False)
                uno_timer = threading.Timer(1800.0, unoTimer)
                uno_timer.start()
                print("Uno Timer started\n")
                tuno_start = perf_counter()

            elif message.role_mentions[0].name == 'Ping for Uno' and uno is True:
                await message.channel.send("{} You pinged within 30 minutes of the last ping.\nIf you ping within the timeline too much, you will be muted".format(message.author.mention))
                await channel.send("{} pinged for Uno within the cool-down".format(message.author.mention))
                print("\nWarned User")

        #CAH Ping
        if message.role_mentions:
            if message.role_mentions[0].name == 'Ping for CAH' and cah is False:
                await message.channel.send("Pinged for CAH!!\nCounter Started")
                cah = True
                rolecah = message.guild.get_role(474654468454219776)
                await rolecah.edit(guild=guild, role=rolecah, mentionable=False)
                cah_timer = threading.Timer(1800.0, cahTimer)
                cah_timer.start()
                print("\nCAH Timer started")
                tcah_start = perf_counter()

            elif message.role_mentions[0].name == 'Ping for CAH' and cah is True:
                await message.channel.send("{} You pinged within 30 minutes of the last ping.\nIf you ping within the timeline too much, you will be muted".format(message.author.mention))
                await channel.send("{} pinged for CAH within the cool-down".format(message.author.mention))
                print("\nWarned User")

        #1v1 Ping
        if message.role_mentions:
            if message.role_mentions[0].name == 'Ping for Uno 1v1' and oneVone is False:
                await message.channel.send("Pinged for Uno 1v1!!\nCounter Started")
                oneVone = True
                roleovo = message.guild.get_role(618601197817036800)
                await roleovo.edit(guild=guild, role=roleovo, mentionable=False)
                ovo_timer = threading.Timer(1800.0, oneVoneTimer)
                ovo_timer.start()
                print("\nUno 1v1 Timer started")
                tovo_start = perf_counter()

            elif message.role_mentions[0].name == 'Ping for Uno 1v1' and oneVone is True:
                await message.channel.send("{} You pinged within 30 minutes of the last ping.\nIf you ping within the timeline too much, you will be muted".format(message.author.mention))
                await channel.send("{} pinged for Uno 1V1 within the cool-down".format(message.author.mention))
                print("\nWarned User")

        #Chess Ping
        if message.role_mentions:
            if message.role_mentions[0].name == 'Ping For Chess' and chess is False:
                await message.channel.send("Pinged for Chess!!\nCounter Started")
                chess = True
                rolechess = message.guild.get_role(499039071822282762)
                await rolechess.edit(guild=guild, role=rolechess, mentionable=False)
                chess_timer = threading.Timer(1800.0, chessTimer)
                chess_timer.start()
                print("\nChess Timer started")
                tchess_start = perf_counter()

            elif message.role_mentions[0].name == 'Ping for Chess' and chess is True:
                await message.channel.send("{} You pinged within 30 minutes of the last ping.\nIf you ping within the timeline too much, you will be muted".format(message.author.mention))
                await channel.send("{} pinged for Chess within the cool-down".format(message.author.mention))
                print("\nWarned User")

        #Tea Ping
        if message.role_mentions:
            if message.role_mentions[0].name == 'Ping for Tea' and tea is False:
                await message.channel.send("Pinged for Tea!!\nCounter Started")
                tea = True
                roletea = message.guild.get_role(597141127845642241)
                await roletea.edit(guild=guild, role=roletea, mentionable=False)
                tea_timer = threading.Timer(1800.0, teaTimer)
                tea_timer.start()
                print("\nTea Timer started")
                ttea_start = perf_counter()

            elif message.role_mentions[0].name == 'Ping For Tea' and tea is True:
                await message.channel.send("{} You pinged within 30 minutes of the last ping.\nIf you ping within the timeline too much, you will be muted".format(message.author.mention))
                await channel.send("{} pinged for Chess within the cool-down".format(message.author.mention))
                print("\nWarned User")

client.run(token)