from recipes.views import index, food, recipe
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^recipe/$', recipe, name='recipe'),
    # ex: /food/
    url(r'^food/(?P<food_id>[0-9]+)/$', food, name='food'),
]