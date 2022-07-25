from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import MainForm


# Create your views here.
def index(request):
    if request.method =='POST':
        form = MainForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            if 'add' in request.POST:
                res = num1 + num2
            if 'sub' in request.POST:
                res = num1 - num2
            if 'mul' in request.POST:
                res = num1 * num2
            if 'pot' in request.POST:
                res = num1 ** num2
            if 'div' in request.POST:
                if num2==0:
                    res = "Error división por cero"
                else:
                    res = num1 / num2
            if 'root' in request.POST:
                if num1<0:
                    res = 'Error: Base negativa para la raiz'
                else:
                    res = num1 ** (1/num2)
            args = {'form': form , 'result': res}
            return render(request, 'inputs.html', args)


    else:
        form = MainForm()
        return render(request, 'inputs.html', {'form': form})
