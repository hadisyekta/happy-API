import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from happyd1g1t.models import Happiness, Employee, Team
from happyd1g1t.serializers import HappinessSerializer


# Create your tests here.
class HappinessCreateViewTestCase(APITestCase):
    url = reverse("happyd1g1t:happiness-create")

    def setUp(self):
        self.username = "hadiseh"
        self.email = "hadis@d1g1t.com"
        self.password = "some-strong-password"
        
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.login(username=self.username, password=self.password)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_happiness_create_byuser_nonteam(self):
        happiness = {"happiness_level": 4}
        
        response = self.client.post(self.url,
                                json.dumps(happiness),
                                content_type="application/json")
        
        response_data = json.loads(response.content)
        self.assertEqual(403, response_data['status_code'])
        # self.assertEqual('You must be part of a team to insert level of your happiness.', response_data['errors'])

    def test_happiness_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=None)
        new_user = User.objects.create_user("newuser", "new@user.com", "some_strong_pass")
        team = Team.objects.create(name='TestTeam', is_active=True)
        employee = Employee.objects.create(user=new_user, team=team)
        new_user.employee = employee
        new_user.save()
        # new_token = Token.objects.create(user=new_user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        self.client.login(username='newuser', password='some_strong_pass')
        
        happiness = {"happiness_level": 4}
        
        response = self.client.post(self.url,
                                json.dumps(happiness),
                                content_type="application/json")

        response_data = json.loads(response.content)
        self.assertEqual(201, response_data['status_code'])
        
        # Test when user add another happiness in one day
        response = self.client.post(self.url,
                                json.dumps(happiness),
                                content_type="application/json")
        response_data = json.loads(response.content)
        self.assertEqual(400, response_data['status_code'])
        # self.assertEqual('Each employee can add her/his level of happiness once time a day!', response_data['errors']['non_field_errors'][0])

    def test_happiness_data_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=None)
        new_user = User.objects.create_user("newuser2", "new2@user.com", "some_strong_pass")
        team = Team.objects.create(name='TestTeam2', is_active=True)
        employee = Employee.objects.create(user=new_user, team=team)
        new_user.employee = employee
        new_user.save()
        # new_token = Token.objects.create(user=new_user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        
        self.client.login(username='newuser2', password='some_strong_pass')
        happiness = {"happiness_level": 4}
        response = self.client.post(self.url,
                                json.dumps(happiness),
                                content_type="application/json")

        response_data = json.loads(response.content)
        self.assertEqual(201, response_data['status_code'])



class HappinessReportViewTestCase(APITestCase):
    url = reverse("happyd1g1t:happiness-report")

    def setUp(self):
        self.username = "yekta"
        self.email = "yekta@d1g1t.com"
        self.password = "some-strong-password"
        
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.login(username=self.username, password=self.password)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_happiness_report_auth_noteam(self):
        response = self.client.get(self.url)
        response_data = json.loads(response.content)
        self.assertEqual(403, response_data['status_code'])
        # self.assertEqual("You must be part of a team to see the happiness report.", response_data['errors'])

    def test_happiness_report_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION=None)
        new_user = User.objects.create_user("newuser5", "new5@user.com", "some_strong_pass")
        team = Team.objects.create(name='TestTeam1', is_active=True)
        employee = Employee.objects.create(user=new_user, team=team)
        new_user.employee = employee
        new_user.save()
        # new_token = Token.objects.create(user=new_user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        self.client.login(username='newuser5', password='some_strong_pass')
        response = self.client.get(self.url)
        response_data = json.loads(response.content)
        self.assertEqual(200, response_data['status_code'])

    def test_happiness_report_unauth(self):
        self.client.logout()
        response = self.client.get(self.url)
        
        response_data = json.loads(response.content)
        self.assertIn('happiness_avg_allteam', response_data['data'])


   