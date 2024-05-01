# Polimento de Planilha para Moodle

Este script em Python é utilizado para polir e formatar uma planilha de dados de alunos, tornando-a compatível com a importação no Moodle, um sistema de gerenciamento de aprendizado amplamente utilizado.

## Pré-requisitos
Antes de executar este script, certifique-se de ter as seguintes bibliotecas Python instaladas:
- Pandas
- Openpyxl

Você pode instalá-las executando os seguintes comandos no terminal:

pip install pandas
pip install openpyxl

## Como usar
1. Clone este repositório ou baixe o script Python.
2. Crie um ambiente virtual (opcional, mas recomendado):
    ```
    pip install virtualenv
    virtualenv nome_do_ambiente
    nome_do_ambiente\Scripts\activate  # para Windows
    source nome_do_ambiente/bin/activate  # para macOS/Linux
    ```
3. Execute o script Python:
    ```
    python nome_do_script.py
    ```
4. Após a execução bem-sucedida, você encontrará o arquivo CSV polido como `alunos_ava_solucionado.csv`.

## Descrição do Script
- O script lê um arquivo Excel `alunos.xlsx`.
- Limpa os CPFs e turmas dos alunos.
- Renomeia e divide o nome do aluno em "firstname" e "lastname".
- Cria as colunas de cursos e grupos com base em um dicionário de correspondências.
- Cria senhas padrão para os alunos.
- Exporta os dados polidos para um arquivo CSV compatível com o Moodle.

## Notas
- Certifique-se de fornecer o arquivo Excel `alunos.xlsx` na mesma pasta que o script.
- Você pode ajustar o dicionário `course_dict` conforme necessário para corresponder aos seus cursos e grupos.
- As senhas padrão podem ser alteradas conforme suas políticas de segurança.

Após a execução bem-sucedida do script, você pode importar o arquivo CSV resultante para o Moodle para gerenciar os dados dos alunos.
