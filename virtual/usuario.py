class Usuario:
    def __init__(self, nome, login, email, senha, codserie, altura, idade):
        self._nome = nome
        self._login = login
        self._email = email
        self._senha = senha
        self._codserie = codserie
        self._altura = altura
        self._idade = idade

    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_login(self):
        return self._login
    def _set_login(self, login):
        self._login = login
    def _get_email(self):
        return self._email
    def _set_email(self, email):
        self._email = email
    def _get_senha(self):
        return self._senha
    def _set_senha(self, senha):
        self._senha = senha
    def _get_codserie (self):
        return self._codserie
    def _set_codserie (self, codserie):
        self._codserie = codserie
    def _get_altura (self):
        return self._altura
    def _set_altura (self, altura):
        self._altura = altura
    def _get_idade (self):
        return self._idade
    def _set_idade (self, idade):
        self._idade = idade

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.nome,self.login,self.email,self.senha,self.codserie,self.altura,self.idade)

    nome = property( _get_nome, _set_nome)
    login = property( _get_login, _set_login)
    email = property( _get_email, _set_email)
    senha = property( _get_senha, _set_senha)
    codserie = property( _get_codserie, _set_codserie)
    altura = property( _get_altura, _set_altura)
    idade = property( _get_idade, _set_idade)