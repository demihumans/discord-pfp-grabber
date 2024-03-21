import nextcord
import asyncio

client = nextcord.Client()
token='' # enter bot token here btw if ur a retard

async def x():
    i = input("Enter User's ID: ")

    try:
        user = await client.fetch_user(int(i))
    except nextcord.errors.NotFound:
        await x()

    if user.avatar:
        ii = user.avatar.url
    else:
        ii = user.default_avatar.url

    print(f"av: {ii}")

@client.event
async def on_ready():
    print('               ,                  \n               Et                 \n               E#t                \n  t            E##t     t         \n  ED.          E#W#t    ED.       \n  E#K:         E#tfL.   E#K:      \n  E##W;        E#t      E##W;     \n  E#E##t    ,ffW#Dffj.  E#E##t    \n  E#ti##f    ;LW#ELLLf. E#ti##f   \n  E#t ;##D.    E#t      E#t ;##D. \n  E#ELLE##K:   E#t      E#ELLE##K:\n  E#L;;;;;;,   E#t      E#L;;;;;;,\n  E#t          E#t      E#t       \n  E#t          E#t      E#t       \n               ;#t                \n                :;                ')
    await x()

client.run(token)
