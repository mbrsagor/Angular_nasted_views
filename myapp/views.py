from django.http import HttpResponse


def welcome(request):

    NAME = "Sagor"
    # Django template work look like this::-
    HTML_STRING = f"""
    <h1>Welcome to our website</h1>
    <p>This is {NAME}
    """
    return HttpResponse(HTML_STRING)
