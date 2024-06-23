opcao = 's'

while opcao != 'n':
  
  try:
    peso = float(input('Digite seu peso (0.00 kg): '))
    altura = float(input('Digite sua altura (0.00 m): '))
    imc = peso / (altura * altura)

    print('==================================')
  
    if imc < 16:
      print(f'Seu IMC é {imc:.2f} — Magreza grave')
    elif imc < 16 and imc <= 16.9:
      print(f'Seu IMC é {imc:.2f} — Magreza moderada')
    elif imc > 17 and imc <= 18.5:
      print(f'Seu IMC é {imc:.2f} — Magreza leve')
    elif imc > 18.6 and imc <= 24.9:
      print(f'Seu IMC é {imc:.2f} — Peso ideal')
    elif imc > 25 and imc <= 29.9:
      print(f'Seu IMC é {imc:.2f} — Sobrepeso')
    elif imc > 30 and imc <= 34.9:
      print(f'Seu IMC é {imc:.2f} — Obesidade grau I')
    elif imc > 34.9:
      print(f'Seu IMC é {imc:.2f} — Obesidade morbida')
      
    print('==================================')
  except:
    print('Valor digitado invalido! ')
      
  opcao = str(input('Deseja continuar? s/n: '))
  # CRIAR O EXECUTAVELCOM O CX_FREEZA
  # cxfreeze imc.py --target-dir calculadora-imc
  # https://www.alura.com.br/artigos/criando-um-executavel-a-partir-de-um-programa-python?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=111087461203&hsa_ad=687448474447&hsa_src=g&hsa_tgt=dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwsaqzBhDdARIsAK2gqncSG3jWIUyFqdDHAbUIZdnxhc0HAjJYr7g-Tg7zkJGwtqsiPxTzSiIaAiZpEALw_wcB
  