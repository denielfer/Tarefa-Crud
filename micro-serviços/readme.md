# Solução Microsserviço
Esta solução em microsserviço, para emular diversas maquinas foi usado o docker ( sendo criado um docker-compose para falicitar a criação das maquinas ), assim temos 2 projetos, Frontend usando React e Backend com FastAPI, com um banco de dasdos MySQL.

## Tecnologias:
 - [Docker](https://www.docker.com/products/docker-desktop/): 4.26.1 
 - [NPM](https://nodejs.org/en/download): 8.13.1
 - React: 18.2.0
 - [Python](https://www.python.org/downloads/): 3.10.4 
 - FastAPI:0.109.0 
 - SQLAlchemy: 2.0.25

Aqui temos o docker para virtualizar as maquinas, NPM para gerenciar os pacotes do front, que é um projeto react, FastAPI no back com SQLAchemy de ORM e um banco de dados MySQL.

## Como inicializar

### Docker
Com o doquer é nescessario inicial mente criar a rede externa a primeria vez assim, executamos, primeiro:

```powershell
    docker network create tarefa
```
Para criar a rede externa que sera usada pelo front e back.
Então podemos subir as maquinas no docker, na pasta micro-serviços:
```powershell
    docker docker-compose up
```
Ao executar esse comando as maquinas serão iniciadas, porém ocorrera um problema com o backend, o qual tentara se conectar ao Banco de Dados, porém este demora um pouco mais a iniciar assim havera falha na sua inicialização, sendo nescessario reinia-lo. Note que este problema so acontece quando inicializamos o Banco de dados e o BackEnd ao "mesmo tempo".

Então terremos o FrontEnd rodando em: http://localhost:3000/ e o BackEnd em:  http://localhost:8000/

### Não Docker
Nescessario ter python instalado na maquina que rodara o servidor BackEnd e NPM na maquina FrontEnd.

1- Banco de Dados

 Criamos o servidor MySQL, criamos uma DataBase chamada 'mysqldb' e iniciamos com o [script base](https://github.com/denielfer/Tarefa-Crud/tree/main/micro-servi%C3%A7os/init_db). Este cria na DataBase 'mysqldb' a tabela de tarefa e um usuario que sera usado pelo back para manipular os dados.

2- BackEnd

Como esta solução foi criada para ser executada no Docker é nescessario fazer um ajuste antes de executar o projeto BackEnd. No arquivo de [configuração](https://github.com/denielfer/Tarefa-Crud/blob/main/micro-servi%C3%A7os/backend/Tarefas/setting.py) é nescessario altera os valores terornados nas linhas 22 a 26, para os valores desejados ( usuario e senha criados no script de inicialização, que estao presentes no .env, o host e path da DataBase ).

Com estas auterações feitas na pasta 'backend':
```powershell
   pip install -r requirements.txt 
   uvicorn Tarefas.main:app --host 0.0.0.0 --port 8000 --log-config log.ini
```
Assim teremos o server sendo iniciado na porta 8000, no local host e os logs sendo escritos em 'logfile.log'

3- FrontEnd

Na pasta 'frontend' executamos:
```powershell
    npm install
    npm start
```

Então terremos o FrontEnd rodando em: http://localhost:3000/ e o BackEnd em:  http://localhost:8000/

## Rotas:
### FrontEnd
 - '/' : Temos pagina inicial com a lista de tarefas caregadas do banco
 - '/tarefa/' : Pagina de Adição de tarefa
 - '/tarefa/{id}' : Pagina de Edição da tarefa com id={id}

### BackEnd
 - '/tarefa/', GET : Lista de todas as tarefas do banco, com todos os seus dados
 - '/tarefa/{id}, GET: Todos os dados da tarefa com id={id}
 - '/tarefa/{id}, DELETE: Deleta tarefa com id={id}
 - '/tarefa/', POST: Cria uma nova Tarefa com dados passados no corpo da request.
 - '/tarefa/{id}/', PUT: Altera os dados da tarefa com id={id} para os passados no corpo da request.
 - '/tarefa/slice/{start}/{limit}', GET: Lista de tarefas que começa em {start} e termina em {limit}, se existirem, das tarefas, ordenadas por criação.
 
## Como usar
Nesta primeira imagem temos a pagina inicial do FrontEnd.

![Alt Text](img/home.png)

Nesta pagina temos 4 elementos:

1 - Botão comun a todas as paginas para ir a pagina inicial
2 - Lista de tarefas cadastradas
3 - Botão para adicionar uma nova tarefa
4 - Cada item da lista de tarefas pode ser clicado para expandir e mostra a descrição

Assim ao clicarmos em um item temos:

![Alt Text](img/home1.png)

Aqui temos a expanção de 1 card que tras:

1 - Card onde mostra o comentario
2 - Botao para editar tarefa
3 - Botão para deletar tarefa


### Adição

Na pagina inicial ao clicar o botao de Adicionar item, somos redirecionados a pagina de adição

![Alt Text](img/adição.png)

A qual apos prenchermos titulo e Data podemos enviar no botao enviar, que ficara verde ao preenchermos todos os dados. Caso não tenha sido preenchido Titulo ou Data o envio não sera efetuado, com os campos informando o dado ausente. Ao finalizarmos o envia somos redirecionado a pagina inicial.

### Visualizar

Na pagina inicial temos todas as Tarefas cadastradas, para ver a descrição de uma delas, clicamos no seu item da lista.

### Editar

Para editar uma tarefa é aberto o card da tarefa desejada, na pagina inicial, e preciona o botão de edição. Sendo redirecionado a uma pagina similar de criação, com os dados pre-caregados, então após editar os dados, clica-se em enviar, recebendo uma confirmação que a tarefa foi editada e sendo redirecionado a pagina inicial.

### Deletar

Para deletar uma tarefa abrimos o card da tarefa desejada, na pagina inicial, e preciona o botão de deletar.

## Comentarios

Esta solução ja trás uma api que pode ser disponibilizada ou integrada a um serviço, porém sem fatores de segurança.

Atravez dessa mostramos como poderia ser uma solução em microsserviço, que poderia ser facilmente incorporada a um serviço ja existende e modularizado para facil escalabilidade.

### Arquitetura:
Nesta aquitetura temos o docker para simular a interação de 3 maquinas com 2 redes. Comforme:

![Alt Text](img/arquitetura.png)

Aqui temos a ideia de ter uma rede internet para isolar o banco de dados, para ser acessado somente por maquinas predeterminadas, neste caso o BackEnd e em um cenario real uma maquina de administrador de banco de dados, e uma rede externa que seria a coneção usada do BackEnd e FrontEnd com a internet padrão, pela qual os usuarios acessariam.