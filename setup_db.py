import sqlite3
import os

def setup_database():
    db_path = os.path.join(os.path.dirname(__file__), 'shrine.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create scrolls table with sample data
    cursor.execute('DROP TABLE IF EXISTS scrolls')
    cursor.execute('''
        CREATE TABLE scrolls (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            content TEXT NOT NULL
        )
    ''')

    # Insert sample data
    sample_data = [
        ("History of the North", "The northern lands were once ruled by wise elders who valued knowledge above all."),
        ("Art of the Silent Blade", "Mastery of stealth requires patience and the ability to become one with the shadows."),
        ("Tales of the Dragon Temple", "Legends speak of a temple guarded by ancient spirits, where only the worthy may enter."),
        ("Wisdom of the Ancients", "True strength comes not from power, but from understanding one's own heart."),
        ("The Path of the Ninja", "A ninja's journey is fraught with deception, but clarity comes from within."),
        ("Chronicles of the Shadow Clan", "The shadow clan mastered the art of invisibility, striking fear into the hearts of their enemies."),
        ("Legends of the Eternal Flame", "The eternal flame burns within those who seek justice, never extinguishing their resolve."),
        ("Secrets of the Wind Walker", "To walk with the wind is to become untouchable, a ghost in the storm."),
        ("Myths of the Dragon's Hoard", "Ancient treasures lie hidden, guarded by riddles and illusions."),
        ("Tales of the Forgotten Warrior", "A warrior's legacy is etched in the scars of battle, remembered in the echoes of time!.")
    ]

    cursor.executemany('INSERT OR IGNORE INTO scrolls (title, content) VALUES (?, ?)', sample_data)

    # Create hidden table with flag
    cursor.execute('DROP TABLE IF EXISTS wisdom_secrets')
    cursor.execute('''
        CREATE TABLE wisdom_secrets (
            hidden_title TEXT NOT NULL,
            hidden_content TEXT NOT NULL
        )
    ''')

    cursor.execute('INSERT INTO wisdom_secrets (hidden_title, hidden_content) VALUES (?, ?)', ('Secret Wisdom', 'nhc{d3c3pt10n_r3v34ls_truth}'))

    # Create messages table for spirit challenge
    cursor.execute('DROP TABLE IF EXISTS messages')
    cursor.execute('''
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY,
            message_text TEXT NOT NULL
        )
    ''')

    # Insert some sample messages
    sample_messages = [
        "May the spirits guide you.",
        "Rest in peace, brave warriors.",
        "Your sacrifice will not be forgotten."
    ]

    cursor.executemany('INSERT INTO messages (message_text) VALUES (?)', [(msg,) for msg in sample_messages])

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == '__main__':
    setup_database()
