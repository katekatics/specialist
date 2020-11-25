from django.http import HttpResponse, HttpRequest


def homePageView(request: HttpRequest):
    """
    Функция, которая будет отображать Hello world!
    на веб странице.
    """
    return HttpResponse("<h1>Hello world!<h1>")
