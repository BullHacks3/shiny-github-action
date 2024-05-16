from django.conf.urls import url
import pickle


def unsaferr(pickled):
    return pickle.loads(pickled)


urlpatterns = [
    url(r'^(?P<object>.*)$', unsaferr)
]

urlpatternss = [
    url(r'^(?P<object>.*)$', unsaferr)
]
