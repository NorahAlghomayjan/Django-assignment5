from django.shortcuts import render
import random 


def index(request):

    guess = random.randint(1, 100)
    print(guess)
    
    request.session['guess'] = guess
    request.session['attempts'] = 0

    return render(request,'index.html')


def result (request):

    print(request.session['attempts'])
    
    userGuess = int(request.POST.get('guess'))
    request.session['guess']

    if (userGuess == request.session['guess']):
        result = f'{userGuess} was the right number!'
        context = {"result": result}
        return render(request,'win.html',context)
    
    if (request.session['attempts'] == 4):
        context = {"result": "You Lose"}
        return render(request,'win.html',context)

    if (userGuess > request.session['guess']):
        result = 'Too high!'
    else:
        result = 'Too low!'

    request.session['attempts'] += 1  
    context = {"result": result,
    'attempts':request.session['attempts']}

    return render(request,'result.html',context)