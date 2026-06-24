import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

class WorldCupPredictor:
    def __init__(self):
        self.model = XGBClassifier(
            n_estimators=100, 
            max_depth=6, 
            learning_rate=0.1, 
            objective='multi:softprob',
            random_state=42
        )
        self.features = ['home_attack', 'home_defense', 'away_attack', 'away_defense', 'attack_diff']

    def train(self, df_ml):
        X = df_ml[self.features]
        y = df_ml['match_result']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict_proba(self, home_stats, away_stats):
        features_input = np.array([[ 
            home_stats['goals_scored'], home_stats['goals_conceded'],
            away_stats['goals_scored'], away_stats['goals_conceded'],
            home_stats['goals_scored'] - away_stats['goals_scored']
        ]])
        proba = self.model.predict_proba(features_input)[0]
        return proba