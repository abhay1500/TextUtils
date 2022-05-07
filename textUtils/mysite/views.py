from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("hello world")
    #test={'name':'Abhay','place':'bangalore'}
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def analyse(request):
    #get the text
    t=request.POST.get('text','No Input')
    c=request.POST.get('punc','OFF')
    capitalise=request.POST.get('capitalise','OFF')
    lowercase=request.POST.get('lowercase','OFF')
    newlineremover=request.POST.get('newlineremover','OFF')
    extraspaceremover=request.POST.get('extraspaceremover','OFF')
    
    print(t)
    print(c)
    #analyse the text
    if c =="on":
        punctuations='''/[-[\]}()*+';{:"?.,%^$<>|#\]/,"$&'''
        analysed=""
        for char in t:
            if char not in punctuations:
                analysed=analysed +char
            
        puc={'val':'Punctuations Removed Successfully','analysed_text':analysed}
        t=analysed
        #return render(request,'analyse.html',puc)
    if(capitalise=='on'):
        analysed=""
        for char in t:
            analysed=analysed+char.upper()
            
        puc={'val':'Text capitalised Successfully','analysed_text':analysed}
        t=analysed
        #return render(request,'analyse.html',puc)
    
    if(lowercase=='on'):
        if t==t.upper():
            analysed=""
            for char in t:
                analysed=analysed+char.lower()
            puc={'val':'Text converted to Lower case Successfully','analysed_text':analysed}
            t=analysed
            #return render(request,'analyse.html',puc)
        else:
            t=analysed
            return HttpResponse("<h2><b>Upper case input only.</b></h2>")
    if(newlineremover=='on'):
        analysed=""
        for char in t:
            if char!="\n" and char!="\r":
                analysed=analysed+char
        puc={'val':'newlines removed Successfully','analysed_text':analysed}
        t=analysed
        #return render(request,'analyse.html',puc)        
    if(extraspaceremover=='on'):
        analysed=""
        for index,char in enumerate(t):
            if  index+1<len(t) and not(t[index]==" " and t[index+1]==" "):
                analysed=analysed+char
        puc={'val':'Extra spaces removed Successfully','analysed_text':analysed}
        t=analysed
        #return render(request,'analyse.html',puc)             
    if(c!="on" and capitalise!="on" and lowercase!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Error")
    return render(request,'analyse.html',puc)
    
"""def about(request):
    return HttpResponse('''<h2>Data Structures</h2> <a href="https://www.youtube.com/watch?v=yZf7XqFYU24&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l">click here to learn</a>''')
def abhay(request):
    return HttpResponse('''<h2>my website</h2><a href="https://github.com/abhay1500">click here to see</a>''')"""
