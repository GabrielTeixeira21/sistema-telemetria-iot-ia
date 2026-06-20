import time
import random
import requests

# URL da nossa API Java
URL_API = "http://localhost:8080/api/telemetria"

print("🏎️ Simulador IoT de Alta Performance Iniciado...")
print("A enviar dados em tempo real para a API Java. Prime Ctrl+C para parar.\n")

tempo_decorrido = 0
velocidade_atual = 0.0
temperatura_atual = 40.0

try:
    while True:
        tempo_decorriona = tempo_decorrido + 1
        
        # Simulação de comportamento dinâmico normal
        if tempo_decorrido < 30:  # Primeiros 15 segundos: Aceleração contínua
            velocidade_atual += random.uniform(3.0, 6.0)
            aceleracao_x = random.uniform(1.5, 2.5)  # Força linear
            aceleracao_y = random.uniform(-0.5, 0.5) # Pouca curva
            temperatura_atual += random.uniform(0.5, 1.2)
        else:  # Depois estabiliza com oscilações normais de pista
            velocidade_atual = random.uniform(180.0, 210.0)
            aceleracao_x = random.uniform(-1.0, 1.0)
            aceleracao_y = random.uniform(-2.0, 2.0) # Forças G laterais em curvas
            temperatura_atual += random.uniform(-0.2, 0.4)

        # ---- INJEÇÃO DE ANOMALIA AUTOMÁTICA ----
        # Aos 40 segundos, simulamos uma falha crítica (motor a queimar / quebra mecânica)
        if 40 <= tempo_decorrido <= 45:
            print("⚠️ [INJEÇÃO DE ANOMALIA] A simular falha no sistema...")
            velocidade_atual = max(0.0, velocidade_atual - random.uniform(25.0, 40.0))
            temperatura_atual += random.uniform(5.0, 12.0) # Temperatura dispara drasticamente
            aceleracao_x = random.uniform(-3.5, -2.5)       # Travagem violenta

        # Garantir limites lógicos
        velocidade_atual = round(max(0.0, velocidade_atual), 2)
        temperatura_atual = round(max(20.0, temperatura_atual), 2)
        aceleracao_x = round(aceleracao_x, 2)
        aceleracao_y = round(aceleracao_y, 2)

        # Montar o JSON igualzinho ao que usámos no Postman
        payload = {
            "velocidade": velocidade_atual,
            "aceleracaoX": aceleracao_x,
            "aceleracaoY": aceleracao_y,
            "temperatura": temperatura_atual
        }

        # Enviar os dados para a API Java via POST
        try:
            response = requests.post(URL_API, json=payload)
            if response.status_code == 200:
                print(f"✅ [Envio OK] Vol: {velocidade_atual}km/h | Temp: {temperatura_atual}ºC | G-X: {aceleracao_x}")
            else:
                print(f"❌ Erro no servidor: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print("❌ Erro: Não foi possível ligar à API Java. Garante que o Spring Boot está a correr!")

        # Atualiza a contagem e espera 500ms (0.5 segundos) para o próximo envio
        tempo_decorrido += 0.5
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n🛑 Simulador desligado pelo utilizador.")