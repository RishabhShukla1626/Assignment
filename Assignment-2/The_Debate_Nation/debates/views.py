from django.shortcuts import render, redirect
from .models import Debates, Arguments
from .forms import ArgumentsForm
# Create your views here.

#debate list view
def debates(request):
    debates = Debates.objects.all().order_by('-created')
    context = {"debates": debates}
    return render(request, 'debates/debates.html', context)


def add_arguement(request, pk):
    try:
        debate = Debates.objects.get(id=pk)
        argument = Arguments.objects.filter(debate=debate)[0]
        form = ArgumentsForm(instance=argument)
        if request.method == "POST":
            form = ArgumentsForm(request.POST, instance=argument)
            if form.is_valid():
                Arguments.objects.create(debate=debate, 
                argument=request.POST['argument'],
                opinion=request.POST['opinion'])
                return redirect("debates")
        context = {"form": form}
        return render(request, "debates/argument_form.html", context)
    except Exception as e:
        raise Exception(e)

