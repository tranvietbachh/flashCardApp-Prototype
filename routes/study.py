from flask import Blueprint, render_template, abort, session, redirect, url_for, request
from services.sm2 import update_review
from services.card_service import get_card, save_review
from services.deck_service import get_deck
from services.study_service import get_study_cards, get_due_cards

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

@study.route("/study/review", methods=["GET","POST"])
def review():
    
    if request.method == "POST":
        rating = request.form.get("rating")

        if rating:
            
            session[rating] = session.get(rating, 0) + 1

            deck_id = session.get("study_deck")
            current_index = session.get("current_index", 0)
            mode = session.get("study_mode", "deck")

            cards = get_study_cards(deck_id) if mode == "deck" else get_due_cards()

            if current_index < len(cards):
                card = get_card(cards[current_index]["id"])
                updated = update_review(card, rating)
                save_review(card["id"], updated)

            session["current_index"] = current_index + 1
            session["show_answer"] = False

        return redirect(url_for("study.session_page"))


    session["current_index"] = 0
    session["show_answer"] = False
    
   
    for r in ["forgot", "hard", "good", "easy"]:
        session[r] = 0

    return redirect(url_for("study.session_page"))

@study.route("/study")
def study_home():

    cards = get_due_cards()

    deck_summary = {}

    for card in cards:
        deck = card["deck_name"]

        if deck not in deck_summary:
            deck_summary[deck] = 0

        deck_summary[deck] += 1

    return render_template(
        "study/index.html",
        due_count=len(cards),
        deck_summary=deck_summary
    )