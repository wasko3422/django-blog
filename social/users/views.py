from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations {}'.format(form.cleaned_data['username']))
            return redirect('posts-home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'register.html', {'form': form})

