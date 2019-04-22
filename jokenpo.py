# coding: utf-8

# In[5]:

def main():
	print('{:=^40}'.format(' JOKENPÔ GAME '))
	print('''ESCOLHA UMA DAS OPÇÕES
		[ 1 ] - PEDRA
		[ 2 ] - PAPEL
		[ 3 ] - TESOURA''')
	itens = ('', 'PEDRA', 'PAPEL', 'TESOURA')	
	jogada_computador = randint(1, 3)
	pontos_usuario = 0
	pontos_computador = 0
	cls = lambda: os.system('cls')
	while pontos_computador <= 1 and pontos_usuario <= 1:
		try:
			jogada = int(input('Qual sua jogada? '))
			print('JO')
			sleep(1)
			print('KEN')
			sleep(1)
			print('PO!')
			sleep(1)
			print('-=' * 10)
			print(f'O usuário jogou {itens[jogada]}')
			print(f'O computador jogou {itens[jogada_computador]}')		
			print('-=' * 10)			
			
		except:
			if jogada != 1 or jogada != 2 or jogada != 3:
				print('Digite uma opção válida (1/2/3)!')
				print('Tente novamente')				
				continue
		try:
			if jogada == 1:
				if jogada_computador == 1:				
					print('Empate!')					
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)
				elif jogada_computador == 2:					
					print('Papel ganha de pedra!')					
					print('Vitória do computador!')
					pontos_computador = pontos_computador + 1
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)
				elif jogada_computador == 3:					
					print('Pedra ganha de tesoura!')					
					print('Vitória do usuário!')
					pontos_usuario = pontos_usuario + 1
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)
				else:
					print('Jogada inválida!')
			elif jogada == 2:

				if jogada_computador == 1:
					print('Papel ganha de pedra!')					
					print('Vitória do usuário')
					pontos_usuario = pontos_usuario + 1
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)				
				
				elif jogada_computador == 2:					
					print('Empate!')					
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)
				
				elif jogada_computador == 3:					
					
					print('Tesouda ganha de papel')					
					print('Vitória do Computador!')
					pontos_computador = pontos_computador + 1
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)
				else:
					print('Jogada inválida!')
				
			elif jogada == 3:
				if jogada_computador == 1:
					print('Pedra ganha de tesoura!')
					print('Vitória do computador')					
					pontos_computador = pontos_computador + 1
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)
				
				
				elif jogada_computador == 2:					
					print('Tesoura ganha de papel')
					print('Vitória do usuário!')					
					pontos_usuario = pontos_usuario + 1
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')					
					print('\n' * 5)
				
				elif jogada_computador == 3:					
					print('Empate!')
					print(f'PLACAR: usuário {pontos_usuario} x computador {pontos_computador}')									
					print('\n' * 5)
				else:
					print('Jogada inválida!')			
				
		except:
			pass

	cls()
	print('-=' * 15)
	print('-=' * 15)
	print('JOGO FINALIZADO')
	print(f'PLACAR: Usuário {pontos_usuario} X Computador {pontos_computador}')
	print('-=' * 15)
	print('-=' * 15)
	if pontos_usuario > pontos_computador:
		print('USUÁRIO VENCEU!')
	else:
		print('COMPUTADOR VENCEU!')
		
main()
