# Notificador de Arquivamento de Inquérito Policial

## Descrição
Esta aplicação Python, com interface gráfica, envia notificações por SMS nos casos de arquivamento de inquéritos policiais, gerando um comprovante, para atendimento à Resolução Nº 1.920/2024-PGJ, de 19 de setembro de 2024. O programa utiliza a API do Twilio.

## Pré-requisitos
* **Python:** Instalar a versão Python 3.6 ou superior.
* **Bibliotecas:**
  * `PyQt5`: `pip install PyQt5`
  * `twilio`: `pip install twilio`
  * `dotenv`: `pip install python-dotenv`
  * `reportlab`: `pip install reportlab` (para a geração do PDF)
* **Conta Twilio:** Criar uma conta na Twilio e obter as credenciais (account_sid e auth_token).
* **Arquivo .env:** Criar um arquivo .env na raiz do projeto com as seguintes variáveis:
  * `DIRETORIO`: Diretório onde os PDFs serão salvos.
  * `CELULAR_ORIGEM`: Número de telefone da sua conta Twilio.
  * `PAIS`: Código do país dos números de destino (no caso: '+55').
  * `FUNCIONARIO`: e-mail do funcionário responsável pelo controle.
  * `PROMOTOR`: Cargo.
  * `account_sid` e `auth_token`: Credenciais da sua conta Twilio.

## Como usar
1. **Configuração:** Preencha o arquivo .env com as informações corretas.
2. **Execução:** Execute o script Python principal.
3. **Interface:**
   * Preencha os campos: Número do IP, Nome, Celular e selecione o tipo de notificação (no checkbox).
   * Clique em "Enviar" para enviar o SMS e gerar o PDF.

## Estrutura do Projeto
* **tela_notificador.ui:** Arquivo de interface criado com o Qt Designer.
* **comprovante.py:** Módulo responsável por gerar o PDF com o comprovante de envio.
* **README.md:** Este arquivo.

## Funcionalidades
* **Interface Gráfica:** Facilita a utilização do sistema.
* **Envio de SMS:** Utiliza a Twilio para enviar mensagens para os destinatários.
* **Geração de PDF:** Cria um comprovante em PDF para cada envio.
* **Personalização:** Permite personalizar as mensagens e o diretório de saída.
* **Validação:** Verifica se todos os campos obrigatórios foram preenchidos.

## Observações
* **Segurança:** Proteja as credenciais da sua conta Twilio.
* **Personalização:** Adapte as mensagens e o layout do PDF conforme a necessidade.
* **Erros:** Implemente um sistema de log para registrar erros e facilitar a depuração.

## Contribuições
Contribuições são bem-vindas! Abra um issue ou um pull request.

## Licença
Este projeto está licenciado sob a licença MIT.

## Fonte
https://www.twilio.com/docs/messaging/quickstart/python