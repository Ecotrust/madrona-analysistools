from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<uid>[\w_]+)/progress.json$', 'progress', name='analysis-progress'),
    url(r'^(?P<uid>[\w_]+)/progress.html$', 'progress_html', name='analysis-html-progress'),
]
