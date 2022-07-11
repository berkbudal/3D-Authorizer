from math import ceil
import random
import string
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse
from .models import Human
from django.views import generic

def buildContext(session):
    session_values = {}
    if session:
        session_values = {
            "name": session.get('name', ""),
            "robot_name": session.get('robot_name', ""),
            "correct_answer_2": session.get('correct_answer_2', ""),
            "gender": session.get('gender', "") ,
            "birth_year": session.get('birth_year', None),
            "pet": session.get('pet', None),
            "city": session.get('city', ""),
            "hair_color": session.get('hair_color', ""),
            "height": session.get('height', ""),
            #
        }
    return {**session_values}


def get_robot_name(human_name):
    # choose from all lowercase, digits and punctuations
    # lowercase and punctuation are doubled so they have more probabilities than numbers
    phi = (1 + 5 ** 0.5) / 2

    length = ceil(len(human_name)*phi) # a robot name longer than a human name by the golden ratio. no one knows exactly why.
    letters = string.ascii_lowercase + string.ascii_lowercase + string.punctuation + string.punctuation + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def index(request):
    return render(request, 'index.html')

def step1(request):
    
    if request.method == 'POST':
        if request.POST.get('name').strip(): # name was provided
            #save name and generate a robot name
            request.session['name'] = request.POST.get('name')
            request.session['robot_name'] = get_robot_name(request.POST.get('name'))
            # go to step 2
            return HttpResponseRedirect(reverse('step2'))
    return render(request, 'steps/step1.html',context=buildContext(request.session))

def step2(request):
    answers = { 
        'answers': {
        'a': 'Duck',
        'b': 'Couch',
        'c': 'Earth',
        'd': 'Thrashbin',
        }
    }
    correct_answer = 'd'
    ctx = {**answers, **buildContext(request.session)}

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        ctx = {**ctx, **{'selected_answer' : selected_answer}} ## store the selected answer in the context
        if selected_answer == correct_answer:
            request.session['correct_answer_2'] = True
            return HttpResponseRedirect(reverse('step3'))
    return render(request, 'steps/step2.html',context=ctx)
    # return render(request, 'steps/step2.html',context=buildContext(request.session))

def step3(request):
    answers = {
        'answers': {
        'a': '11',
        'b': '1',
        'c': '7',
        'd': '19',
        }
    }
    correct_answer = 'a'
    ctx = {**answers, **buildContext(request.session)}

    if request.method == 'POST':
        gender = request.POST.get('gender').strip()
        selected_answer = request.POST.get('answer')
        ctx = {**ctx, **{'selected_answer' : selected_answer, 'gender': gender}} ## store the selected answer in the context
        if gender and selected_answer == correct_answer: # correct answer given.
            # store the value in the session and redirect 
            request.session['gender'] = gender
            return HttpResponseRedirect(reverse('step4'))
    return render(request, 'steps/step3.html',context=ctx)

def step4(request):
    answers = {
        'answers': {
        'a': 'Sphere',
        'b': 'Torus',
        'c': 'Pill',
        'd': 'Pyramid',
        }
    }
    correct_answer = 'd'
    ctx = {**answers, **buildContext(request.session)}

    if request.method == 'POST':
        birth_year = request.POST.get('birth_year').strip()
        selected_answer = request.POST.get('answer')
        ctx = {**ctx, **{'selected_answer' : selected_answer, 'birth_year': birth_year}} ## store the selected answer in the context
        if birth_year and selected_answer == correct_answer: # correct answer given.
            # store the value in the session and redirect 
            request.session['birth_year'] = birth_year
            return HttpResponseRedirect(reverse('step5'))
    return render(request, 'steps/step4.html',context=ctx)

def step5(request):
  
    ctx = {**buildContext(request.session)}

    if request.method == 'POST':    
        request.session['pet'] = True
        return HttpResponseRedirect(reverse('step6'))
    return render(request, 'steps/step5.html',context=ctx)
    # return render(request, 'steps/step5.html',context=buildContext(request.session))

def step6(request):
    answers = {
        'answers': {
        'a': '6',
        'b': '7',
        'c': '8',
        'd': '9',
        }
    }
    correct_answer = 'c'
    ctx = {**answers, **buildContext(request.session)}

    if request.method == 'POST':
        city = request.POST.get('city').strip()
        selected_answer = request.POST.get('answer')
        ctx = {**ctx, **{'selected_answer' : selected_answer, 'city': city}} ## store the selected answer in the context
        if city and selected_answer == correct_answer: # correct answer given.
            # store the value in the session and redirect 
            request.session['city'] = city
            return HttpResponseRedirect(reverse('step7'))
    return render(request, 'steps/step6.html',context=ctx)

def step7(request):
    answers = {
        'answers': {
        'a': 'Mountain',
        'b': 'Crab',
        'c': 'Chair',
        'd': 'Face',
        }
    }
    correct_answer = 'd'
    ctx = {**answers, **buildContext(request.session)}

    if request.method == 'POST':
        hair_color = request.POST.get('hair_color').strip()
        selected_answer = request.POST.get('answer')
        ctx = {**ctx, **{'selected_answer' : selected_answer, 'hair_color': hair_color}} ## store the selected answer in the context
        if hair_color and selected_answer == correct_answer: # correct answer given.
            # store the value in the session and redirect 
            request.session['hair_color'] = hair_color
            return HttpResponseRedirect(reverse('step8'))
    return render(request, 'steps/step7.html',context=ctx)

def step8(request):
    answers = {
        'answers': {
        'a': 'A5',
        'b': 'E3',
        'c': 'X0',
        'd': 'TT',
        }
    }
    correct_answer = 'b'
    ctx = {**answers, **buildContext(request.session)}

    if request.method == 'POST':
        height = request.POST.get('height')
        selected_answer = request.POST.get('answer')
        ctx = {**ctx, **{'selected_answer' : selected_answer, 'height': height}} ## store the selected answer in the context
        if selected_answer == correct_answer: # correct answer given.
            #create the human
            request.session['height'] = height
            Human.create(request.session)
            return HttpResponseRedirect(reverse('step9'))
    return render(request, 'steps/step8.html',context=ctx)

def step9(request):
    sesh_copy = {**request.session}
    #clear the session info except for the robot name (this is used to know which profile is yours)
    for key in sesh_copy:
        if key != 'robot_name' and key!= 'name':
            del request.session[key]
    return render(request, 'steps/step9.html', context=buildContext(request.session))

class HumanListView(generic.ListView):
    model = Human
    template_name = 'humans_list.html'
    queryset: Human.objects.order_by('created_at')
    
    def get_context_data(self, **kwargs):
        context = super(HumanListView, self).get_context_data(**kwargs)
        context['robot_name'] = self.request.session.get('robot_name')
        return context
