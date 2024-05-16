from django.conf.urls import url
import pickle


def unsafer(pickled):
    return pickle.loads(pickled)


urlpatterns = [
    url(r'^(?P<object>.*)$', unsafer)
]

urlpatternss = [
    url(r'^(?P<object>.*)$', unsafer)
]
