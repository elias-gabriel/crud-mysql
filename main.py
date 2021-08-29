import criar
import deletar
import ler
import atualizar

opcao = 0

while opcao != 5:
    print('''OPÇÕES [ 1 ] CRIAR [ 2 ] DELETAR  [ 3 ] LER [ 4 ] ATUALIZAR  [ 5 ] SAIR''')
    opcao = int(input('O QUE DESEJA FAZER?'))
    if opcao == 1:
        criar.Criar()
    elif opcao == 2:
        deletar.Deletar()
    elif opcao == 3:
        ler.consulta(IdUser=True)
    elif opcao == 4:
        atualizar.atualiza()
    else:
        print('Opção inválida')
print('Fim do programa, volte sempre')
print('=-=' * 10)
