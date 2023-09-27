from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from model.pedido import Pedidos


class PedidoSchema(BaseModel):
    """ Define como um novo registro de auditoria de inventarios produtos faltantes no estoque
    """
    
    descricao_pedidos : str = "Camisa Polo G"
    quantidade : str = "5"
    valor_compra : str =  "120"
    valor_frete : str =  "12"
    valor_total : int = "132"
    

class PedidoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com nome do produto.
    """
    descricao_pedidos: str = "Digite nome produto"


class ListagemPedidoSchema(BaseModel):
    """ Define como uma listagem de produtos que teve auditoria.
    """
    pedido:List[PedidoSchema]


def apresenta_pedidos(pedidos: List[Pedidos]):
    """ Retorna uma representação de produtos auditados seguindo o schema definido em
        InventarioViewSchema.
    """
    result = []
    for pedido in pedidos:
        result.append({
            "descricao_pedidos":pedido.descricao_pedidos,
            "quantidade":pedido.quantidade,
            "valor_compra":pedido.valor_compra,
            "valor_frete":pedido.valor_frete,
            "valor_total": pedido.valor_total,
            "data_pedido":pedido.data_insercao,
        })

    return {"pedidos": result}


class PedidoViewSchema(BaseModel):
    """ Define como um auditoria será retornado: descrição de produtos auditados).
    """
        
    descricao_pedidos : str = "Camisa Polo G"
    quantidade : str = "Camisa"
    valor_compra : str =  "120"
    valor_frete : str =  "12"
    valor_total : int = "132"
    data_insercao : str = "12/03/2023"


class PedidoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    descricao_pedidos: str

def apresenta_pedido(pedidos: Pedidos):
    """ Retorna uma representação da auditoria seguindo o schema definido em
        pedidoViewSchema.
    """
    return {
        "descricao_pedidos":pedidos.descricao_pedidos,
        "quantidade":pedidos.quantidade,
        "valor_compra":pedidos.valor_compra,
        "valor_frete":pedidos.valor_frete,
        "valor_total": pedidos.valor_total,
        
    }