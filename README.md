# 🏎️ End-to-End IoT Telemetry Ingestion & AI Anomaly Detection System

This is a distributed ecosystem designed to simulate, ingest, persist, and analyze high-frequency streaming data from racing vehicle sensors or IoT devices.
The main goal of this project is to demonstrate an End-to-End (E2E) Architecture where data travels from the physical simulation on the track to an Artificial Intelligence analytical layer that identifies dynamic faults without relying on rigid, hardcoded thresholds.

## 🏗️ System Architecture

The ecosystem is divided into four main layers:
* **Generation Layer (Data Source):** A dynamic Python simulator that generates physical metrics every 500ms and injects controlled mechanical faults.
* **Ingestion & Business Layer (REST API):** A robust Java Spring Boot 3 microservice applying modern software design best practices.
* **Persistence Layer (Data Store):** A PostgreSQL relational database focused on a Time-Series / Event Log pattern.
* **Analytical Layer (AI Engine):** A Python module using Scikit-Learn for unsupervised Machine Learning auditing and anomaly isolation.

## 🛠️ Technologies & Patterns Used

### Backend (Java)
* **Spring Boot 3 & Spring Web:** Development of concurrent REST endpoints.
* **Spring Data JPA & Hibernate ORM:** Automatic object-relational mapping and SQL query abstraction.
* **Repository Pattern:** Decoupling the data layer while ensuring security against SQL Injection.
* **Inversion of Control (IoC) & Dependency Injection:** Lifecycle management and modularity via constructor injection (`private final`).
* **Lombok:** Reduction of boilerplate code via annotations.

### Artificial Intelligence & Simulation (Python)
* **Scikit-Learn (Isolation Forest):** Unsupervised Machine Learning algorithm focused on the geometric isolation of contextual anomalies.
* **Pandas:** Manipulation, cleaning, and analysis of structured time-series data.
* **SQLAlchemy & Psycopg2:** Native connection and optimized data extraction from PostgreSQL.
* **Requests:** HTTP communication with the Java ecosystem.

## 🧠 The AI Engine: Why Isolation Forest?

In industrial and high-performance systems, fixed thresholds (e.g., `if temperature > 100`) fail because a fault depends heavily on the track context (G-forces, current speed, etc.).
This system utilizes **Isolation Forest** (Unsupervised Learning) due to the natural scarcity of fault data in real-world scenarios. Instead of learning what a failure looks like, the algorithm learns the structure of normal on-track behavior.

Since anomalies are rare and distinct from normal data clusters, the model isolates them with very few splits in a randomized decision tree. The algorithm identifies a mechanical failure through sudden drops in expected correlation (e.g., temperature spiking to 200°C while acceleration drops sharply due to violent braking), assigning these data rows an anomaly score of `-1`.

## 🚀 How to Run the Project

### 1. Prerequisites
* Java 21+ installed.
* PostgreSQL running with a database named `iot_telemetria_db` created.
* Python 3.10+ installed.

### 2. Running the Backend (Java)
Configure your credentials in the `src/main/resources/application.properties` file and run the main application:
```bash
# Hibernate will automatically generate the database tables in PostgreSQL
./mvnw spring-boot:run
