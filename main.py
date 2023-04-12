from bot_settings import InstagramFollowerBot
from reportlab.pdfgen import canvas

# josechay_20

# input where you may provide username
profile_input = input(f"May you provide me your instagram username:")

profile_link = f"https://www.instagram.com/{profile_input}/"

bot = InstagramFollowerBot(profile_link)
bot.log_in_bot()

# converting methods to variables, which are lists
following = bot.find_following_users(profile_to_visit=profile_link)
followers = bot.find_follower_users(profile_to_visit=profile_link)

print(following)
print(len(following))
print(followers)
print(len(followers))

following_set = set(following)
followers_set = set(followers)

# Elements that are in following_set but not in followers_set
uncommon_following = list(following_set - followers_set)

# Elements that are in followers_set but not in following_set
uncommon_followers = list(followers_set - following_set)

print(uncommon_following)
print(len(uncommon_following))

print(uncommon_followers)
print(len(uncommon_followers))

# merge uncommon lists with unique elements
unique_items = uncommon_followers + uncommon_following

# define the title and bullet point list
title = 'Users who don\'t follow you or you neither follow them'
# users = ['User ' + str(i) for i in range(1, 301)]

# set the font and font size for the title
title_font = ('Helvetica-Bold', 14)

# set the font and font size for the list
list_font = ('Helvetica', 12)

# define the page size and margin
page_width, page_height = 595.27, 841.89  # A4 size in points (1/72 inch)
left_margin, right_margin = 50, 50
top_margin, bottom_margin = 50, 50
usable_width = page_width - left_margin - right_margin
usable_height = page_height - top_margin - bottom_margin

# create a new PDF canvas and start the first page
pdf = canvas.Canvas('instagram-users.pdf')
pdf.setTitle(title)
pdf.setFont(*title_font)
pdf.drawCentredString(page_width/2, page_height-top_margin-20, title)

# add the bullet point list to the first page
y = page_height - top_margin - 50
for i, item in enumerate(unique_items):
    if y <= bottom_margin + 50:
        # if there isn't enough space for the next item, start a new page
        pdf.showPage()
        y = page_height - top_margin - 50
        pdf.setFont(*title_font)
        pdf.drawCentredString(page_width/2, page_height-top_margin-20, title)
        pdf.setFont(*list_font)
    pdf.drawString(left_margin, y, '\u2022')
    pdf.drawString(left_margin + 20, y, item)
    y -= 20

# save the PDF
pdf.save()




