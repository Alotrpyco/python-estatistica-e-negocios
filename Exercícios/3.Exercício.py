# Declarando variáveis
# valores em R$ criados pela minha imaginação

produto1 = 'creatina'
preço_de_custo_produto1 = 25
preço_de_venda_produto1 = 80
quantidade_vendida_produto1 = 100
produto2 = 'whey'
preço_de_custo_produto2 = 75
preço_de_venda_produto2 = 85
quantidade_vendida_produto2 = 150
produto3 = 'bcaa'
preço_de_custo_produto3 = 50
preço_de_venda_produto3 = 76
quantidade_vendida_produto3 = 200
custo_fixo_mensal = 2000


#1.Calcular o lucro por unidade de cada produto
lucro_por_unidade_produto1 = preço_de_venda_produto1 - preço_de_custo_produto1
lucro_por_unidade_produto2 = preço_de_venda_produto2 - preço_de_custo_produto2
lucro_por_unidade_produto3 = preço_de_venda_produto3 - preço_de_custo_produto3
print("lucro de uma creatina vendida é", lucro_por_unidade_produto1)
print("lucro de um whey vendida é", lucro_por_unidade_produto2)
print("lucro de um bcaa vendida é", lucro_por_unidade_produto3)


#2.Calcular o lucro total de cada produto (lucro por unidade × quantidade)
lucro_total_produto1 = lucro_por_unidade_produto1 * quantidade_vendida_produto1
lucro_total_produto2 = lucro_por_unidade_produto2 * quantidade_vendida_produto2
lucro_total_produto3 = lucro_por_unidade_produto3 * quantidade_vendida_produto3
print("lucro total obtido com a venda da creatina é",lucro_total_produto1)
print("lucro total obtido com a venda do whey é", lucro_total_produto2)
print("lucro total obtido com a venda do bcaa é", lucro_total_produto3)


