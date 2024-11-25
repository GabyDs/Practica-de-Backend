from django.db.models import F

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

from django.urls import reverse

# Muestra las ultimas 5 preguntas de la encuesta
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
        
    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request, "polls/index.html", context)

# muestra un texto de pregunta sin resultados, pero con un formulario para votar.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})

# muestra los resultados de una pregunta en particular.
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/results.html", {"question": question})

# gestiona la votación para una elección concreta en una pregunta específica.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # Siempre devuelve un HttpResponseRedirect después de tratar con éxito los datos POST.
        # Esto evita que los datos se publiquen dos veces si un usuario pulsa el botón Atrás.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
