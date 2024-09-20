
# Refatoração
MENOR_IDADE = 18
CHAR_OBRIGATORIO = "@"
MINIMO_CHAR_NOME = 3

class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):
        
        if cliente.idade < MENOR_IDADE:
            return "Cliente menor de idade não cadastrado!"
        
        if not CHAR_OBRIGATORIO in cliente.email:
            return "Email inválido, não cadastrado!"
        
        if len(cliente.nome) < MINIMO_CHAR_NOME:
            return "Nome inválido, este nome possui menos que 3 caracteres!" 

        self.clientes_cadastrados.append(cliente)

        if len(self.clientes_cadastrados) > 0:
            return "Cadastrado com sucesso!!!"