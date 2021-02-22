from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index_view(request):
    # return render(request, 'index.html')
    if request.method == 'GET':
        return render(request, 'index.html')
    

    elif request.method == 'POST':
        
        context_calc = {
            'first_number':request.POST.get('first_number'),
            'second_number':request.POST.get('second_number'),
            'operation':request.POST.get('operation'),
            'res' : 0,
            'sign' : '0',
            }

        try:
            numbers = (list(map(int, request_body['numbers'][0].split(' '))))
            response_body += f'<div>{", ".join(list(map(str, numbers)))}</div>'
            
        except ValueError:
            numbers = (list(map(str, request_body['numbers'][0].split(' '))))
            response_body += f'<div>{", ".join(list(map(str, numbers)))}</div>'
            response_body += f'<div>Error: Enter numbers</div>'
            request_body = parse_qs(request.body.decode())

        
        return render(request, 'result_history.html', context_calc) 