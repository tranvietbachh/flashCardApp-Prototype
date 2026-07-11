from database.database import query_db, execute_db


def get_all_decks():
    return query_db("""
        SELECT
            decks.*,
            COUNT(cards.id) AS card_count
        FROM decks
        LEFT JOIN cards
            ON decks.id = cards.deck_id
        GROUP BY decks.id
        ORDER BY decks.created_at DESC
    """)


def get_deck(deck_id):
    return query_db(
        """
        SELECT *
        FROM decks
        WHERE id = ?
        """,
        (deck_id,),
        one=True
    )


def create_deck(name, description):
    execute_db(
        """
        INSERT INTO decks(name, description)
        VALUES (?, ?)
        """,
        (name, description)
    )