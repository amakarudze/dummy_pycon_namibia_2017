from django.test import TestCase, RequestFactory
from django.core import mail
from django.contrib.auth.models import User, AnonymousUser

from .models import Entry
from .views import home


class TestViews(TestCase):
    # Test homepage rendering
    def test_home(self):
        response = self.client.get("")
        self.assertEquals(response.status_code, 200)


class TestModel(TestCase):
    # Test string representation of model in admin
    def test_string_representation(self):
        entry = Entry(title="test entry")
        self.assertEqual(str(entry), entry.title)

    # Test model plural in admin
    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")
        self.assertNotEqual((Entry._meta.verbose_name_plural), "entrys")


class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
                       'Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       fail_silently=False,
                      )
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", email="test@test.com", password="pass1234")

    def test_login_success(self):
        response = self.client.login(username="test_user", password="pass1234")
        self.assertTrue(response)


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
                                             username='jacob', email='jacob@test.com', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /
        response = home(request)
        self.assertEqual(response.status_code, 200)