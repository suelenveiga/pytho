class Temporada:
    def __init__(self, descricao, codigo, numero, FK_serie_cod):
        self._descricao = descricao
        self._codigo = codigo
        self._numero = numero
        self._FK_serie_cod = FK_serie_cod

    def _get_descricao(self):
        return self._descricao
    def _set_descricao(self, descricao):
        self._descricao = descricao
    def _get_codigo (self):
        return self._codigo
    def _set_codigo (self, codigo):
        self._codigo = codigo
    def _get_numero (self):
        return self._numero
    def _set_numero (self, numero):
        self._numero = numero
    def _get_FK_serie_cod (self):
        return self._FK_serie_cod
    def _set_FK_serie_cod (self, FK_serie_cod):
        self._FK_serie_cod = FK_serie_cod
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.descricao,self.codigo,self.numero,self.FK_serie_cod)

    descricao = property( _get_descricao, _set_descricao)
    codigo = property( _get_codigo, _set_codigo)
    numero = property( _get_numero, _set_numero)
    FK_serie_cod = property( _get_FK_serie_cod, _set_FK_serie_cod)