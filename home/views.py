from django.conf import settings

from django.http import HttpResponse


def acme_challenge(request, challenge):
    """
    Returns the the code requested by Lets Encrypt, to prove ownership
    of a domain.
    """
    lets_encrypt_string = settings.LETS_ENCRYPT_STRING
    challenge_response = "{}.{}".format(challenge, lets_encrypt_string)

    return HttpResponse(challenge_response)
