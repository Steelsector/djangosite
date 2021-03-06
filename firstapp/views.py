# coding=utf-8
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import ListView, FormView, DetailView
from django.core.mail import EmailMultiAlternatives
from firstapp.forms import Contact
from firstapp.models import Skill
from django_slack import slack_message
from firstapp.models import Project


class Home(ListView):
    template_name = 'index.html'
    model = Skill

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['form'] = Contact(self.request.POST or None)
        return context


class ProjectDetail(DetailView):
    template_name = 'project.html'
    model = Project


class ContactMe(FormView):
    form_class = Contact
    success_url = reverse_lazy('index')
    template_name = 'index.html'

    def form_valid(self, form):

        slack_message('my_message.slack', {
            'message': form.cleaned_data.get('contacter_message'),
            'name': form.cleaned_data.get('contacter_name'),
            'mail': form.cleaned_data.get('contacter_mail')
        })

        return super(ContactMe, self).form_valid(form)
