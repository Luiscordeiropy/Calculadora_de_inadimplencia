from time import sleep
from datetime import datetime, timedelta

taxa_condominial = 255  # Taxa cobrada aos proprietários do condomínio
taxa_com_multa = taxa_condominial + (taxa_condominial * 0.02)  # Multa de 2%
juros = 0.0033 * taxa_com_multa  # Juros de 0,33% ao dia
data1 = datetime.now()  # data de agora DD/MM/AAAA HORAS/MINUTOS/SEGUNDOS
data1.strftime("%d/%m/%Y")  # Formatação da data
total = 0  # Valor total das taxas condominiais inadimplentes
cobrancas = int(input("Quantos cobranças existem?"))
for c in range(cobrancas):  # Faz o detalhamento de todas as taxas condominiais
    print("=-" * 10, f"referente a cobrança {cobrancas}", "-=" * 10)
    if cobrancas > datetime.today().month:  # Se a cobrança é maior que o mês atual para que possa diminuir um ano no sistema
        ano = 2023
        mes = 13 - (cobrancas - datetime.today().month)  # Sistema para diminuir 1 ano a cada 12 meses
        while True:
            if mes <= 0:
                ano -= 1
            if 0 < mes <= 12:
                break
            else:
                mes += 12

        print("Ano de referencia", ano)
        print("Mês de referencia", mes)
    else:  # Cobraças menores que o mês atual, pois se a cobrança for maior que o mês deverá diminuir 1 ano
        ano = 2024
        mes = (data1.month - cobrancas) + 1  # Define de que mês essa cobrança é
        print("Ano de referência: ", ano)
        print("Mês de referencia: ", mes)
    data2 = datetime(ano, mes, 10)  # Data de Referencia (De que ano e de que mês é essa cobrança)
    diferenca = data1 - data2
    cobrancas -= 1  # Diminui uma cobrança para que a função "for" do começo do sistema, Volte para fazer a proxima taxa com inadimplência seguindo a ordem decrescente.
    totjuros = juros * diferenca.days  # Define o total de juros dessa cobrança
    print("Quantidade de dias até hoje: ", diferenca.days)
    print(f"A quantidade de juros é de: {totjuros:.2f}")
    print(f"Total de juros com a taxa condominial: {taxa_com_multa + totjuros:.2f} ")
    total += taxa_com_multa + totjuros
    print("=-" * 32)
    sleep(0.5)

print(total)
