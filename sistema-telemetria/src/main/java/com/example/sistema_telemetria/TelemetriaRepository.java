package com.example.sistema_telemetria;

import org.springframework.data.jpa.repository.JpaRepository;

public interface TelemetriaRepository extends JpaRepository<DadosTelemetria, Long> {
}