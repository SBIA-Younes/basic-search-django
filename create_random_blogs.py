import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"searsh.settings")

import django
django.setup()

from faker import Faker
from blog.models import BlogPost


fake = Faker()

def create_random_blog():
    title = fake.sentence()
    content = fake.paragraphs(nb=3)
    BlogPost.objects.create(title=title, content=content)
    
for _ in range(50):
  create_random_blog()
  
print("50 blogs randmom created successfully")