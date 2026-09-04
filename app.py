
def calcular_consumo():
    print("=" * 45)
    print("⚡ CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE ⚡")
    print("=" * 45)
    
    # Entradas de dados
    aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ").strip()
    
    try:
        potencia = float(input("Digite a potência do aparelho em Watts (W): "))
        horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))
    except ValueError:
        print("\n❌ Erro: Por favor, digite apenas números válidos para potência e horas.")
        return

    # Cálculo do consumo mensal em kWh
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    
    # Custo estimado usando tarifa fixa (R$ 0,75 por kWh)
    tarifa_kwh = 0.75
    custo_estimado = consumo_mensal * tarifa_kwh

    # Exibição dos resultados
    print("\n" + "-" * 45)
    print("📊 RESULTADO DA ESTIMATIVA MENSAL")
    print("-" * 45)
    print(f"🔹 Aparelho: {aparelho.capitalize()}")
    print(f"⚡ Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"💰 Custo estimado: R$ {custo_estimado:.2f}/mês (Tarifa ref.: R$ 0,75/kWh)")
    print("=" * 45)

if __name__ == "__main__":
    calcular_consumo()