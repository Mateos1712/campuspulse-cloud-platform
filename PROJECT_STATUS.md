# Estado del proyecto

Fecha de inicio: 7 de septiembre de 2026.

## Entregado en el scaffold inicial

- [x] Project charter y arquitectura.
- [x] Matriz de requisitos de la vacante.
- [x] API Python instrumentada.
- [x] Pruebas unitarias iniciales.
- [x] Dockerfile multi-stage y usuario no-root.
- [x] Docker Compose con Prometheus y Grafana.
- [x] Dashboard y alertas provisionados como código.
- [x] Terraform modular para VPC, ECR, ECS Fargate, ALB, autoscaling y CloudWatch.
- [x] Jenkinsfile para CI/CD por ramas.
- [x] Validación de pull requests con Bitbucket Pipelines.
- [x] Rol Ansible para configurar Jenkins en Ubuntu.
- [x] Manifiestos Kubernetes y configuración EKS efímera.
- [x] Runbook, troubleshooting y pitch de entrevista.

## Verificaciones realizadas en este entorno

- [x] Compilación sintáctica de todos los archivos Python.
- [x] Validación JSON del dashboard de Grafana.
- [x] Validación sintáctica Bash de los scripts.
- [x] Revisión de llaves balanceadas en archivos Terraform.
- [x] Escaneo textual para evitar credenciales AWS y llaves privadas.
- [ ] Pruebas pytest y lint: requieren instalar dependencias del proyecto.
- [ ] Docker Compose: requiere Docker Engine activo.
- [ ] `terraform init/validate/plan`: requiere Terraform y acceso al registry del provider.
- [ ] Ansible check mode: requiere un host Ubuntu de laboratorio.
- [ ] Kubernetes dry-run: requiere kubectl y los CRD de Prometheus Operator.

## Próxima sesión recomendada

Empezar por **Semana 1 — Aplicación, pruebas y Docker**. No crear recursos AWS todavía. El objetivo será ejecutar localmente, entender cada archivo, generar métricas y realizar el primer pull request con evidencia.

