import csv

from services.card_service import create_card


def import_csv(deck_id, file):

    decoded = file.stream.read().decode("utf-8").splitlines()

    reader = csv.DictReader(decoded)

    required_columns = [
        "english",
        "vietnamese"
    ]

    if not all(column in reader.fieldnames for column in required_columns):
        raise ValueError(
            "CSV must contain 'english' and 'vietnamese' columns."
        )

    for row in reader:

        if not row["english"].strip():
            continue

        create_card(
            deck_id,
            row.get("english", ""),
            row.get("vietnamese", ""),
            row.get("ipa", ""),
            row.get("part_of_speech", ""),
            row.get("example", ""),
            row.get("example_translation", ""),
            row.get("notes", ""),
            row.get("difficulty", 1),
            row.get("tags", "")
        )