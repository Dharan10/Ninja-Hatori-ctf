import os
import logging
import base64
from datetime import timedelta
from typing import Optional
from flask import Flask, render_template, request, session, redirect, url_for, flash
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
    'shrine': os.environ.get('FLAG_SHRINE', 'nhc{w1sd0m_1n_l1ght}'),
    'illusion': os.environ.get('FLAG_ILLUSION', 'nhc{sp1r1t_0f_4ir}'),
    'forest': os.environ.get('FLAG_FOREST', 'nhc{sh4d0ws_0f_d4rkn3ss}'),
    'volcano': os.environ.get('FLAG_VOLCANO', 'nhc{fl4m3_0f_s4cr1f1c3}')
}

# Security Features
limiter = Limiter(app)
csrf = CSRFProtect(app)
talisman = Talisman(app, content_security_policy={'default-src': "'self'"}, force_https=True)

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

@app.route('/forge')
def forge():
    """Render the forge page."""
    return render_template('forge.html')

@app.route('/logout')
def logout():
    """Clear the session."""
    session.clear()
    flash('Session cleared.', 'info')
    return redirect(url_for('index'))

@app.errorhandler(429)
def ratelimit_handler(e):
    """Handle rate limit exceeded."""
    flash('Too many requests. Slow down!', 'warning')
    return redirect(url_for('map'))

if __name__ == '__main__':
    app.run(debug=True)
