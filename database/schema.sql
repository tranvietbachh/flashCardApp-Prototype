DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS decks;

CREATE TABLE decks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    deck_id INTEGER NOT NULL,

    english TEXT NOT NULL,
    vietnamese TEXT NOT NULL,

    ipa TEXT,
    part_of_speech TEXT,

    example TEXT,
    example_translation TEXT,

    notes TEXT,
    difficulty INTEGER DEFAULT 1,
    tags TEXT,

    ease_factor REAL DEFAULT 2.5,
    interval INTEGER DEFAULT 0,
    repetitions INTEGER DEFAULT 0,

    due_date DATE DEFAULT CURRENT_DATE,
    last_review DATE,

    reviews INTEGER DEFAULT 0,
    lapses INTEGER DEFAULT 0,

    FOREIGN KEY(deck_id) REFERENCES decks(id)
);