from database.database import query_db, execute_db
from datetime import date

def get_cards(deck_id):
    return query_db(
        """
        SELECT *
        FROM cards
        WHERE deck_id = ?
        ORDER BY english
        """,
        (deck_id,)
    )


def get_card(card_id):
    return query_db(
        """
        SELECT *
        FROM cards
        WHERE id = ?
        """,
        (card_id,),
        one=True
    )


def create_card(
    deck_id,
    english,
    vietnamese,
    ipa,
    part_of_speech,
    example,
    example_translation,
    notes,
    difficulty,
    tags
):
    today = date.today().isoformat()

    execute_db(
        """
        INSERT INTO cards(
            deck_id,
            english,
            vietnamese,
            ipa,
            part_of_speech,
            example,
            example_translation,
            notes,
            difficulty,
            tags,
            ease_factor,
            interval,
            repetitions,
            due_date,
            last_review,
            reviews,
            lapses
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            deck_id,
            english,
            vietnamese,
            ipa,
            part_of_speech,
            example,
            example_translation,
            notes,
            difficulty,
            tags,
            2.5,        # ease_factor
            0,          # interval
            0,          # repetitions
            today,      # due_date
            None,       # last_review
            0,          # reviews
            0           # lapses
        )
    )

def update_card(
    card_id,
    english,
    vietnamese,
    ipa,
    part_of_speech,
    example,
    example_translation,
    notes,
    difficulty,
    tags
):
    execute_db(
        """
        UPDATE cards
        SET
            english=?,
            vietnamese=?,
            ipa=?,
            part_of_speech=?,
            example=?,
            example_translation=?,
            notes=?,
            difficulty=?,
            tags=?
        WHERE id=?
        """,
        (
            english,
            vietnamese,
            ipa,
            part_of_speech,
            example,
            example_translation,
            notes,
            difficulty,
            tags,
            card_id
        )
    )


def delete_card(card_id):
    execute_db(
        "DELETE FROM cards WHERE id=?",
        (card_id,)
    )

def save_review(card_id, updated):
    execute_db(
        """
        UPDATE cards
        SET
            interval = ?,
            ease_factor = ?,
            repetitions = ?,
            due_date = ?,
            last_review = ?,
            reviews = ?,
            lapses = ?
        WHERE id = ?
        """,
        (
            updated["interval"],
            updated["ease_factor"],
            updated["repetitions"],
            updated["due_date"],
            updated["last_review"],
            updated["reviews"],
            updated["lapses"],
            card_id
        )
    )

def save_review(card_id, review):

    execute_db(
        """
        UPDATE cards
        SET
            ease_factor = ?,
            interval = ?,
            repetitions = ?,
            due_date = ?,
            last_review = ?,
            reviews = ?,
            lapses = ?
        WHERE id = ?
        """,
        (
            review["ease_factor"],
            review["interval"],
            review["repetitions"],
            review["due_date"],
            review["last_review"],
            review["reviews"],
            review["lapses"],
            card_id
        )
    )