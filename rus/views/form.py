from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from ..forms.contact import Contact

from django.views.decorators.csrf import csrf_exempt

from ..models import FormContact


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
            FormContact.objects.create(name=form.data['anti_name'], email=form.data['anti_email'],
                                       subject=form.data['anti_subject'],
                                       message=form.data['anti_message'])

            rendered = render_to_string('rus/thank.html')
            return HttpResponse(rendered)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Contact()

    # rendered = render_to_string('rus/contact.html', context={'form': form})
    # return HttpResponse(rendered)
    return render(request, 'rus/contact.html', {'form': form})
