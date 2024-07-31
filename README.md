# Cadastro de Produtor Rural

Este projeto é uma aplicação Flask para cadastro de produtores rurais. A aplicação permite cadastrar, editar e excluir produtores, além de gerar relatórios e dashboards sobre as fazendas cadastradas. A aplicação utiliza PostgreSQL como banco de dados e pode ser executada utilizando Docker.

## Funcionalidades

- Cadastro de produtores rurais com validação de CPF e CNPJ
- Edição e exclusão de produtores
- Dashboard com gráficos e relatórios sobre as fazendas
- Validação de áreas da fazenda (área total, área agricultável e área de vegetação)

## Tecnologias

- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Docker

## Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.9 ou superior (para desenvolvimento local fora do Docker)

## Configuração

### 1. **Configuração com Docker**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/usuario/repo.git
   cd repositorio

1. **Crie e inicie os contêineres com Docker Compose:**
   `docker-compose up --build`
