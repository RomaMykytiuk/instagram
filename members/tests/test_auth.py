import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User=get_user_model()

@pytest.mark.django_db
def test_login_with_email(client):
    user = User.objects.create_user(email='test@gmail.com',username='test',password='1234')
    response = client.post(reverse('login'),{
        'username':'test@gmail.com',
        'password':'1234'
    })
    assert response.status_code==302
    assert response.url==reverse('profile')


