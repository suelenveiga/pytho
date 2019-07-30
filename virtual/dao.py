from Usuario import Usuario
from psycopg2 import connect
from server import DAO

class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__()
    def excluir(self, Usuario):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM Usuario WHERE codigo = %s",[Usuario.codigo])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no inserir -- exception seguindo para ser tratada")
            raise e
    def buscar(self, cod):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM Usuario WHERE codigo = %s', [cod])
                row = cur.fetchone()
                Usuario = Usuario(codigo=row[0],nome=row[1],login=row[2],altura=row[3],senha=row[4],idade=row[5],email=row[6],enviar=row[7])
                cur.close()
                return Usuario
        except BaseException as e:
            print ("Problema no buscar -- exception seguindo para ser tratada")
            raise e     
    def listar(self):
        vet = []
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM Usuario')
                for row in cur.fetchall():
                    vet.append(Usuario(codigo=row[0],nome=row[1],login=row[2],altura=row[3],senha=row[4],idade=row[5],email=row[6]))
                cur.close()
        except BaseException as e:
            print ("Problema no listar -- exception seguindo para ser tratada")
            raise e    
        return vet
    def inserir(self, Usuario):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("insert into Usuario(nome,login,altura,senha,idade,senha,login) values (%s, %s, %s, %s, %s, %s, %s)",[Usuario.nome,Usuario.login,Usuario.altura,Usuario.senha,Usuario.idade,Usuario.email])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no inserir -- exception seguindo para ser tratada")
            raise e
    def alterar(self, Usuario):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("UPDATE Usuario SET nome=%s, login=%s, altura=%s, senha=%s, idade=%s, senha=%s, login=%s WHERE codigo = %s", [Usuario.nome,Usuario.login,Usuario.altura,Usuario.senha,Usuario.idade,Usuario.email,Usuario.enviar,Usuario.codigo])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no alterar -- exception seguindo para ser tratada")
            raise e
    def salvar(self, Usuario):
        if Usuario.persistido():
            self.alterar(Usuario)
        else:
            self.inserir(Usuario)
