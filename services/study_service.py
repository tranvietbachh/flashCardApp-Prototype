from services.card_service import get_cards
from database.database import query_db

def get_study_cards(deck_id):
    return get_cards(deck_id)

def get_due_cards():
    cards = query_db("""
        SELECT
            cards.*,
            decks.name AS deck_name
        FROM cards
        JOIN decks
            ON cards.deck_id = decks.id
        WHERE due_date <= DATE('now')
        ORDER BY due_date, english
    """)

    print(cards)
    print(len(cards))

    return cards