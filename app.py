# Alertar e pedir informações  no pyautogui
import pyautogui

#pyautogui.alert(text='iniciando sua automação',title='automação de login',button='ok')
#pyautogui.prompt(text='digite seu email',title='informação obrigatória')
#print(f'você digitou{email}')
# confirmar se algo deve ou não acontecer
resposta = pyautogui.confirm(text='continuar rodando nossa automação?',title='confirmação',buttons=['sim','não','cancelar'])
if resposta == 'sim':
    print('continuar automação')
elif resposta == 'não':
    print('encerrando automação')
else:
    print('operação cancelada')