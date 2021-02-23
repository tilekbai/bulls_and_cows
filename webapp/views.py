from django.shortcuts import render
from random import randint

# Create your views here.

from django.shortcuts import render

secret_nums = []  
def index_view(request):


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
        print("===== SECRET NUMS =====: ", str(secret_nums))
        print(">>>>> PLAYER NUMS >>>>>: ", str(player_nums))

        if player_nums == secret_nums:
            return render(request, 'win.html', numbers_dict) 
        

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

        return render(request, 'result_history.html', numbers_dict)