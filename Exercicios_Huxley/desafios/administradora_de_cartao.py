"""Descrição
Uma administradora de cartões está oferecendo uma promoção aos seus clientes. A pessoa que não puder pagar o total da fatura no mês de março poderá pagar apenas 50% do valor, e o restante poderá ser pago no mês seguinte com juros de 6,5%. 

Desenvolva uma solução para ajudar o cliente a descobrir qual será o valor de sua fatura no mês de abril caso ele aceite a proposta. 

Formato de entrada

O valor da fatura do mês de março (tipo float).

Formato de saída

O valor total da fatura, valor a pagar em março e o valor a pagar em abril. Todos os valores formatados com duas casas decimais.

Atente para os exemplos apresentados."""

valor = float(input())

print(f"Valor total da fatura: R$ {valor:.2f}")
print(f"Valor a pagar em Marco: R$ {(valor / 2):.2f}")
print(f"Valor a pagar em Abril: R$ {((valor / 2) + (valor * 0.065)):.2f}")