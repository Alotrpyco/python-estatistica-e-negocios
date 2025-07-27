#Declarando as variáveis

nome_produto = input("Coloque o nome do produto:")
quantidade_estoque = input("Coloque a quantidade em estoque:")
quantidade_estoque = float(quantidade_estoque)
preco_compra = input("Coloque o preço de compra:")
preco_compra = float(preco_compra)
preco_venda = input("coloque o preço de venda:")
preco_venda=float(preco_venda)

#calculando o lucro por unidade

lucro_unidade = preco_venda-preco_compra

lucro_total = lucro_unidade*quantidade_estoque

print("lucro por unidade de", nome_produto, ":", lucro_unidade )
print("lucro total:", lucro_total)