from django.urls import path

from bboard.views import *

urlpatterns = [
    path('', index),

    path('html/', index_html, name='index_html'),

    path('<int:rubric_id>/', by_rubric, name='by_rubric'),

    path('add/', BbCreateView.as_view(), name='add')

]
