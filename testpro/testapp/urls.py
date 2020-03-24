from django.conf.urls import url
from.views import OneEndPoint
urlpatterns=[
    url(r"^singleurl/$",OneEndPoint.as_view()),
]