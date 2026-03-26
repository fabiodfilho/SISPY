# SISPY

Sistema de Importação de Matrículas para SIS (Student Information System) - Aplicação Flask para gerar arquivos CSV de matrículas com mapeamento automático de códigos de cursos.

## 📋 Descrição

O SISPY é uma aplicação web desenvolvida em Python com Flask que facilita a importação de matrículas de alunos em sistemas SIS. O sistema lê uma planilha Excel contendo códigos de ofertas de cursos e seus respectivos SIS_IDs, permitindo que o usuário insira códigos de cursos e matrículas de alunos para gerar um arquivo CSV formatado para importação.

### Funcionalidades Principais
- **Mapeamento Automático**: Converte códigos de 6 dígitos de cursos para SIS_IDs válidos
- **Interface Web Simples**: Formulário intuitivo para inserção de dados
- **Validação Robusta**: Verifica códigos inexistentes e entradas inválidas
- **Geração de CSV**: Produz arquivo compatível com importação SIS
- **Tratamento de Erros**: Interrompe geração se houver problemas e informa detalhes

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone ou baixe o projeto**
   ```bash
   cd "seu/diretorio"
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Certifique-se de que o arquivo de banco de dados está presente**
   - O arquivo `Model/BD-OFERTAS-261.1.xlsx` deve estar localizado na pasta `Model/`
   - Este arquivo contém as colunas `Nome_Curso` e `SIS_ID`

4. **Execute a aplicação**
   ```bash
   python main.py
   ```

5. **Acesse no navegador**
   - Abra `http://127.0.0.1:5000`

## 📖 Uso

1. **Página Inicial**: Acesse a URL e você verá um formulário com campos para códigos de cursos e matrículas.

2. **Inserir Dados**:
   - **Códigos de Cursos**: Digite códigos de 6 dígitos (ex: `221016`), um por linha
   - **Matrículas**: Digite números de matrícula dos alunos, um por linha

3. **Gerar CSV**: Clique em "Gerar CSV" para baixar o arquivo `matriculas_sis.csv`

4. **Tratamento de Erros**: Se houver códigos inválidos ou não encontrados, a aplicação exibirá uma página de erro com detalhes.

## 🏗️ Estrutura do Projeto

```
SISPY/
├── main.py                    # Ponto de entrada da aplicação Flask
├── requirements.txt           # Dependências Python
├── README.md                  # Este arquivo
├── Controller/
│   ├── __init__.py
│   ├── csv_controller.py      # Lógica de processamento e geração do CSV
│   └── views.py               # (Reservado para futuras rotas)
├── Model/
│   ├── excel_engine.py        # Carregamento e mapeamento do banco Excel
│   └── BD-OFERTAS-261.1.xlsx  # Banco de dados com códigos e SIS_IDs
└── View/
    ├── static/
    │   ├── style.css          # Estilos CSS da interface
    │   └── images/            # Imagens (se houver)
    └── templates/
        └── index.html         # Template HTML do formulário
```

## 🔧 Como Funciona

### 1. Carregamento do Banco de Dados (`Model/excel_engine.py`)
- Carrega uma vez o arquivo Excel `BD-OFERTAS-261.1.xlsx`
- Mapeia códigos de 6 dígitos (extraídos da coluna `Nome_Curso`) para `SIS_ID`
- Exemplo: `221016` → `11661021221016102000126221016`

### 2. Processamento da Solicitação (`Controller/csv_controller.py`)
- Recebe listas de códigos de cursos e matrículas
- Para cada combinação curso-aluno:
  - Normaliza o código (extrai apenas dígitos, pega primeiros 6)
  - Busca o SIS_ID correspondente no banco
  - Valida entradas e gera erros se necessário
  - Escreve linha no CSV: `[SIS_ID, matricula, "student", "active"]`

### 3. Interface Web (`main.py`)
- Define rotas Flask (`/` para formulário, `/gerar-csv` para processamento)
- Renderiza template HTML
- Retorna CSV para download ou página de erro

### 4. Validações Implementadas
- Códigos devem ter pelo menos 6 dígitos numéricos
- Códigos devem existir no banco de dados
- Blocos de cursos e matrículas não podem estar vazios
- Se qualquer erro for encontrado, a geração é interrompida

## 📦 Dependências

- **Flask**: Framework web
- **Pandas**: Manipulação de dados Excel
- **OpenPyXL**: Leitura de arquivos Excel (.xlsx)

Instaladas via `pip install -r requirements.txt`

## 🐛 Solução de Problemas

### Erro: "Código de curso não encontrado no banco"
- Verifique se o código digitado existe na planilha Excel
- Certifique-se de que a coluna `Nome_Curso` começa com o código de 6 dígitos

### Erro: "colunas esperadas não encontradas"
- Verifique se o arquivo Excel tem as colunas `Nome_Curso` e `SIS_ID`
- O arquivo deve estar em `Model/BD-OFERTAS-261.1.xlsx`

### Aplicação não inicia
- Confirme que todas as dependências estão instaladas
- Verifique se a porta 5000 está livre

## 🤝 Contribuição

Para contribuir:
1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request


