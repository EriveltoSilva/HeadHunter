EJZ Tecnologia Job Recruitment

# Bibliotecas Fundamentais para a aplicação Django
Django==5.0.3
django-notifications-hq==1.8.3
python-dotenv==1.0.1
pillow==10.2.0
daphne==4.1.0
channels==4.0.0
icalendar==5.0.11
django-role-permissions
django-debug-toolbar

# Bibliotecas Fundamentais para o Langchain
chromadb==0.4.22
firebase-admin==6.4.0
langchain==0.1.8
langchain-community==0.0.21
langchain-core==0.1.24
langchain-openai==0.0.6
langchain-experimental==0.0.51
openai==1.12.0
pypdf==4.0.2
PyPDF2==3.0.1
python-dotenv==1.0.1
tabulate==0.9.0
tiktoken==0.6.0


Alguns requisitos funcionais para o software de gestão de candidaturas a vagas de emprego:

1. **Cadastro de Empregadores**:
   - Os empregadores devem poder se cadastrar na plataforma.
   - Deve-se coletar informações como nome da empresa, contato, endereço, entre outros.
   - Os empregadores devem ser verificados antes de poderem postar vagas.

2. **Criação de Vagas**:
   - Os empregadores devem poder criar novas vagas de emprego.
   - Deve ser possível adicionar detalhes da vaga, como título, descrição, requisitos, benefícios, localização, salário, data de expiração, entre outros.
   - Os empregadores podem revisar e editar as vagas que criaram.

3. **Publicação de Vagas**:
   - As vagas devem ser publicadas após a revisão pelo administrador ou automaticamente após a criação, dependendo da configuração.
   - As vagas devem ser visíveis para os candidatos registrados na plataforma.

4. **Cadastro de Candidatos**:
   - Os candidatos devem poder se cadastrar na plataforma.
   - Deve-se coletar informações como nome, contato, experiência profissional, habilidades, formação acadêmica, entre outros.

5. **Pesquisa e Candidatura a Vagas**:
   - Os candidatos devem poder pesquisar e filtrar vagas com base em critérios como localização, tipo de trabalho, setor, salário, etc.
   - Os candidatos devem poder visualizar os detalhes das vagas e enviar seus currículos para as vagas desejadas.
   - Os candidatos devem receber confirmação por e-mail de que sua candidatura foi recebida.

6. **Gerenciamento de Candidaturas**:
   - Os empregadores devem poder visualizar as candidaturas recebidas para suas vagas.
   - Deve ser possível classificar, filtrar e gerenciar as candidaturas recebidas.
   - Os empregadores devem poder entrar em contato com os candidatos através da plataforma.

7. **Comunicação**:
   
   

8. **Notificações**:
   - Os usuários devem receber notificações por e-mail ou dentro da plataforma sobre novas vagas correspondentes ao seu perfil, atualizações de status de candidatura, mensagens recebidas, etc.

9. **Avaliações e Feedback**:
   - Os empregadores e os candidatos devem poder fornecer feedback sobre o processo de recrutamento e sobre os candidatos/empregadores.

10. **Gerenciamento de Contas**:
    - Os usuários devem poder atualizar suas informações de perfil e configurações de conta.
    - Os empregadores devem poder gerenciar suas vagas ativas e histórico de candidaturas.
    - Os candidatos devem poder acessar seu histórico de candidaturas e atualizar seus currículos.

Estes são alguns dos principais requisitos funcionais para o software de gestão de candidaturas a vagas de emprego.