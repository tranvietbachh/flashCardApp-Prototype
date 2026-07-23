SECRET_KEY = "yorushika"
from database.database import query_db
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

get_due_cards()