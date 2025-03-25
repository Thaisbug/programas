# Matrícula de Alunno
alunos_matriculados = {
    "12345": {"nome": "João Silva", "matricula": True},
    "67890": {"nome": "Maria Oliveira", "matricula": True},
    "11223": {"nome": "Carlos Souza", "matricula": False},
    "44556": {"nome": "Ana Santos", "matricula": True},
}

def verificar_matricula(codigo_aluno):
    # Verifica se o código do aluno está no dicionário
    if codigo_aluno in alunos_matriculados:
        # Retorna se a matrícula é verdadeira ou falsa
        return alunos_matriculados[codigo_aluno]["matricula"]
    else:
        return False  # Caso o aluno não exista no sistema

# Exemplo de uso
codigo_aluno = input("Digite o código do aluno para verificar a matrícula: ")

# Verifica a matrícula e imprime o resultado
if verificar_matricula(codigo_aluno):
    print("O aluno está matriculado.")
else:
    print("O aluno não está matriculado ou o código não é válido.")