# PCM Advanced Mock Test

A professional-grade competitive exam mock test built with **Streamlit** — featuring 45 JEE/MHT-CET level questions across Physics, Chemistry, and Mathematics.

## Features

- **45 high-quality questions** — 16 Chemistry + 16 Physics + 13 Mathematics
- **3-hour countdown timer** with auto-submit and time warnings
- **Interactive question navigation** with palette (color-coded)
- **Mark for Review** functionality
- **Comprehensive post-test analytics:**
  - Subject-wise performance
  - Chapter-wise performance tables
  - Question-wise review with step-by-step explanations
  - Difficulty-level analysis (Medium / Hard / Very Hard)
  - Mistake classification (Conceptual / Calculation / Formula / Silly)
  - Negative marking impact analysis
  - Final performance report with specific recommendations

## Marking Scheme

| Action      | Marks |
|-------------|-------|
| Correct     | +4    |
| Wrong       | −1    |
| Unattempted | 0     |

**Maximum Marks:** 180

## Run Locally

### Prerequisites
- Python 3.8+

### Steps

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "PCM Mock Test app"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/pcm-mock-test.git
   git push -u origin main
   ```

2. **Deploy:**
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Click **New app**
   - Select your repo → branch `main` → file `app.py`
   - Click **Deploy**

3. **Share the URL** with your students / peers.

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── questions.py        # 45-question bank with explanations
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Syllabus Coverage

### Chemistry (16 Questions)
- **Chemical Kinetics** (9 Q) — Rate law, order, integrated rate equations, half-life, Arrhenius, pseudo-first-order, graph-based
- Thermodynamics, Equilibrium, Electrochemistry, Solutions, Atomic Structure, Chemical Bonding, Organic Chemistry

### Physics (16 Questions)
- **Electrostatics** (10 Q) — Coulomb's law, electric field, potential, Gauss's law, capacitors, dipole, dielectrics, conductors
- Current Electricity, Magnetism, EMI, Ray Optics, Modern Physics, Kinematics

### Mathematics (13 Questions)
- Units & Dimensions (2 Q)
- Trigonometry (3 Q)
- Mathematical Reasoning (2 Q)
- 3D Geometry (2 Q)
- Algebra, Differentiation, Vectors, Probability

## Difficulty Distribution

| Level     | Count | Percentage |
|-----------|-------|------------|
| Medium    | ~9    | 20%        |
| Hard      | ~22   | 49%        |
| Very Hard | ~14   | 31%        |
