class Episodio:
    def __init__(self, titulo, codigo, numero, FK_serie_cod, FK_temporada_cod):
        self._titulo = titulo
        self._codigo = codigo
        self._numero = numero
        self._FK_serie_cod = FK_serie_cod
        self._FK_temporada_cod = FK_temporada_cod


    def _get_titulo(self):
        return self._titulo
    def _set_titulo(self, titulo):
        self._titulo = titulo
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
    def _get_FK_temporada_cod (self):
        return self._FK_temporada_cod
    def _set_FK_temporada_cod (self, FK_temporada_cod):
        self._FK_temporada_cod = FK_temporada_cod
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.titulo,self.codigo,self.numero,self.FK_temporada_cod,self.FK_serie_cod)

    titulo = property( _get_titulo, _set_titulo)
    codigo = property( _get_codigo, _set_codigo)
    numero = property( _get_numero, _set_numero)
    FK_serie_cod = property( _get_FK_serie_cod, _set_FK_serie_cod)
    FK_temporada_cod = property( _get_FK_temporada_cod, _set_FK_temporada_cod)