
faturamentoestados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}


faturamento = sum(faturamentoestados.values())

print("Percentual de representação por estado:")
for estado, valor in faturamentoestados.items():
    percentual = (valor / faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")
