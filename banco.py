import oracledb
import json


def conectar():
    conn = oracledb.connect(user="RM559183", password="fiap24", dsn="oracle.fiap.com.br/orcl")
    return conn


exportar = None

def perguntar_exportacao():
    global exportar
    if exportar is None:
        exportar = input("Antes de prosseguir, deseja exportar os dados para um arquivo JSON? (s/n): ").strip().lower()



# ---------------------------------------------------------
# CLIENTES
# ---------------------------------------------------------



def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    sql = """SELECT * FROM cliente ORDER BY id_cliente"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    
    if rows:
        perguntar_exportacao()
        if exportar == 's':
            with open('dados.json', 'a') as f:
                for row in rows:
                    json.dump({'id_cliente': row[0], 'nome': row[1], 'email': row[2], 'genero': row[3]}, f)
                    f.write('\n')
    return rows


def buscar_cliente_by_id(id: int) -> dict:
    conn = conectar()
    cursor = conn.cursor()
    sql = "select * from cliente where id_cliente = :1"
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if row:
        dados = {'id_cliente': row[0], 'nome': row[1], 'email': row[2], 'genero': row[3]}
        
        perguntar_exportacao()
        if exportar == 's':
            with open('dados.json', 'a') as f:
                json.dump(dados, f)
                f.write('\n')
                
        return dados
    return {}


def cadastrar_cliente(cliente: dict):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO cliente (id_cliente, nome, email, genero)
             VALUES (:1, :2, :3, :4)"""
    cursor.execute(sql, (cliente['id_cliente'], cliente['nome'], cliente['email'], cliente['genero']))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's':
        with open('dados.json', 'a') as f:
            json.dump(cliente, f)
            f.write('\n')


def modificar_cliente(cliente: dict):
    conn = conectar()
    cursor = conn.cursor()
    sql = """UPDATE cliente
             SET nome = :1, email = :2, genero = :3 WHERE id_cliente = :4"""
    cursor.execute(sql, (cliente['nome'], cliente['email'], cliente['genero'], cliente['id_cliente']))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's':
        with open('dados.json', 'a') as f:
            json.dump(cliente, f)
            f.write('\n')


def excluir_cliente(id: int):
    cliente_info = buscar_cliente_by_id(id)
    
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM cliente WHERE id_cliente = :1"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's' and cliente_info:
        with open('dados.json', 'a') as f:
            json.dump({'id_cliente': cliente_info['id_cliente'], 'nome': cliente_info['nome']}, f)
            f.write('\n')



# ---------------------------------------------------------
# EMPRESAS
# ---------------------------------------------------------



def listar_empresas():
    conn = conectar()
    cursor = conn.cursor()
    sql = """SELECT * FROM empresa ORDER BY id_empresa"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    
    if rows:
        perguntar_exportacao()
        if exportar == 's':
            with open('dados.json', 'a') as f:
                for row in rows:
                    json.dump({'id_empresa': row[0], 'nome': row[1], 'cnpj': row[2], 'vantagens': row[3]}, f)
                    f.write('\n')
    return rows


def buscar_empresa_by_id(id: int) -> dict:
    conn = conectar()
    cursor = conn.cursor()
    sql = "select * from empresa where id_empresa = :1"
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if row:
        dados = {'id_empresa': row[0], 'nome': row[1], 'cnpj': row[2], 'vantagens': row[3]}
        
        perguntar_exportacao()
        if exportar == 's':
            with open('dados.json', 'a') as f:
                json.dump(dados, f)
                f.write('\n')
                
        return dados
    return {}


def cadastrar_empresa(empresa: dict):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO empresa (id_empresa, nome, cnpj, vantagens)
             VALUES (:1, :2, :3, :4)"""
    cursor.execute(sql, (empresa['id_empresa'], empresa['nome'], empresa['cnpj'], empresa['vantagens']))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's':
        with open('dados.json', 'a') as f:
            json.dump(empresa, f)
            f.write('\n')


def modificar_empresa(empresa: dict):
    conn = conectar()
    cursor = conn.cursor()
    sql = """UPDATE empresa
             SET nome = :1, cnpj = :2, vantagens = :3 WHERE id_empresa = :4"""
    cursor.execute(sql, (empresa['nome'], empresa['cnpj'], empresa['vantagens'], empresa['id_empresa']))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's':
        with open('dados.json', 'a') as f:
            json.dump(empresa, f)
            f.write('\n')


def excluir_empresa(id: int):
    empresa_info = buscar_empresa_by_id(id)
    
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM empresa WHERE id_empresa = :1"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's' and empresa_info:
        with open('dados.json', 'a') as f:
            json.dump({'id_empresa': empresa_info['id_empresa'], 'nome': empresa_info['nome']}, f)
            f.write('\n')



# ---------------------------------------------------------
# AVALIAÇÕES
# ---------------------------------------------------------



def listar_avaliacoes():
    conn = conectar()
    cursor = conn.cursor()
    sql = """SELECT * FROM avaliacao ORDER BY id_avaliacao"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    
    if rows:
        perguntar_exportacao()
        if exportar == 's':
            with open('dados.json', 'a') as f:
                for row in rows:
                    json.dump({'id_avaliacao': row[0], 'id_cliente': row[1], 'id_empresa': row[2], 'nota': row[3]}, f)
                    f.write('\n')
    return rows


def buscar_avaliacao_by_id(id_avaliacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_avaliacao, id_cliente, id_empresa, nota, comentario FROM avaliacao WHERE id_avaliacao = :1", (id_avaliacao,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if resultado:
        return {
            'id_avaliacao': resultado[0],
            'id_cliente': resultado[1],
            'id_empresa': resultado[2],
            'nota': resultado[3],
            'comentario': resultado[4],  
        }
    return None


def cadastrar_avaliacao(avaliacao: dict):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO avaliacao (id_avaliacao, id_cliente, id_empresa, nota, comentario)
             VALUES (:1, :2, :3, :4, :5)"""
    cursor.execute(sql, (avaliacao['id_avaliacao'], avaliacao['id_cliente'], 
                         avaliacao['id_empresa'], avaliacao['nota'], avaliacao['comentario']))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's':
        with open('dados.json', 'a') as f:
            json.dump(avaliacao, f)
            f.write('\n')


def modificar_avaliacao(avaliacao: dict):
    conn = conectar()
    cursor = conn.cursor()

    sql = """UPDATE avaliacao
             SET nota = :1, comentario = :2
             WHERE id_avaliacao = :3"""
    cursor.execute(sql, (avaliacao['nota'], avaliacao['comentario'], avaliacao['id_avaliacao']))

    conn.commit()
    cursor.close()
    conn.close()

    perguntar_exportacao()
    if exportar == 's':
        with open('dados.json', 'a') as f:
            json.dump(avaliacao, f)
            f.write('\n')


def excluir_avaliacao(id: int):
    avaliacao_info = buscar_avaliacao_by_id(id)
    
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM avaliacao WHERE id_avaliacao = :1"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    perguntar_exportacao()
    if exportar == 's' and avaliacao_info:
        with open('dados.json', 'a') as f:
            json.dump({'id_avaliacao': avaliacao_info['id_avaliacao'], 'nota': avaliacao_info['nota']}, f)
            f.write('\n')
