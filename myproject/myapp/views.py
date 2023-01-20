from django.shortcuts import render

def rectarea(request):
    context = {}

    context['area'] = "0"

    context['a'] = "0"

    context['b'] = "0"

    if request.method == 'POST':

        print("POST method is used")

        a = request.POST.get('length', '0')

        b = request.POST.get('breadth', '0')

        print('request=',request)

        print('Length=',1)

        print('Breadth=',b)

        area= int(a) * int(b)

        context['area'] = area

        context['a'] = a

        context['b'] = b

        print('Area=', area)

        return render(request, 'myapp/math.html', context)



