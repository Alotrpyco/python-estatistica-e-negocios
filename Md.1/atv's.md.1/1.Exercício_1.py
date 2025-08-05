
#Criar variáveis para representar: Nome de um produto; Quantidade em estoque; Preço de compra; Preço de venda.

#Declarando variáveis
nome_produto = "morango"
quantidade_estoque = 250
preco_compra = 0.75
preco_de_venda = 2.50

#calculado o lucro por unidade e lucro total
lucro_unidade = preco_de_venda-preco_compra
lucro_total = quantidade_estoque*preco_de_venda

print("Lucro por unidade de", nome_produto, "é", lucro_unidade)
print("lucro total vendendo os 250 morangos é:", lucro_total)




