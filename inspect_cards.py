import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from cards.models import Card, Company

print('Companies:')
for c in Company.objects.all():
    print(c.id, c.name)

print('\nCards:')
for card in Card.objects.select_related('company').all():
    print(card.id, card.name, card.grade, card.company.name)
