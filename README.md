# ⚽ FIFA World Cup 2026 Match Predictor using Machine Learning

An enterprise-grade Machine Learning Classification Pipeline built with Python and Streamlit to predict the probabilities (Win, Draw, Lose) of any match setup in the upcoming FIFA World Cup 2026. The system eliminates heavy charting components to focus purely on high-performance text-based metrics and domain-specific financial odds modeling.

## 🚀 Key Features

- **XGBoost Classifier Integration:** Replaced basic models with Extreme Gradient Boosting (`XGBClassifier`) for high-accuracy tabular data training.
- **Dynamic Data Injection:** Automatically handles expanding World Cup 2026 rosters (e.g., Indonesia, Thailand, China, etc.) by calculating global baseline normalization scores to prevent `KeyError` on runtime.
- **Strict UX Constraint:** Intelligent selectboxes that dynamically filter out the selected Home Team from the Away Team choices to eliminate redundant inputs.
- **Sports Analytics Extension (Decimal Odds):** Converts mathematical prediction arrays into European Decimal Odds ($\text{Odds} = \frac{1}{\text{Probability}}$) providing a real-world sports betting reference.
- **FIFA Tournament Logic:** Custom normalization logic to handle Group Stage matches (allowing draws) vs. Knock-Out stages (eliminating draws mathematically).

---

## 🛠️ System Architecture & Folder Structure

The project strictly follows the Modular OOP (Object-Oriented Programming) architecture to decouple data manipulation from interface presentation:

```text
IntroduceAI/
├── .gitignore            # Excludes massive files like venv/ and __pycache__/
├── requirements.txt      # Reproducible dependency management
├── app.py                # Ultra-lean Streamlit Frontend (Text-based presentation)
├── README.md             # Project documentation
│
├── data/
│   └── raw/              # Ground-truth Kaggle CSV historical datasets
│
└── src/                  # Core Machine Learning Backend
    ├── __init__.py       # Initializes src as a Python package
    ├── data_pipeline.py  # ETL, Feature Engineering (Attack/Defense Strength calculation)
    └── ai_model.py       # Model training, Hyperparameter configuration & Evaluation
