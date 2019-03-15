from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import *
from app_question import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# router.register(r'type',question_typeList,  base_name='topic-list')
# router.register(r'type/(?P<pk>[0-9]+)', question_typeUpdate)
# router.register(r'topic', question_topicList)
# router.register(r'addquestion',Add_questionViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^type/',views.question_typeList, name='type-list'),
    url(r'^typeid/(?P<pk>[0-9]+)/',views.question_typeUpdate, name='type-update'),
    url(r'^topic/',views.question_topicList, name='topic-list'),
    url(r'^topicid/(?P<pk>[0-9]+)/',views.question_topicUpdate, name='topic-update'),
    url(r'^complexity/',views.question_complexList, name='complex-list'),
    url(r'^complexityid/(?P<pk>[0-9]+)/',views.question_complexUpdate, name='complex-update'),
    url(r'^addquestion/',views.add_questionList, name='addquestion-list'),
    url(r'^addquestionid/(?P<pk>[0-9]+)/',views.add_questionUpdate, name='addquestion-update')

]