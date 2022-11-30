import re
import requests
from django.core.management.base import BaseCommand
from app.models import Categories
from app.models import News


def get_news():
    url = 'https://content.guardianapis.com/search?api-key=99b95102-072a-4131-ba40-bc800d0fd653&show-fields=thumbnail&&page-size=20&q=all&show-blocks=all'
    response = requests.get(url, headers={'Content-Type':
                                          'application/json'})
    data = response.json()
    # print(data['response']['results'][0]['blocks']['body'][0]['bodyHtml'])
    results = data['response']['results']
    return results


# def seed_news():
#     for i in get_news():
#         news = News(
#             title=i['webTitle'],
#             description=i[0]['blocks']['body'][0]['bodyHtml'],
#             slug=i['id'],)

#     news.save()



def seed_news():
    url = 'https://content.guardianapis.com/search?api-key=99b95102-072a-4131-ba40-bc800d0fd653&show-fields=thumbnail&&page-size=20&q=life&show-blocks=all'
    response = requests.get(url, headers={'Content-Type':
                                          'application/json'})
    data = response.json()
    results = data['response']['results']

    for i in results:
        News.objects.create(
            title=i['webTitle'],
            image=i['fields']['thumbnail'],
            description=i['blocks']['body'][0]['bodyTextSummary'],
            category=Categories.objects.get(name='Lifestyle')
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_news()
        # clear_data()
        print("completed")
