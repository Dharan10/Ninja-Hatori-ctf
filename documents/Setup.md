# Setup Guide

## Local Development Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dharan10/Ninja-Hatori-ctf.git
   cd Ninja-Hatori-ctf
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup database**:
   ```bash
   python setup_db.py
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   - Open browser to `http://localhost:5000`
   - Start the adventure

## Docker Deployment

### Prerequisites
- Docker installed and running

### Deployment Steps

1. **Build the Docker image**:
   ```bash
   docker build -t ninja-hattori-ctf .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 ninja-hattori-ctf
   ```

3. **Access the application**:
   - Open browser to `http://localhost:5000`

## Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
SESSION_SECURE=True
FLAG_CAVERN=nhc{ech0es_1n_th3_d4rkn3ss}
FLAG_GRAVEYARD=nhc{l3g4cy_d3c0d3d_fr0m_run3s}
FLAG_SHRINE=nhc{d3c3pt10n_r3v34ls_truth}
FLAG_SPIRIT=nhc{scr1pt3d_1llus10ns_sh4tt3r}
FLAG_FOREST=nhc{sh4d0ws_0f_d4rkn3ss}
FLAG_VOLCANO=nhc{fl4m3_0f_s4cr1f1c3}
FLAG_SHADOWS=nhc{sh4d0w_c0mm4nd_3x3cut3d}
FLAG_FLAME=nhc{f1l3_p4th_tr4v3rs3d_w1th_fl4m3}
FINAL_FLAG=smn{Th3_S3cr3t_Scr0ll_0f_S0g3n_1s_Y0urs!}
```

## Troubleshooting

### Common Issues

1. **Port 5000 already in use**:
   ```bash
   # Find process using port 5000
   lsof -i :5000
   # Kill the process or use different port
   docker run -p 5001:5000 ninja-hattori-ctf
   ```

2. **Database errors**:
   - Ensure `shrine.db` exists
   - Run `python setup_db.py` again

3. **Permission errors**:
   - Check file permissions on database files
   - Ensure write access to uploads/ directory

### Reset Progress
Visit `http://localhost:5000/reset` to clear session and restart.
