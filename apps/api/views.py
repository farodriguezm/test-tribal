import http3
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def ping(request):
    return Response("pong")


async def jokes(request):
    jokes = []
    uri = 'https://api.chucknorris.io/jokes/random'

    client = http3.AsyncClient(verify=False)
    while len(jokes) < 15:
        exists = False
        data = await client.get(uri)
        temp = data.json()
        id = temp['id']

        for el in jokes:
            if el['id'] == id:
                exists = True

        if(not exists):
            jokes.append({
                'id': temp['id'],
                'icon_url': temp['icon_url'],
                'value': temp['value']
            })

    return JsonResponse(jokes, safe=False)
