nome = input("Qual o nome do produto?")
preco = float(input("Qual o preço do produto?"))

if(preco < 50):
  print("Produto " + nome + " tem preço baixo" )
elif(preco > 100):
  print("Produto " + nome + " tem preço alto" )
else:
  print("Produto " + nome + " tem preço médio" )

