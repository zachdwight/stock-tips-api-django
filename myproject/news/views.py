from django.shortcuts import render

# We are going to use the demo sentiment call from alphavantage.co as our example
# https://www.alphavantage.co/

# You can swap out any sort of call/link to whatever source you are interested in but make sure you update news_list with the right items of interest

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
import datetime

@api_view(['GET'])
def get_financial_news(request):
    """Parses Alpha Vantage news sentiment API response."""
    ticker = request.GET.get('tickers', 'AAPL') 
    api_key = request.GET.get('apikey', 'demo') #
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPError handling for bad calls
        data = response.json()

        if "feed" not in data: #Check for errors from API
            return Response({"error": data.get("Information", "Unknown Alpha Vantage API Error")}, status=500)

        news_list = []
        for item in data["feed"]:
            news_list.append({
                "title": item.get("title"),
                "link": item.get("url"),
                "time": item.get("time_published"),
                "sentiment": item.get("overall_sentiment_label")
            })

        return Response(news_list)

    except requests.exceptions.RequestException as e:
        return Response({"error": f"Failed to fetch news: {e}"}, status=500)
    except ValueError: #Handles JSON decode errors
        return Response({"error": "Invalid JSON response from Alpha Vantage"}, status=500)
    except KeyError as e: #Handles missing key in the json response
        return Response({"error": f"Missing key in Alpha Vantage response: {e}"}, status=500)
    except Exception as e:
        return Response({"error": f"An unexpected error occurred: {e}"}, status=500)

