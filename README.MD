FlashCard

Still in prototype phase

Runs on a Flask backend.
Set up a virtual environment (venv), install the required dependencies, then run app.py.
Current Proof of Concept

The current prototype supports:

Uploading vocabulary through CSV import.
Creating, editing, and deleting flashcards.
Organizing flashcards into decks.
Studying cards one at a time.
Revealing answers and rating recall as Forgot, Hard, Good, or Easy.
Displaying a simple session summary showing the number of Forgot, Hard, Good, and Easy responses.

A sample dataset is provided in test_files.csv for testing the application.

To Do
Implement SM-2 algorithm for flash card queue (function completed)
Add SM-2 required variables to the database.
Return only cards due for review today.
Update card scheduling after each review.
Audio features.
Customization and settings.
Improved study tab/dashboard.