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
    return render(request, 'signup.html')
