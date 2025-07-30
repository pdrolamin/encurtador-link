import random
import string
from django.db import models

def gerar_codigo_aleatorio (tamanho=5):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=tamanho))

class Link(models.Model):
    url_original = models.URLField()
    url_encurtado = models.CharField(max_length=8, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.url_encurtado:
            novo_codigo = gerar_codigo_aleatorio()
            while Link.objects.filter(url_encurtado=novo_codigo).exists():
                novo_codigo = gerar_codigo_aleatorio()
            self.url_encurtado = novo_codigo
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.url_encurtado
    