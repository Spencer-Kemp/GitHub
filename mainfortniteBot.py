from fortniteBot import fortniteBot

bot1 = fortniteBot("Ninja")
bot2 = fortniteBot("Chat")
bot3 = fortniteBot("Orange")

fortniteBot.health = 95 # changes all bots health to 95
bot1.take_damage(5)
bot2.take_damage(200)

print(bot1.health)
print(bot1.name)

print(bot2.health)
print(bot3.health)