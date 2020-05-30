"""
Tarifa do estacionamento:

    1a a 2a hora: R$ 1.00 cada
    3a e 4a hora: RS 1.40 cada
    5a hora e seguintes horas: R$ 2.00 cada

O numero de horas a pagar é sempre inteiro e arrendondado por excesso. Quem estacionar por 61 min, pagará por 2 horas,
que é o mesmo que alguém pagaria se tivesse permanecido por 120 min. O momento de chegada e partida são apresentados em
forma de pares inteiros. Por exemplo 12 50 (dez para as 1 da tarde). Pretende-se criar um programa que, lidos pelo
teclado os horarios de chegada e partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada
e a partida se dão com intervalo não superior a 24 horas, isso não é uma situação de erro, antes significará que a
partida ocorreu no dia seguinte ao da chegada
"""
# entrada dos valores em formato de string
chegada = input("Digite o horario da chegada: ")
partida = input("Digite o horario da partida: ")

# converter a string para uma lista
chegada = chegada.split(" ")
partida = partida.split(" ")

# conversao de string para inteiro do dados
hora_chegada = int(chegada[0])
min_chegada = int(chegada[1])

hora_partida = int(partida[0])
min_partida = int(partida[1])

# converter as horas para minutos e somar com os minutos
mins_chegada = hora_chegada * 60 + min_chegada
mins_partida = hora_partida * 60 + min_partida

# Calculo da diferenca do horario de chega e de partida em minutos
dif_partida_chegada = mins_partida - mins_chegada

qtd_hora = int(dif_partida_chegada / 60)
qtd_min = dif_partida_chegada % 60

valor_pagar = 1

if 60 < dif_partida_chegada < 121:
    valor_pagar += 1
elif 120 < dif_partida_chegada < 181:
    valor_pagar += 2.4
elif 180 < dif_partida_chegada < 241:
    valor_pagar += 3.8
elif dif_partida_chegada > 240 and qtd_min == 0:
    valor_pagar = 4.8 + 2 * (qtd_hora - 4)
elif dif_partida_chegada > 240 and qtd_min != 0:
    valor_pagar = 4.8 + 2 * (qtd_hora - 3)
elif dif_partida_chegada <= 0:  # Caso a pessoa fique de um dia para outro nao ultrapassando as 24 hrs
    dif_partida_chegada = (24 * 60) - mins_chegada + mins_partida  # converte quando dá 00 horas
    qtd_hora = int(dif_partida_chegada / 60)
    qtd_min = dif_partida_chegada % 60
    if dif_partida_chegada > 240 and qtd_min == 0:
        valor_pagar = 4.8 + 2 * (qtd_hora - 4)
    elif dif_partida_chegada > 240 and qtd_min != 0:
        valor_pagar = 4.8 + 2 * (qtd_hora - 3)

print(f"Valor a pagar: R$ {valor_pagar:.2f}")
print(f"Tempo passado: {qtd_hora}:{qtd_min:02d}")  # {:02d}: 0 - indica que tem zero na frente, 2: 2 casas, d: inteiro
