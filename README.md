Projeto para fins educativos: Aplicação de Pesquisa de Produtos em Python com Tkinter e PostgreSQL

Esse software ainda não atende totalmente ao conceito SCRUD, pois só faz leitura, mas pretendo implementar gravação em um futuro próximo.

Este repositório contém o código fonte de uma aplicação Python simples para pesquisar produtos em um banco de dados PostgreSQL. A aplicação possui uma interface gráfica intuitiva que permite ao usuário buscar produtos por ID ou por palavra-chave. Os resultados da pesquisa são exibidos em uma tabela ordenável.

**Instruções**:

  1. Primeiramente, instale as dependências para rodar o software:

       ```pip install tkinter psycopg2```

  2. Configure o arquivo ```db.py```:

       • Edite o arquivo ```db.py``` e substitua os valores de ```dbname```, ```user```, ```password```, ```host``` e ```port``` pelas informações corretas do seu banco de dados PostgreSQL.

  4. Execute o software:
       ```python gui.py```

**Como funciona**:

  • A aplicação conecta-se ao banco de dados PostgreSQL utilizando a biblioteca psycopg2.
  • O usuário pode realizar pesquisas por ID ou por palavra-chave.
  • A pesquisa é realizada no banco de dados e os resultados são exibidos em uma tabela na interface gráfica.
  • A tabela pode ser ordenada por qualquer coluna clicando no cabeçalho da coluna.

**Contribuições serão muito bem-vindas!** Para contribuir, por favor, comente e sugira aprimoramentos. Lembrando novamente que esse projeto é para fins exclusivamente acadêmicos, portanto, o foco não está necessariamente em produzir um software de nível empresarial.

**Informações Adicionais**:

Banco de dados: A aplicação utiliza um banco de dados PostgreSQL. É necessário ter um banco de dados criado e configurado antes de executar a aplicação.
Tabela: A aplicação espera encontrar uma tabela chamada "produto" com os campos "id", "nome" e "valor".
Requisitos: Python 3.x, Tkinter, psycopg2.
