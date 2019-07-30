class Serie:
    def __init__(self, titulo, codigo):
        self._titulo = titulo
        self._codigo = codigo
        self._codigoDepto = codigoDepto

    def _get_titulo(self):
        return self._titulo
    def _set_titulo(self, titulo):
        self._titulo = titulo
    def _get_codigo (self):
        return self._codigo
    def _set_codigo (self, codigo):
        self._codigo = codigo
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.titulo,self.codigo)

    titulo = property( _get_nome, _set_nome)
    codigo = property( _get_codigo, _set_codigo)