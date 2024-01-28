# Solução monolito
Esta solução é feita em monolito, usando o Framework Django, com a database padrão de SQLite. 

## Tecnologias
 - [Python](https://www.python.org/downloads/): 3.10.4 
 - [Django](https://www.djangoproject.com/) : 5.0.1
 - [SQLite](https://www.sqlite.org/index.html): 3 

## Como inicializar
Dentro do repositório django-monolito, é necessário instalar as dependências ( de preferência em um ambiente virtual ):
```powershell
   pip install -r requirements.txt 
```
Como o banco de dados não vem atualizado do git, precisamos executar as alterações no banco, usando:
```powershell
   python .\UnMEP\manage.py migrate 
```
e por fim para iniciar o servidor:
```powershell
   python .\UnMEP\manage.py runserver 
```
O projeto será executado no local host na porta 8000, portanto acessamos pelo link:
http://127.0.0.1:8000/tarefas/

## Como usar
Na imagem abaixo temos a página principal, onde todas as operações podem ser feitas.

![Alt Text](img/pagina_inicial.png)

Nesta página temos 4 elementos:

1 - Lista de tarefas cadastradas
2 - Botão para editar tarefa
3 - Botão para deletar tarefa
4 - Formulário de adição/edição de tarefa


### Adição

Para adicionar uma tarefa é necessário digitar o título, data e descrição desta tarefa, e selecionar o estados, por fim clicando em salvar

### Visualizar

As tarefas têm suas informações apresentadas na lista de tarefas, com exceção da descrição, que para ser visualizada é necessário clicar em editar e este será carregado no campo de descrição

### Editar

Clique no botão ‘Editar’ da tarefa desejada. As informações da tarefa serão carregadas no formulário (item 4), onde você poderá realizar as edições necessárias. Para salvar as alterações, clique no botão ‘Editar’ do formulário.

### Deletar

Para deletar uma tarefa clica-se no botão deletar do formulário.


## Comentários
Nesta solução não existe uma API pronta para ser disponibilizada a um cliente ou integrada a um serviço diretamente, uma vez que o CSRF (Cross-Site Request Forgery) está ativo, para este poder ser disponibilizado seria necessário remover o CSRF destas rotas e torna as respostas um json, uma vez que a resposta está sendo uma página web.

Essa solução foi feita para mostrar a possibilidade de um monolito que possa ser melhorado futuramente, apresentando assim uma solução nesta arquitetura.

Uma outra melhoria seria desacoplar o banco da máquina fazendo integração com um externo, uma vez que esta solução usa o SQLite criado automático pelo Django.

### Arquitetura:
Nesta arquitetura temos em uma máquina toda a aplicação.

![Alt Text](img/arquitetura.png)
