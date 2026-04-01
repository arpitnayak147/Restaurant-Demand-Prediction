# Restaurant Demand Prediction

This project predicts:
- Daily covers (number of guests)
- Average check per guest

## Features
- Reservation-based features
- Time-based features
- Lag & rolling features

## Models
- XGBoost for covers_count
- XGBoost for avg_check

## Model Performance

- Covers Model WMAPE: ~7%
- Baseline WMAPE: ~12.9%

→ ~45% improvement over baseline

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py

 
