from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from cpmeye.models import Submission
from cpmeye.forms import SubmissionForm
from cpmeye.forms import UserForm

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required    
def get_submission_list(starts_with=''):
        submission_list = []
        if starts_with:
                submission_list = Submission.objects.filter(name__istartswith=starts_with)
        else:
                submission_list = Submission.objects.all()
      
def suggest_submission(request):
        context = RequestContext(request)
        submission_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['suggestion']

        submission_list = get_submission_list(8, starts_with)

        return render_to_response('cpmeye/submission_list.html', {'sw':starts_with,'cat_list': cat_list }, context)

from cpmeye.forms import VotingForm
      
def index(request):
    context = RequestContext(request)

    submission_list = Submission.objects.order_by('-chancounter') #we may remove this if we are gonna sort it by category
    
    # Render the response and return to the client.

     #if request.method == 'POST':
      #form = VotingForm(data=request.POST)
      #sub = Submission.objects.get(pk = subid)
      #sub.chancounter -= 1
      #sub.save()
      #return render_to_response('index.html', {'submission_list':submission_list}, context)
    
    #else:
    return render_to_response('index.html', {'submission_list':submission_list}, context)

from cpmeye.forms import SubmissionForm

@login_required
def add_submission(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = SubmissionForm(data=request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/cpmeye/')
        else:
            print form.errors
    else:
        form = SubmissionForm()

    return render_to_response( 'add_submission.html',
            {'form': form},
             context)
  
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered},
            context)


from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse  

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/cpmeye/')
            else:
                return HttpResponse("Your CPMeye account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/cpmeye/')
  
@login_required
def voteup(request, submissionID):
    sub = get_object_or_404(Submission, pk = submissionID)
    sub.chancounter += 1
    sub.save()
  
    return HttpResponseRedirect('/cpmeye/')

@login_required
def votedown(request):
    sub = request.GET("submission.id")
    sub.chancounter -= 1
    sub.save()