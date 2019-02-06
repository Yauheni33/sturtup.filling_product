import json
from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def generation(request):
    with open('/Users/yauheni/PycharmProjects/Django/mysite/polls/templates/good_menu.json', 'r') as file:
        data = json.loads(file.read())
    keys = request.POST.dict().keys()
    u = {"menu_id": len(data['menus']) + 1, "place_name": request.POST.dict()['placeName'], "price": round(float(request.POST.dict()['price']), 2), "product_ids": []}
    for i in keys:
        if 'product' in i:
            u['product_ids'].append(int(request.POST.dict()[i]))
    data['menus'].append(u)
    with open('/Users/yauheni/PycharmProjects/Django/mysite/polls/templates/good_menu.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False)
    return HttpResponse('Ваше меню принято')

def read(request):
    return render(request, 'index.html')

def login(request):
    with open('/Users/yauheni/PycharmProjects/Django/mysite/polls/templates/users.json', 'r') as file:
        data = file.read()
    users = json.loads(data)
    return HttpResponse('OK' if request.GET['firstname'] in users['users'] else 'Неверный логин')
