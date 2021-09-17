from random import sample
primeiroAluno = input('Digite nome do primeiro aluno: ')
segundoAluno = input('Digite nome do segundo aluno: ')
terceiroAluno = input('Digite nome do terceiro aluno: ')
quartoAluno = input('Digite nome do quarto aluno: ')
alunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
sorteio = sample(alunos, k=4)
print(f'A ordem dos alunos sorteados foi {sorteio}.')
