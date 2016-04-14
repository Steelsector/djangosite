from django.views.generic import ListView

from firstapp.forms import Contact
from firstapp.models import Skill

from firstapp.models import Projects


class Home(ListView):
    template_name = 'index.html'
    model = Skill

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['projects'] = Projects.objects.all()
        context['contact_form'] = Contact()
        return context
