import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import IsolationForest
import numpy as np

# 1. Ligar ao PostgreSQL local e extrair os dados guardados pela API Java
# Garante que a password está correta no URL de conexão abaixo
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/iot_telemetria_db"
engine = create_engine(DATABASE_URL)

print("🔍 A ler dados históricos do PostgreSQL via SQLAlchemy...")
df = pd.read_sql_table("dados_telemetria", con=engine)

if len(df) < 20:
    print("❌ Poucos dados na base de dados. Deixa o simulador correr mais um bocado antes de analisar!")
    exit()

print(f"📊 Registos encontrados para análise: {len(df)}")

# 2. Selecionar as colunas (features) que o modelo vai avaliar
features = ['velocidade', 'aceleracaox', 'aceleracaoy', 'temperatura']
X = df[features]

# 3. Inicializar e treinar o modelo Isolation Forest
# O 'contamination' define a percentagem estimada de dados que achamos ser anómalos (ex: 5%)
modelo = IsolationForest(contamination=0.05, random_state=42)
print("🧠 A treinar o modelo de Inteligência Artificial (Isolation Forest)...")
modelo.fit(X)

# 4. Prever anomalias
# O algoritmo devolve 1 para dados normais e -1 para anomalias
df['previsao'] = modelo.predict(X)

# 5. Filtrar e apresentar os resultados obtidos
anomalias = df[df['previsao'] == -1]

print("\n" + "="*50)
print(f"🚨 RESULTADO DA ANÁLISE IA: DETETADAS {len(anomalias)} ANOMALIAS! 🚨")
print("="*50)

if not anomalias.empty:
    print("\nÚltimos 5 momentos críticos detetados pelo algoritmo:")
    # Mostrar colunas relevantes para validação
    print(anomalias[['id', 'timestamp', 'velocidade', 'temperatura', 'aceleracaox']].tail(5).to_string(index=False))
    print("\n💡 Explicação de Engenharia: Repara como nos IDs acima a temperatura disparou ")
    print("   enquanto a velocidade caiu abruptamente, quebrando o padrão normal da pista!")
else:
    print("\n✅ Nenhum comportamento anómalo detetado. O sistema está estável.")