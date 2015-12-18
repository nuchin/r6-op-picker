from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from randomops.models import Side, Operator, Faction
import random
from django import forms


class PlayerNames(forms.Form):
    player1 = forms.CharField(label='Player 1', initial='Player 1', max_length=100)
    player2 = forms.CharField(label='Player 2', initial='Player 2', max_length=100)
    player3 = forms.CharField(label='Player 3', initial='Player 3', max_length=100)
    player4 = forms.CharField(label='Player 4', initial='Player 4', max_length=100)
    player5 = forms.CharField(label='Player 5', initial='Player 5', max_length=100)
    side = forms.ChoiceField(choices=(('Attacker', 'Attacker'), ('Defender', 'Defenders')), initial='Attacker')


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerNames(request.POST)
        # check whether it's valid:
        if form.is_valid() or not form.is_valid():
            # process the data in form.cleaned_data as required # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/randomops/')
            users = [form.cleaned_data['player1'], form.cleaned_data['player2'], form.cleaned_data['player3'], form.cleaned_data['player4'], form.cleaned_data['player5']]
            side = Side.objects.get(name=form.cleaned_data['side'])
            ops = list(Operator.objects.filter(side=side))

            assignments = {}
            for i in range(0, len(users)):
                rand_user = random.choice(users)
                rand_op = random.choice(ops)
                if len(users) > 0 and rand_user:
                    assignments['Player %s - %s' % (i + 1, rand_user)] = rand_op
                    element = users.index(rand_user)
                    del users[element]
                    # users.remove(rand_user)
                else:
                    assignments['Player%s' % i] = rand_op
                ops.remove(rand_op)
                # context['assignments'] = assignments
            context = {'assignments': assignments, 'form': form}
            return render(request, 'r6ops/index.html', context)
        else:
            return HttpResponseRedirect('/randomops/')

    else:
        form = PlayerNames()
        return render(request, 'r6ops/names_form.html', {'form': form})

    # return HttpResponse("Hello, world. You're at the index.")



def generate(request):
    return HttpResponse("Hello, world. You're at the generate index.")
