from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from selenium import webdriver
from newsapi import NewsApiClient
import spacy
import re

def media_analytics(request, company_name):
    # Download news articles using company name from search engines
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/search?q=" + company_name)
    page_source = driver.page_source
    driver.close()

    newsapi = NewsApiClient(api_key='d83a0fb9e3104414a3693c6c4fdab735')
    search_results = newsapi.get_everything(q=company_name)
    print(search_results['articles'])

    # Combine results from search engines and News API
    articles = search_results['articles'] + page_source

    # NER module
    nlp = spacy.load("en_core_web_sm")
    risk_entities = []
    for article in articles:
        doc = nlp(article)
        for ent in doc.ents:
            if ent.label_ == "ORG":
                if company_name.lower() in ent.text.lower():
                    for token in ent.subtree:
                        if token.ent_type_ == "RISK":
                            risk_entities.append(token.text)

    # Relationship module
    risk_sentences = []
    for article in articles:
        for sentence in article.split("."):
            if any(entity in sentence for entity in risk_entities):
                risk_sentences.append(sentence)

    # Dashboard
    return render(request, "dashboard.html", {"risk_sentences": risk_sentences})