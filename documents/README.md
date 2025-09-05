# Ninja Hattori and the Six Dragon Fragments

A narrative-driven Capture The Flag (CTF) web application built with Flask, featuring six progressive challenges that teach common web vulnerabilities through an engaging story of a ninja warrior.

## Description

Embark on an epic journey as Hattori, a legendary ninja, to collect the Six Dragon Fragments and defeat the Shadow Warlord Ryukazen. This CTF combines storytelling, cybersecurity education, and interactive web exploitation. Players solve challenges by exploiting vulnerabilities like XSS, SQL Injection, Command Injection, and LFI, unlocking fragments and advancing the plot.

## Features

- **6 Progressive Challenges**: Easy to Hard difficulties covering real-world vulnerabilities.
- **Narrative Storyline**: Immersive story with animated text and cinematic elements.
- **Secure by Design**: Rate limiting, CSRF protection, CSP, and Docker hardening.
- **Educational**: Each challenge includes hints and teaches exploitation techniques.
- **Docker Support**: Production-ready containerization with multi-stage builds.
- **Session Management**: Tracks progress and prevents replay attacks.

## Prerequisites

- Python 3.9+
- Docker (for containerized deployment)
- Git

## Installation

### Local Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/Dharan10/Ninja-Hatori-ctf.git
   cd Ninja-Hatori-ctf
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Initialize the Database**:
   ```
   python setup_db.py
   ```

4. **Run the Application**:
   ```
   python app.py
   ```
   Access at `http://localhost:5000`.

### Docker Setup

1. **Build the Image**:
   ```
   docker build -t ninja-hattori-ctf .
   ```

2. **Run the Container**:
   ```
   docker run -p 5000:5000 ninja-hattori-ctf
   ```
   Access at `http://localhost:5000`.

## How to Play

1. **Start**: Visit the landing page and navigate to the map.
2. **Challenges**: Solve each challenge by finding/exploiting vulnerabilities and submitting flags.
3. **Progression**: Unlocked challenges appear on the map; solve all 6 for the finale.
4. **Hints**: Use browser dev tools, inspect elements, and test inputs.
5. **Finale**: Experience the victory sequence, confrontation, and post-credits.

## 🔄 Resetting the Adventure

When pressing the start the adventure if you see anything but not **The Map of Shadows** you may need to **manually reset your progress**.

To do this, simply visit the reset endpoint in your browser:

http://localhost:5000/reset

This will reset your current session so you can start the adventure again.

## Challenges Overview

1. **Cavern (Easy)**: Source code inspection for hidden flags.
2. **Graveyard (Medium)**: Decode double-encoded data.
3. **Shrine (Medium)**: SQL Injection to query hidden data.
4. **Spirit (Medium)**: Reflected XSS to fetch flags.
5. **Shadows (Hard)**: Command Injection with payload crafting.
6. **Flame (Hard)**: LFI with directory traversal and encoding.

## Walkthrough and Hints

For detailed solutions, hints, and step-by-step guides:
- Checkout the `doc/walk` branch: `git checkout doc/walk`.
- Contains markdown files with payloads, explanations, and educational notes.

## Security Notes

- **Educational Purpose**: Vulnerabilities are intentional for learning.
- **Production**: Disable debug mode, use HTTPS, and secure environment variables.
- **Responsible Use**: Do not deploy with real sensitive data.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add feature'`.
4. Push and open a PR.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Credits

- **Developer**: Dharan
- **Inspiration**: Classic CTF challenges and ninja hattori cartoon.
- **Tools**: Flask, SQLite, Docker.

Enjoy the adventure! If you have questions, open an issue on GitHub.
