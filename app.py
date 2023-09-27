from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from datetime import datetime
from schema.error import *
from schema.pedido import *
from model import Session, pedido
from flask_cors import CORS

info = Info(title="API de Pedidos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
pedido_tag = Tag(name="Pedido", description="Adição, visualização e remoção de produtos teve pedido")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')
  
@app.post('/pedidos', tags=[pedido_tag],
          responses={"200": PedidoViewSchema, "409": ErrorSchema, "400": ErrorSchema})


def add_pedido(form: PedidoSchema):
    """Adiciona um novo inventario de produto realizado pelo auditor fiscal à base de dados

    Retorna detalhes do Inventario.
    """
    pedido = Pedidos(

            descricao_pedidos = form.descricao_pedidos,
            quantidade = form.quantidade,
            valor_compra = form.valor_compra,
            valor_frete = form.valor_frete,
            valor_total = form.valor_total,
        )
    try:

        session = Session()

        session.add(pedido)

        session.commit()
        return apresenta_pedido(pedido), 200

    except IntegrityError as e:

        error_msg = "Produto foi auditodo de mesmo nome já foi salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:

        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400


# Metodo GET
@app.get('/pedidos', tags=[pedido_tag],
         responses={"200": ListagemPedidoSchema, "404": ErrorSchema})


def get_pedido():
    """Faz a busca por uma descrição de produto a partir do id produto

    Retorna uma representação de produtos auditados.
    """

    session = Session()

    pedidos = session.query(Pedidos).all()

    if not pedidos:

          return {"pedidos": []}, 200
    else:

        return apresenta_pedidos(pedidos), 200
