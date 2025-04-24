from datetime import datetime

class Dispositivo:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo
        self._ip = None
        self.data_conexao = None

class Roteador:
    def __init__(self, nome: str, ip_base: str, ip: int, senha: str):
        self.nome = nome
        self.ip_base = ip_base
        self.ip = ip
        self.senha = senha
        self.contador = ip + 1
        self.conectados: list[Dispositivo] = []


    def conectar(self, dispositivo: Dispositivo, senha_digitada: str):
        if senha_digitada != self.senha:
            print(f"Conexão recusada para {dispositivo.nome}. Senha incorreta.")
            return

        ip_dispositivo = f"{self.ip_base}.{self.contador}"
        self.contador += 1    
        dispositivo.ip = ip_dispositivo
        dispositivo.data_conexao = datetime.now()
        self.conectados.append(dispositivo)

        print(f"Conectado: {dispositivo.nome} IP | {dispositivo.ip} às {dispositivo.data_conexao:%H:%M:%S}")

    def listar_dispositivos(self):
        print(f"\nRoteador: {self.nome} | {self.ip_base}.{self.ip}")
        if not self.conectados:
            print("Nenhum dispositivo conectado.")
            return

        for d in self.conectados:
            print(f"{d.nome} IP | {d.ip} | Conectado em: {d.data_conexao:%d/%m/%Y %H:%M:%S}")

if __name__ == "__main__":
    r = Roteador("WiFi-Casa", "192.168.0", 1, "123")

    notebook = Dispositivo("Dell Inspiron", "Notebook")
    celular = Dispositivo("iPhone 13", "Smartphone")

    r.conectar(notebook, "123")
    r.conectar(celular, "321")

    r.listar_dispositivos()
