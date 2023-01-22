

# Weather, News, Stock and Portfolio API
This code provides an implementation of four classes: Weather, News, Stock, and Portfolio. Each class uses different external APIs to retrieve data. The Weather class retrieves weather data, the News class retrieves news headlines, the Stock class retrieves stock data and the Portfolio class retrieves all data from all the classes above mentioned.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
You will need to have the following libraries installed:
```
requests
json
```

You will also need API keys for the following APIs:
```
OpenWeatherMap API
NewsAPI
Alpha Vantage API
```
## Installing
Clone the repository

```
git clone https://github.com/pawelfkk/super_simple_weather_api_python
```
## Usage
You can use this code to retrieve weather data, news headlines, stock data, and all data. To use the code, you need to first create an instance of the Portfolio class and provide your API keys as arguments.

```
portfolio = Portfolio("YOUR_WEATHER_API_KEY", "YOUR_NEWS_API_KEY", "YOUR_STOCK_API_KEY")
```
You can then use the get_weather(), get_headlines() and get_stock_data() methods to retrieve weather data, news headlines, and stock data respectively.

```
data = portfolio.get_all_data("New York", "us", "AAPL")
```
You can also use the get_all_data() method to retrieve all data at once.


```
print(data)
```
## Note
Be sure to replace the placeholder strings "YOUR_WEATHER_API_KEY", "YOUR_NEWS_API_KEY", "YOUR_STOCK_API_KEY" with your actual API keys.


## Authors
Pawel - https://github.com/pawelfkk/super_simple_weather_api_python
## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
OpenWeatherMap API, NewsAPI and Alpha Vantage API for providing data.
