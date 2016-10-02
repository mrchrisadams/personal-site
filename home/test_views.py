from django.test import Client
from django.conf import settings
import pytest

@pytest.mark.django_db
def test_challenge():

    c = Client()

    lets_encrypt_string = settings.LETS_ENCRYPT_STRING
    challenge_string = "somenonce"
    lets_encrypt_response = "{}.{}".format(challenge_string, lets_encrypt_string)

    res = c.get('/.well-known/acme-challenge/{}'.format(challenge_string))

    assert(res.status_code == 200)
    assert(res.content == bytes(lets_encrypt_response, 'utf8'))
