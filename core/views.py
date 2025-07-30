import random
import string
from django.shortcuts import render, redirect
from .models import Link
from .forms import FormLinks
from django.http import HttpResponseRedirect, Http404

def gerar_codigo_aleatorio(tamanho=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

def home(request):
    form = FormLinks()
    return render(request, 'home.html', {'form': form})

def valida_link(request):
    if request.method == 'POST':
        form = FormLinks(request.POST)
        if form.is_valid():
            url_original = form.cleaned_data['url_original']

           
            while True:
                codigo = gerar_codigo_aleatorio()
                if not Link.objects.filter(url_encurtado=codigo).exists():
                    break

            link = Link(url_original=url_original, url_encurtado=codigo)
            link.save()
            return render(request, 'home.html', {
                'form': FormLinks(), 
                'link_gerado': codigo  
            })
        else:
            return render(request, 'home.html', {
                'form': form,
                'erro': True
            })
    return redirect('/')

def redirecionar(request, codigo):
    try:
        link = Link.objects.get(url_encurtado=codigo)
        return HttpResponseRedirect(link.url_original)
    except Link.DoesNotExist:
        raise Http404("Esse link encurtado não existe!")
        