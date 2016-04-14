from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from firstapp.models import Skill


class FirstAppTestCases(TestCase):
    def setUp(self):
        self.client = Client()

    def test_skill_model(self):
        skill = Skill.objects.create(name='Test Skill', rate=88)
        self.assertEqual(skill.__unicode__(), '%s (%s)' % (skill.name, skill.rate))

    def test_home(self):
        skill = Skill.objects.create(name='Test Skill', rate=88)
        r = self.client.get(reverse('index'))
        self.assertContains(r, 'contacter_name')
        self.assertContains(r, 'contacter_message')
        self.assertContains(r, 'contacter_mail')
        self.assertContains(r, skill.name)
        self.assertContains(r, skill.rate)

    def test_contact_form(self):
        r = self.client.post(reverse('contact'), data={
            'contacter_name': 'Test User',
            'contacter_message': 'Test message',
            'contacter_mail': 'test',
        })
        self.assertContains(r, 'Enter a valid email address.')

        self.client.post(reverse('contact'), data={
            'contacter_name': 'Test User',
            'contacter_message': 'Test message',
            'contacter_mail': 'test@mail.com',
        })
