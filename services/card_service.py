from database.database import query_db, execute_db


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
            tags
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            tags
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