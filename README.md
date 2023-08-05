# Testar o sistema:
  * com o docker instalado, abra a pasta do projeto no terminal e execute: `docker compose up -d`
  * http://127.0.0.1:8000/ ( pode demorar alguns segundos até estar no ar )
# Editar código no vscode com a extensão Dev Containers:
  * instalar extensão:
    ![vscodeExtDevContainer](https://github.com/cleomarsrv/Django_Concessionaria/assets/126989966/43d35285-7ef5-4910-acfc-2bf8722f7eb7)

  * abra a pasta do projeto no vscode
  * atalho Ctrl + Shift + P
    - digite e selecione a opcao: `Dev Container: reopen in container`
  * execute no terminal integrado: `source .venv/bin/activate`
# Usuários cadastrados:
| usuário          | senha      |
|-----------------:|------------|
| admin(superuser) | 8000/admin |
| gerente1         | 8000/admin |
| supervisor1      | 8000/admin |
| vendedor1        | 8000/admin |
