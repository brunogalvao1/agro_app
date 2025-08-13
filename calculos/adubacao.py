import csv
from pathlib import Path

def carregar_recomendacoes():
    path = Path(__file__).parent.parent / "data" / "recomendacoes_goias_template.csv"
    with open(path, newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))

def calcular_totais_por_area(n, p, k, area_ha):
    return {
        "N_total_kg": n * area_ha,
        "P2O5_total_kg": p * area_ha,
        "K2O_total_kg": k * area_ha
    }