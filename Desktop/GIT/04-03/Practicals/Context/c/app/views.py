from django.views.generic.base import TemplateView
from .models import MyModel
class Intro(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = super(Intro, self).get_context_data(*args, **kwargs)
        context['users'] = MyModel.objects.all()
        return context