from django.http import HttpResponse

def raiz(request):
    return HttpResponse("<!DOCTYPE html>\
<html>\
    <head>\
        <style>\
            html, body, form {\
                height: 100%;\
                margin: 3px;\
                padding: 3px;\
                overflow: hidden;\
                font-family: Arial, Helvetica, sans-serif\
            }\
            h1, a {\
                color: #A3C932;\
            }\
            p {\
                font-size: large;\
            }\
        </style>\
    </head>\
    <title>Lexicon Soluções</title>\
    <body>\
        <h1>Lexicon Soluções</h1>\
        <p><a href='/projetos/'>Projetos</a></p>\
        <p><a href='/admin/'>Administração</a></p>\
    </body>\
</html>")