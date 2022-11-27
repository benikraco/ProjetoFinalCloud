# Projeto Final Cloud 22.2

## Objetivo do projeto

Desenvolver uma aplicação capaz de provisionar uma infraestrutura por meio de uma interface amigável (livre escolha) para gerenciar e administrá-la (construir, alterar e deletar recursos).

## Instalação

Antes de rodar os programas contidos neste repositório, é necessária a instalação de alguns serviços.

### 1. Bibliotecas necessárias

Para instalar as bibliotecas necessárias basta rodar o código abaixo:

```shell
pip3 install requirements.txt
```

### 2. Terraform

Dentro do Home Brew no MacOS:

```shell
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

### 3. AWS CLI

Na utilização do Terraform com AWS, utilizamos o prompt de comando. Assim, é necessário que o usuário do programa possua IAM credentials para autenticar o Terraform AWS provider. Lembrando que essas credenciais devem ser guardadas em variáveis ambientes para não serem vazadas e hackers terem acessos às suas máquinas. Para configurar suas credenciais basta abrir o terminal e digitar:

```shell
aws configure 
```

Depois de rodar este comando, o usuário deve preencher um output da seguinte forma:
- **{ACCESS_KEY}** e **{SECRET_ACCESS_KEY}** = credenciais AWS
- **{REGION}** = us-east-1
- **{OUTPUT FORMAT}** = json

## Utilização

Para executar o programa final basta:

```shell
python3 main.py
```