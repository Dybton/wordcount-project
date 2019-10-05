from django.http import HttpResponse
from django.shortcuts import render
# we need this in order to direct the views to templates
import operator
# we need to import this, to use for sorting


def homepage(request):
    return render(request, 'home.html', {'yo': 'wassup'})
    # here we send back the request (cookies etc) and
    # send them to the html


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    # here we pass on the key: fulltext which we defined in home.html
    # the value we can see is fulltext - this is is the value
    #
    wordlist = fulltext.split()

    worddictionary = {}
    # Don't undetstand how we can just create this?
    # by setting it equal we tell it, that its now a dictionary

    for word in wordlist:
        if word in worddictionary:
            # increase the number
            worddictionary[word] += 1
        else:
            # add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(),
                         key=operator.itemgetter(1), reverse=True)
    # Q: WHat does the items method do? A: Convert dict into list
    # after items, inside the sorted funcion we specify how we want the list sorted

    # items() turns the value into a list
    return render(request, 'count.html', {'fulltext': 'fulltext', 'count': len(wordlist), 'sortedwords': sortedwords})
    # Q:  What does the split method do?
    # A: Makes a string into a list

    # in the return, we decides what we return to user, given request
