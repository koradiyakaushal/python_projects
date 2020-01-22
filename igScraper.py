import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound

language = "en"
URL = "https://www.instagram.com/{}/"

def scrape(username):
    full_url = URL.format(username)
    r = requests.get(full_url)
    s = BeautifulSoup(r.text, "lxml")

    tag = s.find("meta", attrs = {"name": "description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]

    return main_text

USERNAME = input("Enter your Instagram username: ")
data = scrape(USERNAME)

speech = gTTS(text=data, lang=language, slow=False)
speech.save("text.mp3")
playsound("text.mp3")
print(data)