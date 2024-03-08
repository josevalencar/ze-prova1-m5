# Instruções 

1. Instalar o venv com o comando 'python -m venv venv'
2. Ativá-lo com 'venv\Scripts\activate'
3. Instalar os requirements com 'pip install requirements.txt'
4. Rodar o app.py com o comando 'python app.py' no diretório raiz

# Rotas de navegação

●      /novo: cadastra um novo conjunto de pontos em um caminho

●      /pegar_caminho/id: recebe o id do caminho e devolve os pontos cadastrados nele

●      /listas_caminhos: retorna o id e o nome de todos os caminhos cadastrados

●      /atualizar/id: atualiza o caminho cujo id foi fornecido

●      /deletar/id: deleta o caminho com o id fornecido