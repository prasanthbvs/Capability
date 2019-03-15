from django.conf.urls import url, include
from rest_framework import routers
from .api import AnswerquestionViewSet

router = routers.DefaultRouter()
router.register(r'questionanswer', AnswerquestionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]