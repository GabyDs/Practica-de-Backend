from django.http import HttpResponse, Http404

from django.shortcuts import render, get_object_or_404

from .models import Question

# Muestra las ultimas 5 preguntas de la encuesta
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
        
    context = {
        "latest_question_list": latest_question_list,
    }

    # La función render() toma el objeto de la solicitud como su primer argumento,
    # un nombre de plantilla como su segundo argumento y un diccionario como su tercer argumento opcional.
    # La función devuelve un objeto HttpResponse de la plantilla que se ha proporcionado representada con el contexto dado
    return render(request, "polls/index.html", context)

# muestra un texto de pregunta sin resultados, pero con un formulario para votar.
def detail(request, question_id):

    # try:
    #     # Si existe un question con determinado id
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # Lo mismo que el try anterior
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})

# muestra los resultados de una pregunta en particular.
def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

# gestiona la votación para una elección concreta en una pregunta específica.
def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")