# Para criar um ambiente virtual: pip install virtualenv -> virtualenv nome_do_ambiente -> nome_do_ambiente\Scripts\activate ou source nome_do_ambiente/bin/activate para MAC
# Biblioteca necessárias(cole os dois códigos no cmd): pip install pandas / pip install openpyxl

import pandas as pd

# Lendo o arquivo Excel
df = pd.read_excel('alunos.xlsx')


# Limpando CPF
def limpar_cpf(cpf):
    cpf_limpo = str(cpf).replace(".", "").replace("-", "").replace(" ", "").zfill(11)
    return cpf_limpo

# Limpando Turma
def limpar_turma(turma):
    turma_limpo = str(turma).replace("°", "º").replace(" ", "")
    return turma_limpo

df['username'] = df['cpfcgc'].apply(limpar_cpf)

df['turma'] = df['turma'].apply(limpar_turma)

# Renomeando as colunas
df = df.drop('cpfcgc', axis=1).rename(columns={'aluno': 'name', 'emailpes': 'email', 'turma': 'group'})

# Criando colunas de firstname e lastname
df[['firstname', 'lastname']] = df['name'].str.split(n=1, expand=True)

# Cria as colunas course
# Adicione aqui as correspondências entre os dados da coluna "turma" e os courses das disciplinas
course_dict = {"ENF1ºNOT": ["EXEMPLO DE CURSO", "EXEMPLO DE CURSO", "EXEMPLO DE CURSO", "EXEMPLO DE CURSO", "EXEMPLO DE CURSO", "EXEMPLO DE CURSO", "EXEMPLO DE CURSO", "EXEMPLO DE CURSO", "EXEMPLO DE CURSO"],
               "ENF1ºMAT": ["", "", "", "", "", "", "", "", ""]}

# Criando as colunas de course e group
df[['course1', 'course2', 'course3', 'course4', 'course5', 'course6', 'course7', 'course8', 'course9']] = df['group'].apply(lambda x: pd.Series(course_dict.get(x, [""]*9)))
df['group1'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group2'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group3'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group4'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group5'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group6'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group7'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group8'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
df['group9'] = df['group'].apply(lambda x: x.split('º')[0] + 'ºMATUTINO' if x.endswith('MAT') else x.split('º')[0] + 'ºNOTURNO')
# Aqui é possível adicionar mais colunas de group conforme a necessidade

#Criando senha padrão
df['password'] = 'suasenha'

# Criando o arquivo CSV com as colunas desejadas
df.to_csv('alunos_ava_solucionado.csv', columns=['username', 'firstname', 'lastname', 'email', 'course1', 'course2', 'course3', 'course4', 'course5', 'course6', 'course7', 'course8', 'course9', 'group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7', 'group8', 'group9', 'password'], index=False)

print("O polimento da planilha para adicionar no moodle foi concluída.")