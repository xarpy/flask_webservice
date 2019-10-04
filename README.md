# Weather Webservice
> projeto de um webservice em flask

[![Python Version][python-image]][python-url]
[![Flask Version][flask-image]][flask-url]

Pequeno webservice, criado em Python e framework Flask, utilizando de recursos mais novos e variados para construir um projeto estável de um webservice.

## Dependecies

Segue a lista de pacotes utilizados no projeto.

Package           | Version  |
------------------| ---------|
Flask             | 1.1.1    |
Flask-Cors        | 3.0.8    |
Flask-Migrate     | 2.5.2    |
flask-restplus    | 0.13.0   |
Flask-SQLAlchemy  | 2.4.1    |
gunicorn          | 19.9.0   |
marshmallow       | 3.2.0    |
python-dotenv     | 0.10.3   |
requests          | 2.22.0   |
SQLAlchemy        | 1.3.8    |


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
[flask-url]: https://img.shields.io/pypi/pyversions/flask