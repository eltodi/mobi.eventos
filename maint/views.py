# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from utils.decorators import render_with
from maint.models import *
from datetime import timedelta
import datetime
import tweepy

@render_with("home.html")
def home(request):
	api = tweepy.API()
	tws = api.search("xcongresouim")[:20]

	ahora = datetime.datetime.now() - timedelta(hours = +2)
	return {"tws":tws,"ahora":ahora}


@render_with("agenda.html")
def agenda(request):
	ahora = datetime.datetime.now()

	oAgenda = Ponencia.objects.filter(fecha__gte=ahora).order_by("fecha")

	return {"oAgenda":oAgenda}

@render_with("ponentes.html")
def ponentes(request):
	oPonentes = Ponente.objects.all().order_by("nombre")

	return {"oPonentes":oPonentes}


@render_with("ponente.html")
def ponente(request, id):
	oPonente = Ponente.objects.get(id=id)
	oPonencias = Ponencia.objects.filter(ponente = oPonente).order_by("fecha")
	return {"oPonente":oPonente,"oPonencias":oPonencias}


@render_with("feria.html")
def feria(request):
	oStand = Stand.objects.all().order_by("nombre")

	return {"oStand":oStand}


@render_with("stand.html")
def stand(request, id):
	oStand = Stand.objects.get(id = id)

	return {"oStand":oStand}


