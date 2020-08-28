from models import Business
import os
from django.conf import settings
b = Business(name='A business', password = 'asdf')
b.save()
