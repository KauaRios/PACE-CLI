import sqlite3

# conexão com db
con = sqlite3.connect("pace.db")

cur = con.cursor()

#dados ficticios para teste
corridas = [
    ("2026-06-25", "Corrida_Rua", 5.0, 1530), # 1530s = 25m30s
    ("2026-06-26", "HIIT_Esteira", 3.0, 900), # 900s = 15m
    ("2026-06-27", "Corrida_Rua", 10.0, 3120) # 3120s = 52m
]

cur.execute("""CREATE TABLE IF NOT EXISTS SessoesCardio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_sessao TEXT,
    tipo TEXT,
    distancia_km REAL,
    duracao_segundos INTEGER
)""")



cur.executemany("""INSERT INTO SessoesCardio (data_sessao, tipo, distancia_km, duracao_segundos) 
VALUES (?, ?, ?, ?)""", corridas)
con.commit()



cur.execute("""SELECT * FROM SessoesCardio""")


meus_dados = cur.fetchall()


# print(meus_dados)



#logica matematica
for corrida in meus_dados:
    distancia=corrida[3]
    tempo=corrida[4]
    pace_em_segundos=tempo/distancia
    minutos_pace=int(pace_em_segundos//60)
    segundos_pace=int(pace_em_segundos % 60)



    print(f"Na corrida do dia {corrida[1]}, o pace foi de {minutos_pace} Minutos e {segundos_pace} Segundos") 