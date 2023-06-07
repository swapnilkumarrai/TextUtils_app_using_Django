# I have created this file - Swapnil Kumar Rai
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpose = ''
    if removepunc=="on":
        analyzed = ""
        punctuations = '''.,?!;:\"'()[]{}...-—/\\&*#$%@+-=<>_|~•#'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        djtext = analyzed
        if len(purpose)>0:
            purpose = purpose + ", Removed Punctutaions"
        else:
            purpose = purpose + "Removed Punctutaions"
    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        if len(purpose)>0:
            purpose = purpose + ", Capitalized"
        else:
            purpose = purpose + "Capitalized"
    if newlineremover=='on':
        analyzed = ''
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        djtext = analyzed
        if len(purpose)>0:
            purpose = purpose + ", New Line Removed"
        else:
            purpose = purpose + "New Line Removed"
    if extraspaceremover=='on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if index<len(djtext)-1:
                if not (djtext[index]==' ' and djtext[index+1]==' '):
                    analyzed = analyzed + char
            else:
                analyzed = analyzed + char
        djtext = analyzed
        if len(purpose)>0:
            purpose = purpose + ", Removed ExtraSpace"
        else:
            purpose = purpose + "Removed ExtraSpace"
    if removepunc!="on" and fullcaps != 'on' and newlineremover!='on' and extraspaceremover!='on' and len(djtext)>0:
        # return HttpResponse("Please choose atleast one option")
        return render(request, 'analyze.html', {'purpose':'', 'analyzed_text':"Please choose atleast one option"})
    if len(djtext)==0:
        return render(request, 'analyze.html', {'purpose':'', 'analyzed_text':"You did'nt gave any text"})
    
    params = {'purpose':purpose, 'analyzed_text':djtext}
    return render(request, 'analyze.html', params)

# def newlineremove(request):
#     return HttpResponse("new line removet")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def spaceremove(request):
#     return HttpResponse("space remove")

# def charcount(request):
#     return HttpResponse("charcount")
