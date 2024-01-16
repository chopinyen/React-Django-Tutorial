from django.db import models
import string
import random

# Create your models here.

# In Django, a model is a class that is used to contain essential fields and methods. 
# Each model maps to a single table in the database.

# we want random codes for our rooms, so we will use the random module
def generate_unique_code():
    length = 6

    while True:
        # generate a random code
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # check if the code is unique
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    # rules for Django is to have fat models and thin code
