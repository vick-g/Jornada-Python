# lista em python
lista = ["maçã", "banana", "laranja"]

# Pegar a informação na lista
posicao = lista[0]
print(posicao)  # maçã
# ou print(lista[0])  # maçã

# Adicionar uma informação na lista
lista.append("uva")
print(lista)  # ['maçã', 'banana', 'laranja', 'uva']

#dicionário em python
frutas = {"cor": "vermelha", "sabor": "doce", "preço": 2.5}

# Pegar a informação no dicionário
cor = frutas["cor"]
print(cor)  # vermelha

## como vamos usar essas informações no chatbot, vamos criar uma lista de mensagens e um dicionário para armazenar as informações do usuário.
# Cria a lista de mensagens
lista_mensagens = []

# Cria o dicionário para armazenar as informações do usuário
mensagem1 = {"role": "user", "content": "1"}
mensagem2 = {"role": "assistant", "content": "2"}


# Adiciona as mensagens na lista de mensagens
lista_mensagens.append(mensagem1)
lista_mensagens.append(mensagem2)


# Mostra a lista de mensagens
print(lista_mensagens)  # [{'role': 'user', 'content': '1'}, {'role': 'assistant', 'content': '2'}]