# FlashCard

FlashCard is a Flask-based web application designed to help students learn vocabulary through flashcards and spaced repetition. Users can create custom decks, import vocabulary from CSV files, review cards using the SM-2 spaced repetition algorithm, and track daily due reviews.

The project serves as a proof-of-concept prototype for an educational flashcard system.

---

## Features

### Deck Management
- Create new flashcard decks
- View deck information
- Organize vocabulary into multiple decks

### Flashcard Management
- Create flashcards manually
- Edit existing flashcards
- Delete flashcards
- Support for:
  - English
  - Vietnamese
  - IPA Pronunciation
  - Part of Speech
  - Example Sentence
  - Example Translation
  - Notes
  - Difficulty
  - Tags

### CSV Import
Import vocabulary directly from CSV files.

Supported fields:

- english
- vietnamese
- ipa
- part_of_speech
- example
- example_translation
- notes
- difficulty
- tags

Example CSV files are included in the repository.

### Study Sessions

Two study modes are available.

#### Deck Study

Review every card inside a selected deck.

Useful for:

- Learning new vocabulary
- Reviewing an entire topic
- Practicing before exams

#### Daily Study

Reviews only cards whose due date is today or earlier using the SM-2 algorithm.

The dashboard displays:

- Cards due today
- Due cards grouped by deck

### SM-2 Spaced Repetition

Each review updates:

- Ease Factor
- Review Interval
- Repetitions
- Due Date
- Last Review
- Total Reviews
- Lapses

Review ratings:

- Forgot
- Hard
- Good
- Easy

Cards are automatically scheduled for future review.

### Audio Pronunciation

The study session includes browser-based text-to-speech using the Web Speech API.

Features:

- No external API required
- No audio files stored
- Uses the browser's built-in speech synthesis engine

---

## Technologies

Backend

- Python
- Flask
- SQLite

Frontend

- HTML
- CSS
- JavaScript

Libraries

- csv
- sqlite3
- Web Speech API

---

## Project Structure

```
flashCardApp/
│
├── app.py
├── requirements.txt
│
├── database/
│   ├── flashcard.db
│   ├── schema.sql
│   └── database.py
│
├── routes/
│
├── services/
│
├── templates/
│
├── static/
│
└── test_files/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/tranvietbachh/flashCardApp-Prototype.git
```

Navigate to the project

```bash
cd flashCardApp-Prototype
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Database

SQLite is used for local storage.

The database contains two tables:

### Decks

Stores deck information.

### Cards

Stores flashcards together with SM-2 scheduling data.

SM-2 fields include:

- ease_factor
- interval
- repetitions
- due_date
- last_review
- reviews
- lapses

---

## Settings

The Settings page allows the user to reset the database.

Resetting the database removes:

- All decks
- All flashcards
- All study progress

---

## Sample Data

Example CSV datasets are included, including:

- Geography
- B1 Adjectives
- Transport
- Internet & Social Media

These can be imported directly into the application.