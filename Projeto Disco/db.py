import psycopg2

def conectar_db():
   try: 
        conexao = psycopg2.connect("dbname='nome do banco' user='postgres' password='senha do banco' host='localhost' port='5432'")
        return conexao
   except Exception as e:
        print("Não foi possível se conectar ao banco:", e)
        return None

def busca(conexao, consulta, parametros):
   try:
        if conexao is None:
            return []
        
        cursor = conexao.cursor()
        cursor.execute(consulta, parametros)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
   except Exception as e:
        print("Erro ao realizar a busca:", e)
        return []