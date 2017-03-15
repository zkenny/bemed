from django.http import HttpResponse
from django.shortcuts import render

from .ec_forms import ECForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'index.html')

def ec_form(request):
    """
    View function for renewing a specific BookInstance by librarian
    """

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ECForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # If this is a GET (or any other method) create the default form.
    else:
        form = ECForm()

    return render(request, 'ec_forms.html', {'form': form, 'bookinst':book_inst})

def signup(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(str(user_form.errors) + " " + str(profile_form.errors))
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
            'users/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
