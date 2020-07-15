from django.http import JsonResponse
from django.shortcuts import render

from ..forms.contact import Contact

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Contact(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return JsonResponse({'success': True})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Contact()

    return render(request, 'rus_app/contact.html', {'form': form})
