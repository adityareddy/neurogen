from django.shortcuts import render
from django.http import HttpResponseRedirect
from nemo.forms import SearchForm
from nemo.main import getResults

import json

def results(request):
    return render(request, 'nemo/index.html', {'poll': 'poll'})
    
def search(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            search_str = form.cleaned_data['search_str']
            results_unparsed = getResults(search_str)
            results = results_unparsed
            #for result in results_unparsed["results"]["bindings"]:
            #    results.add(result["x1"]["value"])
        else:
            search_str = 'Did not Search'
            results = 'No Results'
    else:
        form = SearchForm() # An unbound form
        search_str = 'Did not Search'
        results = 'No Results'
        

    return render(request, 'nemo/index.html', {
        'form': form, 'search_str': search_str, 'results' : results
    })