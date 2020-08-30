from django.test import TestCase
from django.urls import reverse

from .models import *


def create_cv():
    Details(name='someone', number='123', address='somewhere', email="me@example.com").save()
    Link(text='google', url='http://goo.gle').save()
    Link(text='facebook', url='http://fb.com').save()
    School(name='uni', time='now', subject='cs', grade='first').save()
    School(name='highschool', time='before', subject='stuff', grade='A**').save()
    Work(name='procrastination', time='all the time', position='ceo', description='nothing', experience='scrolling\nclicking').save()
    Achievement(time='rn', description='i wrote some tests for a django app').save()


class CVIndexTests(TestCase):
    def test_correct_template(self):
        create_cv()
        response = self.client.get(reverse('cv:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv/index.html')

    def test_cv_displayed(self):
        create_cv()
        response = self.client.get(reverse('cv:index'))
        self.assertEqual(response.context['details'], Details.objects.first())
        self.assertEqual(response.context['links'].first(), Link.objects.first())
        self.assertEqual(response.context['links'][1], Link.objects.all()[1])
        self.assertEqual(response.context['education'].first(), School.objects.first())
        self.assertEqual(response.context['education'][1], School.objects.all()[1])
        self.assertEqual(response.context['career'].first(), Work.objects.first())
        self.assertEqual(response.context['achievements'].first(), Achievement.objects.first())


class CVEditTests(TestCase):
    def test_exists_form(self):
        response = self.client.get('/admincv/')
        self.assertNotEqual(response.status_code, 404)
