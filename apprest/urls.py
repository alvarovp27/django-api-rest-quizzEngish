from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Usuario, WordTranslationsList, WordTranslationsFromEnglish, WordTranslationUpdateDelete
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    url(r'^api/words/$', WordTranslationsList.as_view()),
    url(r'^api/words/(?P<wordEN>.*)/(?P<typeEN>.*)/(?P<wordSP>.*)/(?P<typeSP>.*)/(?P<category>.*)/$', WordTranslationUpdateDelete.as_view()),
    url(r'^api/words/(?P<wordEN>.*)/$', WordTranslationsFromEnglish.as_view()),
	url(r'^api/token-auth/$', obtain_auth_token),
	url(r'^api/users/$', Usuario.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)