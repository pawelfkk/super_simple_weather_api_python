import requests
import json

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        url = f"{self.base_url}?q={city}&appid={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

class News:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def get_headlines(self, country):
        url = f"{self.base_url}?country={country}&apiKey={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

class Stock:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def get_stock_data(self, symbol):
        url = f"{self.base_url}?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

class Portfolio:
    def __init__(self, weather_api_key, news_api_key, stock_api_key):
        self.weather = Weather(weather_api_key)
        self.news = News(news_api_key)
        self.stock = Stock(stock_api_key)

    def get_all_data(self, city, country, symbol):
        weather_data = self.weather.get_weather(city)
        news_data = self.news.get_headlines(country)
        stock_data = self.stock.get_stock_data(symbol)
        return weather_data, news_data, stock_data

if __name__ == "__main__":
    portfolio = Portfolio("WEATHER_API_KEY", "NEWS_API_KEY", "STOCK_API_KEY")
    data = portfolio.get_all_data("Warszawa", "pl", "AAPL")
    print(data)
