# Weather Webservice
> projeto de um webservice em flask

[![Python Version][python-image]][python-url]
[![Flask Version][flask-image]][flask-url]

Pequeno webservice, criado em Python e framework Flask, utilizando de recursos mais novos e variados para construir um projeto estável de um webservice.

## Pacotes

Segue a lista de pacotes utilizados no projeto.

Package                             | Version  |
------------------------------------| ---------|
[Flask][flask-url]                  | 1.1.1    |
[Flask-Cors][flask_cors-url]        | 3.0.8    |
[Flask-Migrate][flask_migrate-url]  | 2.5.2    |
[flask-restplus][flask_restplus-url]| 0.13.0   |
[Flask-SQLAlchemy][flask-url]       | 2.4.1    |
[gunicorn][gunicorn-url]            | 19.9.0   |
[marshmallow][marshmallow-url]      | 3.2.0    |
[python-dotenv][python_dotenv-url]  | 0.10.3   |
[requests][requests-url]            | 2.22.0   |


## Exemplo de uso:

O produto criado foi feito para fins de testes pessoais, utilizando alguns padrões especificos. O intuito nada mais é que fazer uso de novas tecnologias e pacotes, para alcançar o objetivo do projeto.


## Instalação:

Para instalação em ambiente de desenvolvimento, segue o contexto abaixo, explicando. Caso prefira e tenha conhecimentos avançados, utilizamos como servidor e compilador, nginx e gunicorn, logo disponibilizamos arquivos de configurações caso sabia como implanta-los e queria testar seu uso.

Devemos em breve, finalizar o projeto com uma versão dockerizada, para fins de teste pratico.

### Etapas para uso em desenvolvimento:
1. Com a sua ambiente python, instale a lista de pacotes.
```sh
pip install -r requeriments/dev.txt
```
2. Não esqueça de criar suas variaveis de ambiente, usem o editor de preferência e insira dentro da pasta do projeto.

3. Execute o projeto, na pasta principal
```sh
flask run
```

## Meta

Renan Penna – [@pennarenanti](https://twitter.com/dbader_org)

Distribuido pela licença GNU GENERAL PUBLIC . Veja ``LICENSE`` para maiores detalhes.

[https://github.com/xarpy/flask_webservice](https://github.com/dbader/)

## Contribua

1. Fork it (<https://github.com/xarpy/flask_webservice/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/python-v3.7-blue
[flask-image]: https://img.shields.io/badge/flask-v1.1.1-blue
[python-url]: https://www.python.org/downloads/release/python-374/
[flask-url]: https://flask.palletsprojects.com/en/1.1.x/
[flask_cors-url]: https://flask-cors.readthedocs.io/en/latest/
[flask_migrate-url]: https://flask-migrate.readthedocs.io/en/latest/
[flask_restplus-url]: https://flask-restplus.readthedocs.io/en/stable/index.html
[python_dotenv-url]: https://github.com/theskumar/python-dotenv
[requests-url]: https://requests.kennethreitz.org/en/master/
[flask_sqllchemy-url]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
[gunicorn-url]: http://docs.gunicorn.org/en/latest/index.html
[marshmallow-url]: https://marshmallow.readthedocs.io/en/stable/index.html
