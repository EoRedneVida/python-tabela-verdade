incognitas = int(input('Digite 1 para 1 incognita, 2 para 2 incognitas e 3 para 3 incognitas: '))
if incognitas == 1:
    print('Se a sua incognita tiver o valor TRUE atribuido a ela o resultado final sera TRUE\n Se sua incognita tiver o valor FALSE atribuido a ela o resultado final será Falso')
elif incognitas == 2:
    condicao = int(input('Escolha o conectivo entre suas variaveis: 1 para ^, 2 para v, 3 para -> e 4 para <-> '))
    if condicao == 1:
        print ('Na equação A ^ B: \n Se A for TRUE e B for TRUE seu resultado final será TRUE\n Se A for TRUE e B for FALSE seu resultado final será FALSE\n Se A for FALSE e B for TRUE seu resultado final será FALSE\n Se A for FALSE e B for FALSE seu resultado final será FALSE')
    elif condicao == 2:
        print ('Na equação A v B: \n Se A for TRUE e B for TRUE seu resultado final será TRUE\n Se A for TRUE e B for FALSE seu resultado final será TRUE\n Se A for FALSE e B for TRUE seu resultado final será TRUE\n Se A for FALSE e B for FALSE seu resultado final será FALSE')
    elif condicao == 3:
        print ('Na equação A -> B: \n Se A for TRUE e B for TRUE seu resultado final será TRUE\n Se A for TRUE e B for False seu resultado final será FALSE\n Se A for FALSE e b For TRUE seu resultado final será TRUE\n Se A for FALSE e B for FALSE seu resultado final será TRUE')
    elif condicao == 4:
        print ('Na equação A <-> B: \n Se A for TRUE e B for TRUE seu resultado final será TRUE\n Se A for True e B for FALSE seu resultado final será FALSE\n Se A for FALSE e B for TRUE seu resultado final será FALSE\n Se A for FALSE e B for FALSE seu resultado final será TRUE')
    else:
        print ('Digite um valor válido por favor!!')
elif incognitas == 3:
    print ('Sua equação é (A_B)_C: escolha seu conectivos entre A e B e depois escolha seu conectivo entre C')
    condicao1 = int(input('Escolha seu conectivo entre A e B: 1 para ^, 2 para v, 3 para -> e 4 para <-> '))
    condicao2 = int(input('Escolha seu conectivo entre o resultado do parênteses e C: 1 para ^, 2 para v, 3 para -> e 4 para <-> '))
    if condicao1 == 1 and condicao2 == 1:
        print ('Na equação (A ^ B) ^ C: \n Se A for TRUE, B for TRUE e C for TRUE seu resultado final será TRUE\n Se tiver ao menos uma incognita com valor FALSE o resultado final será FALSE')
    elif condicao1 == 1 and condicao2 == 2:
        print ('Na equação (A ^ B) v C: \n Se A for TRUE e B for TRUE o C pode ter qualquer valor pois o resultado final será TRUE independente de qual valor for atribuido a C\n Se A ou B forem FALSE e C for TRUE seu resultado final será TRUE\n Se A ou B forem FALSE e C for FALSE seu resultado final será FALSE')
    elif condicao1 == 1 and condicao2 == 3:
        print ('Na equação (A ^ B) -> C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE \n Se A e B forem TRUE e C for FALSE seu resultado final será FALSE\n Se A ou B forem FALSE o valor de C não importa pois o resultado final será TRUE independentemente do valor atribuido a C')
    elif condicao1 == 1 and condicao2 == 4:
        print ('Na equação (A ^ B) <-> C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A e B forem TRUE e C for FALSE seu resultado final será FALSE\n Se A ou B forem FALSE e C for TRUE seu resultado final será FALSE\n se A ou B forem FALSE e C for FALSE seu resultado final será TRUE')
    elif condicao1 == 2 and condicao2 == 1:
        print ('Na equação (A v B) ^ C: \n Se A ou B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A ou B forem TRUE e C for FALSE o resultado final será FALSE\n Se A e B forem FALSE o C pode ter qualquer valor pois o resultado final será FALSE independentemente de qual valor o C tiver ')
    elif condicao1 == 2 and condicao2 == 2:
        print ('Na equação (A v B) v C: \n Se A ou B forem TRUE o C pode ter qualquer valor pois o resultado final será TRUE independentemente do valor de C\n Se A e B forem FALSE e C for TRUE seu resultado final será TRUE\n Se A e B forem FALSE e C for FALSE seu resultado final será FALSE')
    elif condicao1 == 2 and condicao2 == 3:
        print ('Na equação (A v B) -> C: \n Se A ou B for TRUE e C for TRUE seu resultado final será TRUE\n Se A ou B forem TRUE e C for FALSE seu resultado final será FALSE\n Se A e B forem FALSE o C pode ter qualquer valor pois o resultado final será TRUE independentemente de qual valor o C tiver')
    elif condicao1 == 2 and condicao2 == 4:
        print('Na equação (A v B) <-> C: \n Se A ou B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A ou B forem TRUE e C for FALSE seu resultado final será FALSE\n Se A e B forem FALSE e C for TRUE seu resultado final será FALSE\n Se A e B forem FALSE e C for FALSE seu resultado final será FALSE')
    elif condicao1 == 3 and condicao2 == 1:
        print ('Na equação (A -> B) ^ C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A for True e B for FALSE o C pode ter qualquer valor que o resultado final será FALSE independentemente de qual seja o seu valor\n Se A for FALSE, B for True e C for TRUE seu resultado final será TRUE\n Se A for FALSE, B for FALSE e C for TRUE seu resultado final será TRUE\n Se C for FALSE A e B podem tere qualquer valor pois o resultado final será FALSE independentemente de qual valor esteja atribuido')
    elif condicao1 == 3 and condicao2 == 2:
        print ('Na equação (A -> B) v B: \n Se A e B forem TRUE o C pode ter qualquer valor pois o resultado final será TRUE independentemente de qual valor seja atribuido a ele\n Se A for TRUE, B for FALSE e C for TRUE seu resultado final será TRUE\n Se A for TRUE, B for FALSE e C for FALSE seu resultado final será FALSE\n Se A for false B e C podem ter qualquer valor pois o resultado final será TRUE independentemente de qual valor seja atribuido a eles')
    elif condicao1 == 3 and condicao2 == 3:
        print('Na equação (A -> B) -> C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A e B forem TRUE e C for FALSE seu resultado final será FALSE\n Se A for TRUE e B for FALSE C pode ter qualquer valor pois o resultado final será TRUE\n Se A for FALSE B e C podem ter qualquer valor pois o resultado final será TRUE')
    elif condicao1 == 3 and condicao2 == 4:
        print('Na equação (A -> B) <-> C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A e B forem TRUE e C for false o resultado final será FALSE\n Se A for TRUE, B for FALSE e C for TRUE o resultado final será FALSE\nSe A for TRUE, B for FALSE e C for FALSE o resultado final será TRUE\n Se A for FALSE, B for TRUE e C for TRUE o resultado final será TRUE\n Se A for FALSE, B for FALSE e C for FALSE o resultado final será FALSE ')
    elif condicao1 == 4 and condicao2 == 1:
        print('Na equação (A <-> B) ^ C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A e B forem FALSE e C for TRUE o resultado final será TRUE\n Se A for TRUE e B for FALSE ou vice versa o C pode ter qualquer valor que o resultado final será FALSE ')
    elif condicao1 == 4 and condicao2 == 2:
        print('Na equação (A <-> B) v C: \n Se A e B forem TRUE o C pode ter qualquer valor pois o resultado final será TRUE\n se C for TRUE A e B podem ter qualquer valor pois o resultado final será TRUE\n Se A for TRUE e B for FALSE ou vice e versa e C for FALSE o resultado final será FALSE')
    elif condicao1 == 4 and condicao2 == 3:
        print ('Na equação (A <-> B) -> C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A e B forem TRUE e C for FALSE o resultado final será FALSE\n Se A for TRUE e B for false ou vice e versa o C pode ter qualquer valor pois o resultado final será TRUE')
    elif condicao1 == 4 and condicao2 == 4:
        print('Na equação (A <-> B) <-> C: \n Se A e B forem TRUE e C for TRUE seu resultado final será TRUE\n Se A e B forem TRUE e C for FALSE seu resultado final será FALSE\n Se A for TRUE e B for FALSE ou vice e versa C for FALSE seu resultado final será FALSE\n Se A for TRUE e B for FALSE ou vice e versa e C for FALSE seu resultado final será TRUE')
    else:
        print('Digite um valor válido!!!')
else: 
    print('Digite um valor válido!!!!!!')    