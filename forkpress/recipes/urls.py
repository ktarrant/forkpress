import recipes.views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', recipes.views.index, name='index'),
]