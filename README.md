# Instagram Web Scraper Bot 💚
Web scraper bot created to facilitate the task of counting the Instagram followers who follow you but they don't follow you or the followers who don't follow them either.

<img src="https://i.ibb.co/Pzcsyb9/intagram-bot.jpg" alt="Instagram Bot" border="0" />

# # Algorithm
The bot starts by driving in the Chrome browser, logs in as a default user, and searches for the user it wants to search for. Enter the “following” section and scroll down when finished create a list, repeat the same process for the “followers” section.

Finally, it merges the two lists and creates a new one with unique elements to later create a PDF document with this list.

<img src="https://i.ibb.co/x2ZdR5h/Instagram-followers-checker-Diagram.jpg" alt="Diagrama de flujo" border="0" />

## Developed with technologies such as:

> Automatization 
> - Python
> - Selenium 
> - ReportLab

### Project features
* Web driving (Selenium Chrome)
* Web scraping (Selenium Chrome)
* PDF creation (ReportLab)