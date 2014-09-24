""" Contains settings specific to django social auth.
"""

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
)

# Linkedin API credentials
LINKEDIN_CONSUMER_KEY = '75euedwzmorpoc'
LINKEDIN_CONSUMER_SECRET = '2qW84TyWVpcTHpBv'
