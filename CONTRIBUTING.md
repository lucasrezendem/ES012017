# Informações importantes
- Sempre antes de executar qualquer comando certifique-se que está no ambiente virtual criado no Virtualenv.
- Não delete nenhum arquivo das pastas migrations após já ter subido esse arquivo para o github.
- Todas as dependências devem ser instaladas pelo pip e corretamente armazenadas no arquivo [requirements.txt](requirements.txt) como explicado na sessão sobre o PIP.
- As informações armazenadas no banco de dados pode ser acessada pela url [http://localhost:8000/admin](http://localhost:8000/admin).

# Preparando o ambiente
Para preparar o ambiente de desenvolvimento e testes é necessário executar os seguntes comandos:
**Obs:** Os comandos são explicados em mais detalhes nas próximas sessões.
```sh
$ cd ES012017
$ virtualenv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
```

# Resumo dos comandos mais importantes
### Virtualenv
Criar um novo ambiente:
```sh
$ cd ES012017
$ virtualenv .venv
```
**Obs:** O nome do ambiente não precisa ser .venv, porém se for utilizar outro nome e o diretório do Virtualenv estiver na dentro do projeto certifique-se de adicionar esse nome no arquivo [.gitignore](.gitignore) para o git ignorar todos os arquivos do ambiente virtual.

Iniciar o ambiente virtual:
```sh
$ source .venv/bin/activate
```

Sair do ambiente virtual:
```sh
(.venv) $ deactivate
```

### PIP
Instalar todas as dependências:
```sh
(.venv) $ pip install -r requirements.txt
```

Se for necessário adicionar uma nova dependencia, instale normalmente com o *pip install* e então no diretório raiz do projeto execute:
```sh
(.venv) $ pip freeze > requirements.txt
```

### Django
Para gerar os arquivos de definição do banco de dados (*migrations*) a partir dos arquivos *models.py* é necessário executar o comando:
```sh
(.venv) $ python manage.py makemigrations
```

Depois de gerar os arquivos de definição do banco de dados (*migrations*) é necessário criar um novo banco de dados ou aplicar as modificações ao banco existente com o comando:
```sh
(.venv) $ python manage.py migrate
```

Criar um usuário admin:
```sh
(.venv) $ python manage.py createsuperuser
```

Rodar testes:
```sh
(.venv) $ python manage.py test
```
