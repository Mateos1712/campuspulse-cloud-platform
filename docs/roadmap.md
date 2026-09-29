# Roadmap guiado

Duración sugerida: **7 semanas**, aproximadamente una hora de lunes a viernes y una sesión más larga durante el fin de semana. Cada fase termina con evidencia visible y un commit etiquetado.

## Fase 0 — Preparación y control de costos

Tickets: `CAMPUS-1` a `CAMPUS-4`.

- [ ] Crear repositorio `campuspulse-cloud-platform` en Bitbucket.
- [ ] Mantener un espejo público en GitHub para reclutadores.
- [ ] Configurar ramas `main` y `develop`, restricciones y pull requests.
- [ ] Crear un tablero Jira Kanban: Backlog, Selected, In progress, Review, Done.
- [ ] Configurar un presupuesto y alarma de facturación en AWS.
- [ ] Revisar identidad activa con `aws sts get-caller-identity`.
- [ ] Copiar `.env.example` a `.env`; nunca versionar `.env`.

**Aceptación:** repositorios creados, tablero visible y alarma de costo configurada.

## Semana 1 — Aplicación, pruebas y Docker

Tickets: `CAMPUS-10` a `CAMPUS-15`.

- [ ] Ejecutar la API localmente.
- [ ] Entender cada endpoint y modelo.
- [ ] Ejecutar las cuatro pruebas.
- [ ] Construir el target Docker `test` y el target `runtime`.
- [ ] Confirmar que el contenedor corre con UID `10001`.
- [ ] Generar una versión defectuosa en una rama y comprobar que CI falla.
- [ ] Abrir y fusionar una pull request hacia `develop`.

**Aceptación:** pruebas verdes, imagen funcional, PR revisada y commit `feat(app): add observable engagement api`.

## Semana 2 — Prometheus, Grafana y SLO

Tickets: `CAMPUS-20` a `CAMPUS-25`.

- [ ] Iniciar `docker compose`.
- [ ] Generar tráfico con `scripts/generate_traffic.sh`.
- [ ] Explicar Counter, Gauge e Histogram.
- [ ] Verificar request rate, error ratio y latencia p95 en Grafana.
- [ ] Activar intencionalmente una alarma de laboratorio.
- [ ] Documentar el SLO y la investigación.

**Aceptación:** dashboard capturado, PromQL explicado y evidencia de una alerta.

## Semana 3 — Terraform y ECS Fargate

Tickets: `CAMPUS-30` a `CAMPUS-38`.

- [ ] Ejecutar `terraform fmt`, `init`, `validate` y `plan`.
- [ ] Aplicar con `enable_runtime=false` para crear VPC y ECR.
- [ ] Construir y publicar la primera imagen con un tag SHA.
- [ ] Aplicar con `enable_runtime=true` y el SHA publicado.
- [ ] Validar ALB, health checks, logs y ECS Exec.
- [ ] Generar tráfico y revisar CloudWatch.
- [ ] Destruir el entorno y confirmar que no quedan recursos facturables.

**Aceptación:** servicio accesible desde el ALB, plan conservado sin secretos y destrucción validada.

## Semana 4 — Ansible y Jenkins

Tickets: `CAMPUS-40` a `CAMPUS-47`.

- [ ] Preparar una VM Ubuntu efímera para Jenkins.
- [ ] Ejecutar el rol Ansible.
- [ ] Repetir el playbook para verificar idempotencia.
- [ ] Completar el asistente inicial de Jenkins.
- [ ] Crear credenciales de Bitbucket sin guardarlas en archivos.
- [ ] Configurar el rol IAM del host para ECR/ECS con privilegios mínimos.
- [ ] Importar el `Jenkinsfile` como multibranch pipeline.

**Aceptación:** Jenkins configurado desde Ansible y segundo playbook sin cambios injustificados.

## Semana 5 — CI/CD, Bitbucket y GitFlow

Tickets: `CAMPUS-50` a `CAMPUS-58`.

- [ ] Configurar webhook con secret o SCM polling mientras Jenkins permanezca privado.
- [ ] Confirmar CI para pull requests.
- [ ] Confirmar CD automático para `develop`.
- [ ] Implementar aprobación manual para `main`.
- [ ] Etiquetar imágenes con SHA y releases con SemVer.
- [ ] Probar rollback a un SHA anterior.
- [ ] Medir duración y tasa de éxito de los pipelines.

**Aceptación:** video continuo commit → pipeline → ECS → smoke test y rollback probado.

## Semana 6 — Kubernetes

Tickets: `CAMPUS-60` a `CAMPUS-67`.

- [ ] Crear cluster local con kind.
- [ ] Cargar la misma imagen construida para ECS.
- [ ] Explicar Deployment, Service, probes, requests, limits, HPA y PDB.
- [ ] Instalar Prometheus Operator y aplicar `ServiceMonitor`.
- [ ] Verificar el dashboard de Grafana.
- [ ] Ejecutar un rolling update y rollback.

**Aceptación:** pods saludables, métricas disponibles y rollback Kubernetes demostrado.

## Semana 7 — EKS efímero, incidente y presentación

Tickets: `CAMPUS-70` a `CAMPUS-78`.

- [ ] Crear EKS solo para la sesión de demostración.
- [ ] Desplegar la imagen inmutable de ECR.
- [ ] Generar carga y revisar escalamiento.
- [ ] Simular una versión con fallo de readiness.
- [ ] Seguir el runbook y restaurar servicio.
- [ ] Grabar una demo técnica de 8 a 10 minutos.
- [ ] Preparar pitch de 90 segundos en inglés.
- [ ] Destruir EKS el mismo día y comprobar costos.

**Aceptación:** demo grabada, incidente documentado, infraestructura destruida y matriz de vacante completa.

## Regla de aprendizaje

Cada ticket debe cerrar con cuatro elementos:

1. Qué problema resolviste.
2. Qué comando o cambio hiciste.
3. Cómo comprobaste el resultado.
4. Qué harías distinto en producción.

