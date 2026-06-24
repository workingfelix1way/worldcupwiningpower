import os
import pandas as pd
import numpy as np

class DataPipeline:
    def __init__(self, raw_dir='data/raw'):
        self.raw_dir = raw_dir
        self.file_historico = None
        self.file_fixture = None
        self._scan_data_files()

    def _scan_data_files(self):
        if os.path.exists(self.raw_dir):
            for file in os.listdir(self.raw_dir):
                if 'historic' in file.lower() or 'results' in file.lower():
                    self.file_historico = os.path.join(self.raw_dir, file)
                elif 'fixture' in file.lower() or 'match' in file.lower():
                    self.file_fixture = os.path.join(self.raw_dir, file)

    def process(self):
        if not self.file_historico or not os.path.exists(self.file_historico):
            self.file_historico = os.path.join(self.raw_dir, 'clean_fifa_worldcup_historical_data.csv')
            
        if not os.path.exists(self.file_historico):
            raise FileNotFoundError(f"Không tìm thấy tệp dữ liệu lịch sử tại: {self.file_historico}")
            
        df_historico = pd.read_csv(self.file_historico)
        df_historico.dropna(subset=['home', 'away', 'home_goals', 'away_goals'], inplace=True)
        
        df_home = df_historico[['home', 'home_goals', 'away_goals']].rename(
            columns={'home': 'team', 'home_goals': 'goals_scored', 'away_goals': 'goals_conceded'}
        )
        df_away = df_historico[['away', 'home_goals', 'away_goals']].rename(
            columns={'away': 'team', 'home_goals': 'goals_conceded', 'away_goals': 'goals_scored'}
        )
        df_team_strength = pd.concat([df_home, df_away], ignore_index=True).groupby('team').mean()
        
        world_cup_2026_new_teams = [
             "Indonesia", "Thailand", "Uzbekistan", "Iraq", 
            "Jordan", "Oman", "Georgia", "Albania", "Mali", "Burkina Faso"
        ]
        
        global_avg_scored = df_team_strength['goals_scored'].mean()
        global_avg_conceded = df_team_strength['goals_conceded'].mean()
        
        new_teams_data = []
        for team in world_cup_2026_new_teams:
            if team not in df_team_strength.index:
                new_teams_data.append({
                    'team': team,
                    'goals_scored': global_avg_scored * 0.9,
                    'goals_conceded': global_avg_conceded * 1.1
                })
                
        if new_teams_data:
            df_new_teams = pd.DataFrame(new_teams_data).set_index('team')
            df_team_strength = pd.concat([df_team_strength, df_new_teams])
        
        df_historico['match_result'] = np.where(df_historico['home_goals'] > df_historico['away_goals'], 2,
                                       np.where(df_historico['home_goals'] == df_historico['away_goals'], 1, 0))
        
        df_ml = df_historico.copy()
        df_ml['home_attack'] = df_ml['home'].map(df_team_strength['goals_scored']).fillna(global_avg_scored)
        df_ml['home_defense'] = df_ml['home'].map(df_team_strength['goals_conceded']).fillna(global_avg_conceded)
        df_ml['away_attack'] = df_ml['away'].map(df_team_strength['goals_scored']).fillna(global_avg_scored)
        df_ml['away_defense'] = df_ml['away'].map(df_team_strength['goals_conceded']).fillna(global_avg_conceded)
        df_ml['attack_diff'] = df_ml['home_attack'] - df_ml['away_attack']
        
        return df_team_strength, df_ml