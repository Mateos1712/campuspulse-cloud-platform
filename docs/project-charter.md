# Project charter — CampusPulse

## Problema

Una institución de educación superior necesita publicar un servicio de participación académica de forma repetible, segura y observable. El equipo recibe cambios frecuentes y requiere reducir despliegues manuales, detectar regresiones y recuperar el servicio rápidamente.

## Solución

CampusPulse automatiza el ciclo completo:

1. Un cambio nace en una rama `feature/*` asociada a un ticket Jira.
2. Bitbucket valida la pull request.
3. Jenkins ejecuta pruebas, lint, auditoría, validación de Terraform y construcción de la imagen.
4. La imagen inmutable se publica en Amazon ECR con el SHA del commit.
5. Terraform despliega la versión en ECS Fargate detrás de un Application Load Balancer.
6. El pipeline ejecuta una prueba de humo.
7. CloudWatch y Prometheus/Grafana permiten observar logs, tráfico, errores y latencia.
8. La misma imagen puede ejecutarse en Kubernetes sin modificar la aplicación.

## Alcance

### Incluido

- API Python con datos exclusivamente sintéticos.
- CI/CD, IaC, configuración, contenedores y observabilidad.
- Entornos local y AWS `dev`.
- Despliegue principal ECS Fargate y despliegue alternativo Kubernetes.
- Documentación técnica y operativa.

### Fuera de alcance inicial

- Datos personales o expedientes reales.
- Integración con sistemas reales de Ellucian.
- Dominio productivo y certificados públicos permanentes.
- EKS permanente.
- Alta disponibilidad empresarial de Jenkins.

## Indicadores de éxito

- El 100% de la infraestructura del entorno `dev` se crea desde Terraform.
- Una pull request defectuosa no puede superar las pruebas.
- Cada imagen desplegada se identifica por SHA, nunca por `latest`.
- El pipeline puede desplegar y comprobar `/healthz` automáticamente.
- Grafana muestra tasa de solicitudes, errores, latencia p95 y eventos.
- Existe un procedimiento probado de rollback.
- El repositorio permite explicar claramente al menos cinco decisiones técnicas.

## SLO de laboratorio

- Disponibilidad objetivo durante demostración: 99.5%.
- Latencia p95: menor a 500 ms.
- Tasa de respuestas 5xx: menor a 5% durante cinco minutos.
- Tiempo objetivo de recuperación de una versión defectuosa: menor a 15 minutos.

