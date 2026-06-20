# 🏎️ Sistema End-to-End de Ingestão de Telemetria IoT & Deteção de Anomalias com IA

Este é um ecossistema distribuído concebido para simular, ingerir, persistir e analisar fluxos de dados (streaming) de alta frequência provenientes de sensores de um veículo de competição ou dispositivo IoT. 

O principal objetivo do projeto é demonstrar uma **Arquitetura End-to-End (E2E)** onde o dado viaja desde a simulação física na pista até uma camada analítica de Inteligência Artificial que identifica falhas dinâmicas, sem depender de limites rígidos (*hardcoded*).

---

## 🏗️ Arquitetura do Sistema

O ecossistema está dividido em quatro camadas principais:

1. **Camada de Geração (Data Source):** Um simulador dinâmico em **Python** que gera métricas físicas a cada 500ms e injeta falhas mecânicas controladas.
2. **Camada de Ingestão & Negócio (REST API):** Um microsserviço robusto em **Java Spring Boot 21** aplicando as melhores práticas de design.
3. **Camada de Persistência (Data Store):** Base de dados relacional **PostgreSQL** focada no padrão *Time-Series / Log de Eventos*.
4. **Camada Analítica (AI Engine):** Módulo em **Python** com **Scikit-Learn** para auditoria e isolamento de anomalias por Machine Learning não supervisionado.

---

## 🛠️ Tecnologias & Padrões Utilizados

### Backend (Java)
* **Spring Boot 21 & Spring Web:** Criação de endpoints REST concorrentes.
* **Spring Data JPA & Hibernate ORM:** Mapeamento objeto-relacional automático e abstração de queries SQL.
* **Repository Pattern:** Desacoplamento da camada de dados garantindo segurança contra *SQL Injection*.
* **Inversão de Controlo (IoC) & Injeção de Dependências:** Gestão de ciclo de vida e modularidade via construtores (`private final`).
* **Lombok:** Redução de *boilerplate code* via anotações.

### Inteligência Artificial & Simulação (Python)
* **Scikit-Learn (Isolation Forest):** Algoritmo de Machine Learning não supervisionado focado em isolamento geométrico de anomalias contextuais.
* **Pandas:** Manipulação, limpeza e análise de séries temporais estruturadas.
* **SQLAlchemy & Psycopg2:** Conexão nativa e extração de dados otimizada a partir do PostgreSQL.
* **Requests:** Comunicação HTTP assíncrona com o ecossistema Java.

---

## 🧠 O Motor de IA: Porquê o Isolation Forest?

Em sistemas industriais e de alta performance, os limites fixos (ex: `if temperatura > 100`) falham porque uma falha depende do contexto de pista (forças G, velocidade atual, etc.). 

Este sistema utiliza **Isolation Forest (Aprendizagem Não Supervisionada)** devido à escassez natural de dados de falhas em cenários reais. Em vez de aprender o que é uma avaria, o algoritmo aprende a estrutura do comportamento normal em pista. 

Como as anomalias são raras e geograficamente distantes do aglomerado normal, o modelo isola-as com muito poucas divisões numa árvore de decisão aleatória. O algoritmo identifica a quebra mecânica através da quebra brusca de correlação (ex: temperatura a disparar a 200ºC com aceleração em valores severamente negativos devido a travagens mecânicas violentas), atribuindo a estas linhas a classificação de **`-1`**.

---

## 🚀 Como Executar o Projeto

### 1. Requisitos Prévios
* Java 21+ instalado.
* PostgreSQL com a base de dados `iot_telemetria_db` criada.
* Python 3.10+ instalado.

### 2. Executar o Backend (Java)
Configure as suas credenciais no ficheiro `src/main/resources/application.properties` e corra a aplicação principal:
```bash
# O Hibernate criará as tabelas automaticamente no PostgreSQL
./mvnw spring-boot:run