""" Production Settings """
from .stage import *


# Set to your Domain here
ALLOWED_HOSTS = [
    "justforfam.com",
    "www.justforfam.com",
]
# The ALB uses the IP while calling the health check endpoint
if os.environ.get("AWS_EXECUTION_ENV"):
    ALLOWED_HOSTS.append(gethostbyname(gethostname()))
