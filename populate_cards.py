import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from cards.models import Card, Company

# Crear o obtener companies
companies_data = [
    {'name': 'Pokémon'},
    {'name': 'Yu-Gi-Oh'},
    {'name': 'Magic: The Gathering'},
    {'name': 'One Piece'},
]

companies = {}
for comp_data in companies_data:
    company, created = Company.objects.get_or_create(name=comp_data['name'])
    companies[comp_data['name']] = company

# Datos de tarjetas populares/más vendidas
cards_data = [
    # Pokémon
    {'name': 'Charizard Base Set', 'grade': 10, 'company': 'Pokémon'},
    {'name': 'Black Lotus Alpha', 'grade': 9, 'company': 'Pokémon'},
    {'name': 'Mewtwo Base Set', 'grade': 9, 'company': 'Pokémon'},
    {'name': 'Pikachu Illustrator', 'grade': 10, 'company': 'Pokémon'},
    {'name': 'Blastoise Base Set', 'grade': 8, 'company': 'Pokémon'},
    
    # Yu-Gi-Oh
    {'name': 'Blue-Eyes White Dragon', 'grade': 10, 'company': 'Yu-Gi-Oh'},
    {'name': 'Dark Magician', 'grade': 9, 'company': 'Yu-Gi-Oh'},
    {'name': 'Exodia the Forbidden One', 'grade': 9, 'company': 'Yu-Gi-Oh'},
    {'name': 'Red-Eyes Black Dragon', 'grade': 8, 'company': 'Yu-Gi-Oh'},
    {'name': 'Swordsoul Grandmaster', 'grade': 8, 'company': 'Yu-Gi-Oh'},
    
    # Magic: The Gathering
    {'name': 'Black Lotus', 'grade': 10, 'company': 'Magic: The Gathering'},
    {'name': 'Time Walk', 'grade': 9, 'company': 'Magic: The Gathering'},
    {'name': 'Ancestral Recall', 'grade': 9, 'company': 'Magic: The Gathering'},
    {'name': 'Jace, the Mind Sculptor', 'grade': 8, 'company': 'Magic: The Gathering'},
    {'name': 'Liliana of the Veil', 'grade': 8, 'company': 'Magic: The Gathering'},
    
    # One Piece
    {'name': 'Luffy Gear 5', 'grade': 10, 'company': 'One Piece'},
    {'name': 'Zoro King of Hell', 'grade': 9, 'company': 'One Piece'},
    {'name': 'Mihawk Warlord', 'grade': 9, 'company': 'One Piece'},
    {'name': 'Nami Navigator', 'grade': 8, 'company': 'One Piece'},
    {'name': 'Sanji Vinsmoke', 'grade': 8, 'company': 'One Piece'},
]

# Crear tarjetas
created_count = 0
for card_data in cards_data:
    card, created = Card.objects.get_or_create(
        name=card_data['name'],
        defaults={
            'grade': card_data['grade'],
            'company': companies[card_data['company']]
        }
    )
    if created:
        created_count += 1
        print(f"✓ Created: {card.name} ({card.grade}) - {card.company.name}")
    else:
        print(f"✗ Already exists: {card.name}")

print(f"\n✅ Total created: {created_count} cards")
