from datetime import date, timedelta


def update_review(card, rating):
    """
    Updates a card using an adapted SM-2 algorithm.

    Ratings:
        forgot
        hard
        good
        easy

    Returns a dictionary containing the updated values.
    """

    interval = card["interval"]
    ease = card["ease_factor"]
    repetitions = card["repetitions"]
    reviews = card["reviews"]
    lapses = card["lapses"]

    today = date.today()

    if rating == "forgot":

        interval = 1
        repetitions = 0
        ease = max(1.3, ease - 0.20)
        lapses += 1

    elif rating == "hard":

        repetitions += 1

        if interval == 0:
            interval = 2
        else:
            interval = round(interval * 1.2)

        ease = max(1.3, ease - 0.15)

    elif rating == "good":

        repetitions += 1

        if repetitions == 1:
            interval = 1
        elif repetitions == 2:
            interval = 3
        else:
            interval = round(interval * ease)

    elif rating == "easy":

        repetitions += 1

        if repetitions == 1:
            interval = 4
        else:
            interval = round(interval * ease * 1.3)

        ease += 0.15

    else:
        raise ValueError("Invalid rating.")

    reviews += 1

    due_date = today + timedelta(days=interval)

    return {
        "interval": interval,
        "ease_factor": ease,
        "repetitions": repetitions,
        "reviews": reviews,
        "lapses": lapses,
        "due_date": due_date.isoformat(),
        "last_review": today.isoformat()
    }