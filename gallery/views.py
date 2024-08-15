from django.shortcuts import render

def index(request):
  dados = {
  1: {"name": "Nebulosa de Carina",
      "subtitle": "webbtelescope.org / NASA / James Webb"
      },
  2: {"name": "Galáxia NGC 1079",
      "subtitle": "nasa.org / NASA / Hubble"
      }
}
  return render(request,'gallery/index.html', {"cards": dados})

def imagem(request):
  return render(request, 'gallery/imagem.html')