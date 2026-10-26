"""Enunciado: Implemente o motor de descontos de uma loja com as seguintes regras:
Pagamento à Vista (Tipo 1):
Se o valor da compra for > R$ 500.00, aplique 15% de desconto.
Caso contrário, aplique 5% de desconto.
Pagamento Parcelado (Tipo 2):
Não há desconto (valor final é o valor da compra).
Especificações:
Entradas: valor_compra (float) e tipo_pagamento (int).
Saída: Valor do desconto aplicado e o valor total final a pagar.
Dica Pythonica: "Explícito é melhor que implícito". Use nomes descritivos como valor_com_desconto em vez de v1. Além disso, certifique-se de tratar o tipo_pagamento explicitamente para garantir que a lógica do parcelamento (Tipo 2) não receba descontos indevidos."""

valor_compra = float(input("Informe o valor da compra: \n"))
tipo_pagamento = int(input("Informe o código da forma de pagamento (1) - À Vista \t (2) - Parcelado: \n"))

if tipo_pagamento == 1 and valor_compra > 500:
    subtotal = (valor_compra * 0.85)
    print(f"O valor da compra é de: R${subtotal:.2f}")
elif tipo_pagamento == 1 and valor_compra <= 500:
    subtotal = (valor_compra * 0.95)
    print(f"O valor da compra é de: R${subtotal:.2f}")
else:
    print(f"O valor da compra é de: R${valor_compra:.2f}")