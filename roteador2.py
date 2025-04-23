from datetime import datetime
from rich import print

class Dispositivo:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo
        self._ip = None  
        self.data_conexao = None

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor: str):
        self._ip = valor

    def __str__(self):
        ip_info = self.ip if self.ip else "Sem IP"
        return f"{self.tipo} {self.nome} | IP: {ip_info}"


class Roteador:
    def __init__(self, nome: str, ip_base: str, senha: str):
        self.nome = nome
        self._ip_base = ip_base  
        self._senha = senha
        self._contador = 1
        self._conectados: list[Dispositivo] = []

    @property
    def ip_base(self):
        return self._ip_base

    def conectar(self, dispositivo: Dispositivo, senha_digitada: str):
        if senha_digitada != self._senha:
            print(f"Conexão recusada para {dispositivo.nome}. Senha incorreta.")
            return

        ip_dispositivo = f"{self._ip_base}.{self._contador}"
        self._contador += 1

        dispositivo.ip = ip_dispositivo
        dispositivo.data_conexao = datetime.now()
        self._conectados.append(dispositivo)

        print(f"Conectado: {dispositivo} às {dispositivo.data_conexao:%H:%M:%S}")

    def listar_dispositivos(self):
        print(f"\nDispositivos conectados ao roteador {self.nome}:")
        if not self._conectados:
            print("Nenhum dispositivo conectado.")
            return

        for d in self._conectados:
            print(f"{d} | Conectado em: {d.data_conexao:%d/%m/%Y %H:%M:%S}")


if __name__ == "__main__":
    r = Roteador("WiFi-Casa", "192.168.0", "senha123")

    notebook = Dispositivo("Dell Inspiron", "Notebook")
    celular = Dispositivo("iPhone 13", "Smartphone")

    notebook_conectado = r.conectar(notebook, "senha123")
    celular_conectado = r.conectar(celular, "errado123")

    r.listar_dispositivos()
