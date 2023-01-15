import requests
from bs4 import BeautifulSoup

class weather:
    def getWeather():
        area = "충주"
        webpage = requests.get('https://www.google.com/search?q=날씨+' + area) #search weather in google
        soup = BeautifulSoup(webpage.text, "html.parser") #parse webpage

        weatherToday = soup.find_all(attrs={'class': 'tAd8D'}) #find weather class in webpage
        temp = soup.find(attrs={'class': 'iBp4i'}) # find temprature class in webpage 
        location = weatherToday[0].get_text() #receive location data
        weather = weatherToday[1].get_text() #receive weather data
        temprature = temp.get_text() #receive temp data
        return f'{location}\n{weather}\n{temprature}' #return value 
