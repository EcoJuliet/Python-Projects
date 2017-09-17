#jogo de perguntas e respostas

aqui = []
print('Quanto é 1+1')
resp1 = input()

if (resp1 == 2):
    print('Correto!')
    print("Proxima pergunta...")
    aqui.append('x')
else:
    print('Resposta errada!')

print('Quanto é 2+2?')
resp2 = input()
          
if (resp2 == 4):
    print('Acertou!')
    aqui.append('x')
else:
    print('Porra, mas tu é burro mesmo né?')

print('A quantidade de respostas corretas é:')
print(aqui)
    
