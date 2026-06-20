package com.example.sistema_telemetria;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Entity
@Table(name = "dados_telemetria")
@Data // O Lombok gera automaticamente os getters, setters, toString, etc.
public class DadosTelemetria {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime timestamp;
    private Double velocidade;
    private Double aceleracaoX;
    private Double aceleracaoY;
    private Double temperatura;
}
