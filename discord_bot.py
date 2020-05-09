import discord
TOKEN = "NzA4NTE1OTM5Mjk3MTMyNTY2.XrYe_A.gBLVFt1koHlB8Xg2MZCEB5Jaymw"
client = discord.Client()
ID = 708531208472100934
@client.event
async def on_ready():
    print("Logged in us")
    print(client.user.name)
    print(client.user.id)
    print("-----")
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == ID:
        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = discord.utils.find(lambda r: r.name == payload.emoji.name, guild.roles)
        if role is not None:
            print(role.name + " was found!")
            print(role.id)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.add_roles(role)
            print("done")

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == ID:
        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = discord.utils.find(lambda r: r.name == payload.emoji.name, guild.roles)
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
            print("done")
client.run(TOKEN)
