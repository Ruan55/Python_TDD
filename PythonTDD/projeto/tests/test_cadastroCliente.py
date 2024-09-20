from projeto.models.cliente import Cliente
from projeto.models.cadastro_cliente import CadastroCliente

# 1 - Teste RED: cliente = Cliente()
def test_que_cliente_seja_cadastrado_com_sucesso():
    # 2 - Teste GREEN 
    cliente = Cliente("Ruan", 22, "Ru22@gmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com sucesso!!!" == resposta

# 1 - Teste RED: cliente = Cliente("Ruan", 12, "Ru22@gmail.com")
def test_que_o_cliente_nao_pode_ser_menor_de_idade():
    cliente = Cliente("Ruan", 12, "Ru22@gmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente menor de idade não cadastrado!" == resposta

# 1 - Teste RED: cliente = Cliente("Ruan", 19, "Ru22")
def test_de_validacao_do_email_do_cliente():
    cliente = Cliente("Ruan", 19, "Ru22")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Email inválido, não cadastrado!" == resposta

# 1 - Teste RED: cliente = Cliente("Ru", 39, "Ru22@gmail.com")
def test_que_nome_do_cliente_nao_pode_ter_menos_que_3_caracteres():
    cliente = Cliente("Ru", 39, "Ru22@gmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Nome inválido, este nome possui menos que 3 caracteres!" == resposta