from recipes.views import index, food
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index, name='index'),
    # ex: /food/
    url(r'^food/(?P<food_id>[0-9]+)/$', food, name='food'),
]