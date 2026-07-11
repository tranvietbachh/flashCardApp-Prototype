from flask import Blueprint, render_template, abort, session, redirect, url_for, request

from services.deck_service import get_deck
from services.study_service import get_study_cards

study = Blueprint("study", __name__)


@study.route("/decks/<int:deck_id>/study")
def start(deck_id):

    deck = get_deck(deck_id)

    if deck is None:
        abort(404)

    cards = get_study_cards(deck_id)

    if len(cards) == 0:
        return render_template(
            "study/session.html",
            deck=deck,
            card=None
        )

    session["study_deck"] = deck_id
    session["current_index"] = 0
    session["show_answer"] = False
    session["forgot"] = 0
    session["hard"] = 0
    session["good"] = 0
    session["easy"] = 0

    return redirect(url_for("study.session_page"))

@study.route("/study/session")
def session_page():

    deck_id = session.get("study_deck")
    current_index = session.get("current_index", 0)
    show_answer = session.get("show_answer", False)

    if deck_id is None:
        return redirect(url_for("decks.index"))

    deck = get_deck(deck_id)
    cards = get_study_cards(deck_id)

    if current_index >= len(cards):
        return render_template("study/summary.html")

    card = cards[current_index]

    return render_template(
        "study/session.html",
        deck=deck,
        card=card,
        current=current_index + 1,
        total=len(cards),
        show_answer=show_answer
    )

@study.route("/study/show-answer", methods=["POST"])
def show_answer():

    session["show_answer"] = True

    return redirect(url_for("study.session_page"))

@study.route("/study/review", methods=["POST"])
def review():

    rating = request.form["rating"]

    if rating == "forgot":
        session["forgot"] = session.get("forgot", 0) + 1

    elif rating == "hard":
        session["hard"] = session.get("hard", 0) + 1

    elif rating == "good":
        session["good"] = session.get("good", 0) + 1

    elif rating == "easy":
        session["easy"] = session.get("easy", 0) + 1

    session["current_index"] += 1
    session["show_answer"] = False

    return redirect(url_for("study.session_page"))