import os
import logging
import base64
import sqlite3
from datetime import timedelta
from typing import Optional
from flask import Flask, render_template, request, session, redirect, url_for, flash, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_talisman import Talisman

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret_key_change_in_prod')
app.config['SESSION_COOKIE_SECURE'] = os.environ.get('SESSION_SECURE', 'False').lower() == 'true'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
app.config['RATELIMIT_KEY_FUNC'] = get_remote_address

# Private flag dictionary - loaded from env vars
flags = {
    'cavern': os.environ.get('FLAG_CAVERN', 'nhc{ech0es_1n_th3_d4rkn3ss}'),
    'graveyard': os.environ.get('FLAG_GRAVEYARD', 'nhc{l3g4cy_d3c0d3d_fr0m_run3s}'),
    'shrine': os.environ.get('FLAG_SHRINE', 'nhc{d3c3pt10n_r3v34ls_truth}'),
    'spirit': os.environ.get('FLAG_SPIRIT', 'nhc{scr1pt3d_1llus10ns_sh4tt3r}'),
    'forest': os.environ.get('FLAG_FOREST', 'nhc{sh4d0ws_0f_d4rkn3ss}'),
    'volcano': os.environ.get('FLAG_VOLCANO', 'nhc{fl4m3_0f_s4cr1f1c3}'),
    'shadows': os.environ.get('FLAG_SHADOWS', 'nhc{sh4d0w_c0mm4nd_3x3cut3d}'),
    'flame': os.environ.get('FLAG_FLAME', 'nhc{f1l3_p4th_tr4v3rs3d_w1th_fl4m3}')
}

# Security Features
limiter = Limiter(app)
csrf = CSRFProtect(app)
talisman = Talisman(app, content_security_policy={'default-src': "'self'", 'script-src': "'self' 'unsafe-inline'", 'style-src': "'self' 'unsafe-inline' https://fonts.googleapis.com"}, force_https=True)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
MAX_FLAG_LENGTH = 100

@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf)

def check_flag(submitted_flag: str) -> Optional[str]:
    """Check if submitted flag is correct and return the challenge name."""
    for challenge, correct_flag in flags.items():
        if submitted_flag == correct_flag:
            return challenge
    return None

@app.before_request
def log_request_info():
    logger.info(f"Request: {request.method} {request.url} from {get_remote_address()}")

@app.route('/')
def index():
    """Render the landing page."""
    return render_template('index.html')

@app.route('/map', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def map():
    """Handle map page and flag submissions."""
    if request.method == 'POST':
        try:
            submitted_flag = request.form.get('flag', '').strip()
            if not submitted_flag:
                flash('Please enter a flag.', 'warning')
                return redirect(url_for('map'))
            
            # Input validation
            if len(submitted_flag) > MAX_FLAG_LENGTH:
                flash('Flag too long.', 'danger')
                logger.warning(f"Flag too long: {submitted_flag[:50]}...")
                return redirect(url_for('map'))
            if not submitted_flag.startswith('nhc{') or not submitted_flag.endswith('}'):
                flash('Invalid flag format.', 'danger')
                logger.warning(f"Invalid flag format: {submitted_flag}")
                return redirect(url_for('map'))
            
            challenge = check_flag(submitted_flag)
            if challenge:
                if 'solved' not in session:
                    session['solved'] = []
                if challenge not in session['solved']:
                    session['solved'].append(challenge)
                    flash(f'Fragment {challenge} unlocked!', 'success')
                    logger.info(f"Flag solved: {challenge}")
                else:
                    flash('Fragment already solved.', 'info')
            else:
                flash('Incorrect flag.', 'danger')
                logger.warning(f"Incorrect flag submitted: {submitted_flag}")
        except Exception as e:
            logger.error(f"Error in flag submission: {e}")
            flash('An error occurred. Try again.', 'danger')
        return redirect(url_for('map'))
    return render_template('map.html')

@app.route('/challenge/graveyard')
def graveyard():
    """Render the graveyard challenge with double-encoded flag."""
    flag = flags['graveyard']
    # First, encode with Base32
    base32_encoded = base64.b32encode(flag.encode()).decode()
    # Then, encode the Base32 string with Base64
    encoded_flag = base64.b64encode(base32_encoded.encode()).decode()
    return render_template('graveyard.html', encoded_flag=encoded_flag)

@app.route('/challenge/shrine', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def shrine():
    """Handle the shrine challenge with SQL injection vulnerability."""
    results = []
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if query:
            try:
                conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'shrine.db'))
                cursor = conn.cursor()
                # Vulnerable SQL query - direct string concatenation
                sql_query = f"SELECT title, content FROM scrolls WHERE title LIKE '%{query}'"
                cursor.execute(sql_query)
                results = cursor.fetchall()
                conn.close()
            except Exception as e:
                logger.error(f"Database error: {e}")
                flash('An error occurred while searching.', 'danger')
    return render_template('shrine.html', results=results)

@app.route('/challenge/spirit', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def spirit():
    """Handle the spirit challenge with reflected XSS vulnerability."""
    message = ""
    if request.method == 'POST':
        message = request.form.get('message', '').strip()
        if message:
            flash('Message submitted.', 'success')
        # For reflected XSS, render the page with the message
        response = make_response(render_template('spirit.html', messages=[], reflected_message=message, flags=flags))
        return response
    
    # GET: no messages, no reflected message
    response = make_response(render_template('spirit.html', messages=[], reflected_message="", flags=flags))
    return response

@app.route('/flag')
def get_flag():
    """Return the spirit flag."""
    return flags['spirit']

@app.route('/challenge/shadows', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def shadows():
    """Handle the shadows challenge with command injection vulnerability."""
    output = ""
    error = ""
    if request.method == 'POST':
        ip = request.form.get('ip', '').strip()
        if ip:
            # Hard mode: Block injection chars to force complex payloads
            blocked_chars = [';', '|', '`', '&']
            if any(char in ip for char in blocked_chars):
                error = 'Invalid IP format. Only alphanumeric, dots, hyphens, $, (, ) allowed.'
            else:
                try:
                    # Vulnerable: direct f-string in os.popen
                    command = f'echo "Scanning {ip}" ; ping -c 1 {ip}'
                    result = os.popen(command).read()
                    output = result
                except Exception as e:
                    output = f"Error: {str(e)}"
    return render_template('shadows.html', output=output, error=error)

@app.route('/challenge/flame')
def flame():
    """Render the flame challenge page."""
    return render_template('flame.html')

@app.route('/challenge/flame/view')
def flame_view():
    """Vulnerable LFI route."""
    scroll = request.args.get('scroll', '')
    if not scroll:
        return "No echo specified."
    try:
        # Vulnerable: no sanitization for ../
        with open(f'uploads/{scroll}', 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Echo not found."
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/challenge/cavern')
def cavern():
    """Render the cavern challenge page."""
    return render_template('cavern.html')

@app.route('/reset')
def reset():
    """Reset the session and clear messages for testing purposes."""
    session.clear()
    try:
        conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'shrine.db'))
        cursor = conn.cursor()
        cursor.execute('DELETE FROM messages')
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Error clearing messages: {e}")
    flash('Session and messages reset. All progress cleared.', 'info')
    return redirect(url_for('index'))

@app.route('/forge')
def forge():
    """Render the forge page."""
    final_flag = os.environ.get('FINAL_FLAG', 'smn{Th3_S3cr3t_Scr0ll_0f_S0g3n_1s_Y0urs!}')
    return render_template('forge.html', final_flag=final_flag)

@app.route('/logout')
def logout():
    """Clear the session."""
    session.clear()
    flash('Session cleared.', 'info')
    return redirect(url_for('index'))

@app.route('/victory')
def victory():
    """Render the victory page if all challenges are solved."""
    if len(session.get('solved', [])) < 6:
        return redirect(url_for('map'))
    return render_template('victory.html')

@app.route('/postcredit')
def postcredit():
    """Render the post-credit scene."""
    return render_template('postcredit.html')

@app.route('/confrontation')
def confrontation():
    """Render the final confrontation scene."""
    return render_template('confrontation.html')

@app.errorhandler(429)
def ratelimit_handler(e):
    """Handle rate limit exceeded."""
    flash('Too many requests. Slow down!', 'warning')
    return redirect(url_for('map'))

if __name__ == '__main__':
    app.run(debug=True)
