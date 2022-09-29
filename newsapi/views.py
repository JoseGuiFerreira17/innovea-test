from django.shortcuts import render
import requests
from decouple import config

def index(request):
    api = "https://newsapi.org/v2/everything?q=keyword&apiKey="+config("API_KEY")
    requisicao = requests.get(api)

    list = requisicao.json()
    list = list["articles"]
    title = []
    desc = []
    author = []

    for i in range(len(list)):
        news = list[i]
        title.append(news['title'])
        desc.append(news['description'])
        author.append(news['author'])
    all_articles = zip(title, desc, author)

    
    context = {
        "articles": all_articles
    }

    return render(request, "index.html", context)