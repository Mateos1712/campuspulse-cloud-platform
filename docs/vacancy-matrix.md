# Matriz vacante → evidencia

| Requisito de Cloud Engineer | Evidencia en CampusPulse | Demostración final |
|---|---|---|
| Terraform | Módulos `network`, `ecr`, `ecs`; variables y outputs | `fmt`, `validate`, `plan`, `apply` y `destroy` |
| Ansible | Rol idempotente `jenkins` | Ejecutar dos veces y mostrar que la segunda no rehace configuración |
| Jenkins | `Jenkinsfile` declarativo | Pipeline por ramas con pruebas, escaneo, build, push, deploy y aprobación |
| Bitbucket | `bitbucket-pipelines.yml`, GitFlow y guía de webhook | Pull request y build disparado desde Bitbucket |
| Python | API, modelos, métricas y pruebas | Explicar middleware y automatizaciones |
| Bash/sh | Smoke test y generador de tráfico | Fallo controlado con código de salida distinto de cero |
| Docker | Multi-stage build y ejecución no-root | Construir una vez y usar la misma imagen en ECS/Kubernetes |
| ECS | Fargate service, task definition, ALB y autoscaling | Despliegue accesible y nueva revisión de tarea |
| Kubernetes | Deployment, Service, HPA, probes, PDB, NetworkPolicy | Despliegue en kind y después EKS efímero |
| Linux | Jenkins sobre Ubuntu y trabajo CLI | Diagnóstico de proceso, red, logs, permisos y disco |
| CI/CD | Flujo completo desde commit hasta smoke test | Comparar CI en PR contra CD en `develop`/`main` |
| Automatización y escalamiento | IaC, configuración, HPA y ECS autoscaling | Carga sintética y observación de métricas |
| Arquitecturas complejas | Dos runtimes, red, registro, CI y observabilidad | Diagrama y ADR explicados sin leer notas |
| Git/GitFlow | Convención de ramas y commits | Feature → PR → develop → release → main |
| Agile/Jira | Backlog `CAMPUS-*` con criterios de aceptación | Tablero Kanban y vínculo ticket-commit-PR |
| SOP y knowledge base | Runbook, arquitectura, ADR y troubleshooting | Resolver un incidente siguiendo el runbook |
| Comunicación escrita | README, diagramas y documentación en inglés/español | Presentación de cinco minutos y demo de diez minutos |

## Lo que debes poder afirmar al terminar

> Diseñé y automaticé una plataforma SaaS contenerizada en AWS. Aprovisioné la red, ECR, ECS Fargate, ALB, autoscaling y observabilidad mediante Terraform; configuré Jenkins con Ansible; implementé CI/CD desde Bitbucket; instrumenté la API con Prometheus y Grafana; y validé la portabilidad de la misma imagen en Kubernetes.

Esta frase solo debe usarse cuando todas las evidencias estén completas y disponibles en el repositorio.

