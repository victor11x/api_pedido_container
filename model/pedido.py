from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime,date
from typing import Union

from model import Base

class Pedidos(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column("pk_pedido", Integer, primary_key=True)
    descricao_pedidos = Column(String(140))
    quantidade = Column(Integer)
    valor_compra = Column(Integer)
    valor_frete = Column(Integer)
    valor_total = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())
    
    
def __init__(self, descricao_pedidos:str, valor_compra:int, valor_total: int, valor_frete: int,quantidade:int,data_insercao:Union[DateTime, None] = None):
        """
        Produtos faltantes no estoque 

        Arguments:
  
        """
        self.descricao_pedidos = descricao_pedidos
        self.quantidade = quantidade
        self.valor_compra = valor_compra
        self.valor_frete = valor_frete
        self.valor_total = valor_total
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
        