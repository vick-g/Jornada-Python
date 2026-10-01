# 🚀 Jornada Python - Intensivão de Automação

Bem-vindo ao repositório dos meus projetos desenvolvidos durante o Intensivão de Python! Aqui estão guardados os códigos, automações e a evolução dos meus estudos na programação.

---

## 📂 Conteúdo das Aulas

### 🤖 Aula 1: Automação de Tarefas com Python
* **Descrição:** Criação de um robô de automação web utilizando `pyautogui`, manipulação de planilhas com `pandas`, tratamento de dados vazios (`nan`) e lógica de repetição com `for`.
* **Funcionalidades:**
  - Abertura automatizada do navegador e maximização inteligente da janela.
  - Preenchimento automático de formulários de login.
  - Leitura de base de dados em CSV (`produtos.csv`) com suporte a caracteres e separadores brasileiros.
  - Cadastro em massa de produtos de forma autônoma.

### 💻 Aula 2: Análise Exploratória e Tratamento de Dados
* **Descrição:** Avanço no projeto de análise de dados para entender os principais motivos de cancelamento dos clientes.
* **Funcionalidades:**
  - **Importação da Base de Dados:** Carregamento do arquivo `cancelamentos.csv` utilizando a biblioteca `pandas`.
  - **Visualização Inicial:** Inspeção dos dados brutos e identificação de colunas irrelevantes para a análise (como o `CustomerID`, removido por não agregar valor preditivo).
  - **Tratamento de Dados:** Utilização do método `tabela.info()` para verificar tipos de dados, contagem de registros e detecção de valores nulos (`NaN`), além da limpeza da base com `dropna()`.
  - **Análise Inicial:** Contagem de clientes ativos e inativos (cancelados) para mensurar o tamanho do problema na base geral.

### 💬 Aula 3: Desenvolvimento de Chatbot com Inteligência Artificial e Streamlit
* **Descrição:** Criação de uma aplicação web interativa de chat utilizando **Streamlit** e a biblioteca oficial da **OpenAI** conectada aos modelos do **Google Gemini**, integrando um sistema de memória de sessão e uma personalidade customizada (*Role System*).
* **Funcionalidades:**
  - **Interface Web Reativa:** Construção de uma interface de chat moderna em tempo real com o Streamlit (`st.chat_input`, `st.chat_message`).
  - **Personalidade Única (*Vick-bot*):** Configuração de um prompt de sistema (`role: system`) para dar ao chatbot uma identidade divertida, descontraída e focada em ajudar com programação e o dia a dia.
  - **Gestão de Histórico e Memória:** Utilização de `st.session_state` para manter o contexto da conversa ativo entre os ciclos de execução da página sem apagar o chat a cada mensagem.
  - **Experiência do Usuário (UX):** Implementação de indicador de carregamento dinâmico (`st.spinner`) enquanto a IA processa e gera a resposta.
  - **Integração Multi-plataforma:** Uso da SDK da OpenAI redirecionada para a API do Google Gemini através de um `base_url` personalizado.
---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 3.13
* **Bibliotecas:** `pyautogui`, `pandas`, `time`, `plotly`
* **Controle de Versão:** Git e GitHub (utilizando Conventional Commits)
* **Ambiente:** Visual Studio Code (VS Code) no Windows

---
*Desenvolvido por Victor Gabriel Mendes de Freitas.*