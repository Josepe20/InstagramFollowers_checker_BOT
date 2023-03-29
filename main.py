from bot_settings import InstagramFollowerBot

profile_link = input("May you provide me your profile link: ")
print(profile_link)

bot = InstagramFollowerBot()
bot.log_in_bot()
bot.find_following_users(profile_to_visit=profile_link)
bot.find_follower_users(profile_to_visit=profile_link)


