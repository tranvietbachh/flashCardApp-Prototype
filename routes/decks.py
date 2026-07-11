from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    abort
)
from services.csv_handler import import_csv
from services.deck_service import (
    get_all_decks,
    get_deck,
    create_deck
)

from services.card_service import (
    get_cards,
    get_card,
    create_card,
    update_card,
    delete_card
)

decks = Blueprint("decks", __name__)


@decks.route("/decks")
def index():
    return render_template(
        "decks/index.html",
        decks=get_all_decks()
    )


@decks.route("/decks/new", methods=["GET", "POST"])
def new_deck():

    if request.method == "POST":

        create_deck(
            request.form["name"],
            request.form["description"]
        )

        return redirect(url_for("decks.index"))

    return render_template("decks/create.html")


@decks.route("/decks/<int:deck_id>")
def view_deck(deck_id):

    deck = get_deck(deck_id)

    if deck is None:
        abort(404)

    return render_template(
        "decks/deck.html",
        deck=deck,
        cards=get_cards(deck_id)
    )


@decks.route("/decks/<int:deck_id>/cards/new", methods=["GET", "POST"])
def new_card(deck_id):

    deck = get_deck(deck_id)

    if deck is None:
        abort(404)

    if request.method == "POST":

        create_card(
            deck_id,
            request.form["english"],
            request.form["vietnamese"],
            request.form["ipa"],
            request.form["part_of_speech"],
            request.form["example"],
            request.form["example_translation"],
            request.form["notes"],
            request.form["difficulty"],
            request.form["tags"]
        )

        return redirect(
            url_for("decks.view_deck", deck_id=deck_id)
        )

    return render_template(
        "decks/card_form.html",
        deck=deck
    )

@decks.route("/decks/<int:deck_id>/upload", methods=["GET", "POST"])
def upload_csv(deck_id):

    deck = get_deck(deck_id)

    if deck is None:
        abort(404)

    if request.method == "POST":

        file = request.files.get("csv_file")

        if file and file.filename.endswith(".csv"):
            import_csv(deck_id, file)

        return redirect(
            url_for(
                "decks.view_deck",
                deck_id=deck_id
            )
        )

    return render_template(
        "decks/upload.html",
        deck=deck
    )
@decks.route("/cards/<int:card_id>/edit", methods=["GET", "POST"])
def edit_card(card_id):

    card = get_card(card_id)

    if card is None:
        abort(404)

    if request.method == "POST":

        update_card(
            card_id,
            request.form["english"],
            request.form["vietnamese"],
            request.form["ipa"],
            request.form["part_of_speech"],
            request.form["example"],
            request.form["example_translation"],
            request.form["notes"],
            request.form["difficulty"],
            request.form["tags"]
        )

        return redirect(
            url_for(
                "decks.view_deck",
                deck_id=card["deck_id"]
            )
        )

    return render_template(
        "decks/card_edit.html",
        card=card
    )


@decks.route("/cards/<int:card_id>/delete", methods=["POST"])
def remove_card(card_id):

    card = get_card(card_id)

    if card is None:
        abort(404)

    delete_card(card_id)

    return redirect(
        url_for(
            "decks.view_deck",
            deck_id=card["deck_id"]
        )
    )