from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Card

# Create your views here.
def serialize_card(card):
    return {
        'id': card.id,
        'name': card.name,
        'grade': card.grade,
        'company': card.company.name
    }


def card_list(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    grade = request.GET.get('grade')
    company = request.GET.get('company')
    cards = Card.objects.select_related('company').all()
    if grade:
        cards = cards.filter(grade=grade)
    if company:
        cards = cards.filter(company__name=company.upper())
    data = []
    for card in cards:
        data.append(serialize_card(card))
    return JsonResponse(data, safe=False)


def get_card(request, card_id):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    card = get_object_or_404(Card, id=card_id)
    data = serialize_card(card)
    return JsonResponse(data, safe=False)