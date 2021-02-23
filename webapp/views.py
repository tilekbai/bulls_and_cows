from django.shortcuts import render
from random import randint

# Create your views here.

from django.shortcuts import render
from collections import Counter

secret_nums = []
all_result_list = []

def index_view(request):
    result_dict = {}

    while len(secret_nums) != 4:
        rand = (randint(1, 10))
        if rand not in secret_nums:
            secret_nums.append(rand)

    if request.method == 'GET':
        return render(request, 'index.html')


    elif request.method == 'POST':
        
        numbers_dict = {
            'first_number':request.POST.get('first_number'),
            'second_number':request.POST.get('second_number'),
            'third_number':request.POST.get('third_number'),
            'fourth_number':request.POST.get('fourth_number'),
            }

        player_nums = []
        bulls = []
        cows = []

        for key in numbers_dict:
            player_nums.append(int(numbers_dict[key]))

        if player_nums == secret_nums:
            for el in player_nums:
                bulls.append(el)
                result_dict['bulls'] = len(bulls)
            result_dict['cows'] = len(cows)
            all_result_list.append(result_dict)
            secret_nums.clear()
            all_result_list.clear()
            return render(request, 'win.html', numbers_dict) 
        
        
        if [k for k,v in Counter(player_nums).items() if v>1]:
            return render(request, 'error.html', numbers_dict) 
        else:
            for el in player_nums:
                try:
                    if player_nums.index(el) == secret_nums.index(el):
                        bulls.append(el)
                        numbers_dict['bulls'] = len(bulls)

                    else:
                        cows.append(el)
                        numbers_dict['cows'] = len(cows)

                except ValueError:
                    pass
        
            result_dict['bulls'] = len(bulls)
            result_dict['cows'] = len(cows)
            all_result_list.append(result_dict)
            return render(request, 'result_history.html', numbers_dict)
            

        


def result_page_view(request): 
    result_page_dict = {i: d for i, d in enumerate(all_result_list, 1)}
    return render(request, 'result_page.html', {'result_page_dict': result_page_dict})