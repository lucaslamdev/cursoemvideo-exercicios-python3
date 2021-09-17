from random import choice
primeiroAluno = input('Digite nome do primeiro aluno: ')
segundoAluno = input('Digite nome do segundo aluno: ')
terceiroAluno = input('Digite nome do terceiro aluno: ')
quartoAluno = input('Digite nome do quarto aluno: ')
alunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
sorteio = choice(alunos)
print(f'O aluno sorteado para apresentar será o/a {sorteio}.')
