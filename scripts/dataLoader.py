import pandas as pd
from pathlib import Path

def carregar_dados():

    raiz_projeto = Path(__file__).resolve().parent.parent
    
    caminho_brasileirao = raiz_projeto / "data" / "mundo_transfermarkt_competicoes_brasileirao_serie_a.csv"
    caminho_copa = raiz_projeto / "data" / "mundo_transfermarkt_competicoes_copa_brasil.csv"
    
    try:
        df_brasileirao = pd.read_csv(caminho_brasileirao)
        df_copa = pd.read_csv(caminho_copa)
        
        print(" Data Base carregadas com sucesso.")
        return df_brasileirao, df_copa
        
    except FileNotFoundError as e:
        print(f"Erro ao encontrar o arquivo: {e}")
        return None, None
    
if __name__ == '__main__':
    df_brasileirao, df_copa = carregar_dados()