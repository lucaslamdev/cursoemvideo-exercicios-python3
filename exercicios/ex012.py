preco = float(input('Qual o preço do produto? '))
desconto = float(5)
print(f'O preço do produto com {desconto:.0f}% de desconto será de R${float(preco-(preco*(desconto/100))):.2f}')
