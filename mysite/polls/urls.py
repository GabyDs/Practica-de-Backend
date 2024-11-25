from django.urls import path

from . import views

urlpatterns = [
    # /polls/
    path("", views.index, name="index"),
    # ej: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ej: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ej: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
]