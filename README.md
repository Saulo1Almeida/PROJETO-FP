
# 📚 Sistema de Gestão Escolar

## 🎯 Objetivo do Sistema

Este sistema foi desenvolvido para auxiliar escolas públicas e comunitárias na organização e gestão de seus recursos educacionais, alinhando-se diretamente ao Objetivo de Desenvolvimento Sustentável (ODS) 4: Educação de Qualidade. O software resolve o problema da gestão manual de dados escolares, oferecendo uma solução digital acessível para:

* Gestores escolares: Para administrar alunos, professores e turmas
* Secretarias: Para manter registros acadêmicos organizados
* Professores: Para acompanhar o desempenho dos alunos
* Comunidade escolar: Para ter transparência nos dados educacionais

## 🚀 Funcionalidades Principais

### 📋 Módulo de Gestão de Alunos (CRUD Completo)

* Cadastro de alunos com nome, matrícula única e vinculação a turmas
* Consulta individual com visualização de todas as notas
* Atualização de dados incluindo gerenciamento de notas por disciplina
* Exclusão segura com remoção automática de notas associadas
* Validação de matrículas duplicadas e dados inconsistentes

### 👨‍🏫 Módulo de Gestão de Professores (CRUD Completo)

* Registro de professores com disciplina específica
* Vinculação automática às turmas
* Proteção contra exclusão quando associado a turmas ativas
* Busca por disciplina para organização pedagógica

### 🏫 Módulo de Gestão de Turmas (CRUD Completo)

* Criação de turmas com professor responsável
* Visualização detalhada incluindo lista de alunos matriculados
* Impedimento de exclusão quando turma possui alunos
* Relações automáticas com alunos e professores

### 📊 Módulo de Relatórios

* Alunos por Turma: Lista organizada com agrupamento por turma
* Professores por Disciplina: Organização por área de atuação
* Notas dos Alunos: Relatório completo de desempenho acadêmico
* Exportação visual no terminal com formatação profissional

### 🗄️ Sistema de Banco de Dados

* SQLite integrado: Não requer servidor externo
* Backup automático: Dados persistidos em arquivo .db
* Estrutura normalizada: tabelas inter-relacionadas

## 💻 Instruções de Execução

### Pré-requisitos

* Python 3.6 ou superior instalado
* Sistema operacional: Windows, Linux ou macOS
* 10 MB de espaço livre em disco

### Passo a Passo para Executar

1. Clone ou baixe o projeto

   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd nome-do-repositorio
   ```

2. Verifique a instalação do Python

   ```bash
   python --version
   ```

   ou

   ```bash
   python3 --version
   ```

3. Execute o programa principal

   ```bash
   python main.py
   ```

   ou

   ```bash
   python3 main.py
   ```

4. Navegação no sistema

   * Use os números do teclado para selecionar opções
   * Pressione ENTER após cada seleção
   * Siga as instruções em cada tela

### Primeiro Uso

1. Ao executar pela primeira vez, o sistema criará automaticamente:

   * Arquivo escola.db (banco de dados)
   * Estrutura completa de tabelas
   * Relacionamentos configurados

2. Fluxo recomendado para início:

   ```
   1. Cadastrar professores
   2. Cadastrar turmas (vinculando professores)
   3. Cadastrar alunos (vinculando às turmas)
   4. Adicionar notas aos alunos
   5. Gerar relatórios conforme necessidade
   ```

## 👥 Equipe de Desenvolvimento

### Líder do Grupo

* Ewerton Guilherme

### Membros do Grupo

* Saulo Eduardo
* Mateus Valerino 
* João Ricardo 
* Davi Magno 

## 🔧 Tecnologias Utilizadas

* Linguagem principal: Python 
* Banco de Dados: SQLite3
* Interface: Site usando Flask, HTML e CSS
* Armazenamento: Arquivo local .db

## 🔌 INSTRUÇÕES PARA ACESSAR INTERFACE

1. Com a pasta do projeto aberta, abra um novo terminal.
2. No terminal, execute o comando:

   ```
   pip install flask
   ```
3. Após a instalação, navegue até a pasta principal do projeto usando o comando:

   ```
   cd nome-da-pasta-do-projeto
   ```
4. Com o terminal já dentro da pasta do projeto, execute o comando:

   ```
   python app.py
   ```
5. O terminal exibirá uma URL contendo números (exemplo: [http://127.0.0.1:5000](http://127.0.0.1:5000)).
   Copie essa URL e cole em qualquer navegador para acessar a interface do sistema.


