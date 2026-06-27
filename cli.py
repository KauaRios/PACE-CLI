import sqlite3
import sys
from datetime import datetime

# codigo Feito por Kauã---------------

# Função utilitária para pegar números sem quebrar o programa
def obter_numero_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("Por favor, digite um valor maior que zero.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número.")

# Função para tratar a data
def obter_data_valida(mensagem):
    while True:
        data_str = input(mensagem)
        try:
            datetime.strptime(data_str, '%Y-%m-%d')
            return data_str
        except ValueError:
            print("Erro: Use o formato AAAA-MM-DD e certifique-se de que a data existe.")

def ver_banco(): 
    con = None
    try:
        con = sqlite3.connect("pace.db")
        cur = con.cursor()
        
        # Faz o SELECT
        cur.execute("SELECT * FROM SessoesCardio")
        meus_dados = cur.fetchall()

        if not meus_dados:
            print("\nNenhuma corrida cadastrada ainda.")
            return

        # Logica matematica
        print("\n--- Histórico de Paces ---")
        for corrida in meus_dados:
            distancia = corrida[3]
            tempo = corrida[4]
            pace_em_segundos = tempo / distancia
            minutos_pace = int(pace_em_segundos // 60)
            segundos_pace = int(pace_em_segundos % 60)

            print(f"[ID: {corrida[0]}] Na corrida do dia {corrida[1]}, o pace foi de {minutos_pace} Minutos e {segundos_pace} Segundos")
            
    except sqlite3.OperationalError:
        print("\nNenhuma corrida cadastrada ainda. O banco está vazio.")
    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
    finally:
        if con:
            con.close()

def cadastrar_corrida():
    print("\n--- Cadastro de Corrida ---")
    data_input = obter_data_valida("Data (AAAA-MM-DD): ")
    tipo_input = input("Tipo (Ex: Corrida na rua): ")
    distancia_input = obter_numero_positivo("Distância (km): ")
    minutos = int(obter_numero_positivo("Minutos: "))
    segundos = int(obter_numero_positivo("Segundos: "))
    tempo_total = (minutos * 60) + segundos

    con = None
    try:    
        con = sqlite3.connect("pace.db")
        cur = con.cursor()
    
        cur.execute("""CREATE TABLE IF NOT EXISTS SessoesCardio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_sessao TEXT,
            tipo TEXT,
            distancia_km REAL,
            duracao_segundos INTEGER
        )""")

        # Verifica se já existe a data
        cur.execute("SELECT id FROM SessoesCardio WHERE data_sessao = ?", (data_input,))
        if cur.fetchone():
            print(f"Atenção: Já existe um registro para o dia {data_input}.")
            confirmacao = input("Deseja salvar esta corrida mesmo assim? (s/n): ").lower()
            if confirmacao != 's':
                print("Cadastro cancelado.")
                return 

        cur.execute("""INSERT INTO SessoesCardio (data_sessao, tipo, distancia_km, duracao_segundos) 
                       VALUES (?, ?, ?, ?)""", (data_input, tipo_input, distancia_input, tempo_total))
        con.commit()
        print("Sucesso: Dados salvos!")




        

    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
    finally:
        if con:
            con.close()

def deletar_corrida():
    print("\n--- Deletar Registro ---")
    ver_banco() 
    
    print("\n[Dica: Digite 0 se quiser cancelar e voltar ao menu]")
    id_para_deletar = int(obter_numero_positivo("Digite o ID da corrida que deseja apagar: "))
    
    if id_para_deletar == 0:
        print("Operação cancelada.")
        return

    con = None
    try:
        con = sqlite3.connect("pace.db")
        cur = con.cursor()
        
        
        cur.execute("SELECT id FROM SessoesCardio WHERE id = ?", (id_para_deletar,))
        if not cur.fetchone():
            print("Erro: Nenhum registro encontrado com esse ID.")
            return

        
        cur.execute("DELETE FROM SessoesCardio WHERE id = ?", (id_para_deletar,))
        con.commit()
        print(f"Sucesso: O registro {id_para_deletar} foi apagado para sempre!")

    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
    finally:
        if con:
            con.close()


#  Fluxo Principal 
while True:
    print("\n" + "="*30)
    print("      SISTEMA DE CORRIDA      ")
    print("="*30)
    print("1 - Cadastrar nova corrida")
    print("2 - Ver histórico de paces")
    print("3 - Deletar uma corrida")
    print("4 - Sair") 
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        cadastrar_corrida()
    elif escolha == '2':
        ver_banco()
    elif escolha == '3':
        deletar_corrida() 
    elif escolha == '4':
        print("Saindo do sistema... Bons treinos!")
        sys.exit() 
    else:
        print("Opção inválida. Tente novamente.")