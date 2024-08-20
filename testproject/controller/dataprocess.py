from django.shortcuts import render
import json
from django.http import HttpResponse

def homepage(request):
    return render(request, 'index.html', {"data": ""})

def segitiga(request):
    numberInput = request.POST['numberInput']

    result = []
    numList = [int(digit) for digit in str(numberInput)]
    n = 1
    for x in numList:
        tmp = str(x)
        for i in range(0, n):
            tmp += '0'
    
        result += [tmp]
        n += 1
    data = {
        "numberInput" : result
    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def ganjil(request):
    numberInput = request.POST['numberInput']

    text = ''
    number = int(numberInput) + 1
    for iteration in range (1, number):
        if iteration % 2 != 0 :
            temp = str(iteration)
            text = text + ' ' + temp

    data = {
        "numberInput" : text
    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def prima(request):
    numberInput = request.POST['numberInput']

    text = '2'
    number = int(numberInput) + 1
    for iteration in range (3, number):
        if iteration % 2 != 0 :
            m = 0
            for iteration_in in range(2, number):
                if iteration % iteration_in == 0 and iteration != iteration_in:
                    m = 1
                    break
            
            if m == 0:
                temp = str(iteration)
                text = text + ' ' + temp

    data = {
        "numberInput" : text
    }

    return HttpResponse(json.dumps(data), content_type="application/json")