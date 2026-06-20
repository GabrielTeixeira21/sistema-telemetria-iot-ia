package com.example.sistema_telemetria;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/telemetria")
public class TelemetriaController {

    private final TelemetriaRepository repository;
    public TelemetriaController(TelemetriaRepository repository) {
        this.repository = repository;
    }

    // Endpoint para RECEBER dados (POST http://localhost:8080/api/telemetria)
    @PostMapping
    public ResponseEntity<DadosTelemetria> receberDados(@RequestBody DadosTelemetria novosDados) {
        // Se o cliente não enviar o timestamp, nós colocamos a hora atual do sistema
        if (novosDados.getTimestamp() == null) {
            novosDados.setTimestamp(java.time.LocalDateTime.now());
        }
        DadosTelemetria dadosSalvos = repository.save(novosDados);
        return ResponseEntity.ok(dadosSalvos);
    }

    // Endpoint para LISTAR todos os dados salvos (GET http://localhost:8080/api/telemetria)
    @GetMapping
    public ResponseEntity<List<DadosTelemetria>> listarDados() {
        List<DadosTelemetria> todosOsDados = repository.findAll();
        return ResponseEntity.ok(todosOsDados);
    }
}