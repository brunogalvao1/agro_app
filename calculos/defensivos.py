def calcular_dose_defensivo(dose_ha, area_ha, concentracao=None):
	total_produto = dose_ha * area_ha
	if concentracao is not None:
		ingrediente_ativo = total_produto * (concentracao / 100)
	else:
		ingrediente_ativo = None

	return {
		"total_produto": total_produto,
		"ingrediente_ativo": ingrediente_ativo
	}

# Exemplo de uso:
if __name__ == "__main__":
	resultado = calcular_dose_defensivo(2.5, 10, 50)
	print(resultado)
