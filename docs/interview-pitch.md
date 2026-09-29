# Pitch para entrevista

## Español — 90 segundos

CampusPulse es un proyecto que diseñé para demostrar el ciclo completo de modernización de una aplicación hacia un modelo SaaS. Construí una API Python con métricas de Prometheus y la empaqueté en una imagen Docker que se ejecuta como usuario no root. La infraestructura de AWS está definida con módulos de Terraform e incluye VPC, ECR, ECS Fargate, un Application Load Balancer, autoscaling, logs, métricas y alarmas de CloudWatch.

Configuré Jenkins con Ansible y definí el pipeline como código. Desde Bitbucket, cada cambio pasa por pruebas, lint, análisis de seguridad, validación de Terraform, construcción de una imagen inmutable y despliegue con prueba de humo. Para demostrar portabilidad, la misma imagen también se ejecuta en Kubernetes con probes, HPA, límites de recursos y monitoreo en Grafana.

Además del despliegue, documenté decisiones, procedimientos de operación, rollback y respuesta a incidentes. Mi objetivo fue demostrar no solamente que puedo crear recursos cloud, sino que puedo convertir requisitos en una solución automatizada, escalable y operable.

## English — 90 seconds

CampusPulse is a portfolio project I designed to demonstrate the complete modernization lifecycle of a SaaS application. I built an observable Python API and packaged it as a non-root Docker container. I defined the AWS infrastructure with reusable Terraform modules, including a VPC, Amazon ECR, ECS Fargate, an Application Load Balancer, service autoscaling, CloudWatch logs, metrics, and alarms.

I configured Jenkins through Ansible and implemented the delivery workflow as code. Starting from Bitbucket, every change goes through automated tests, linting, security checks, Terraform validation, immutable image creation, deployment, and smoke testing. I also deploy the same image to Kubernetes with health probes, resource controls, horizontal scaling, and Prometheus/Grafana monitoring.

Beyond deployment, I documented architecture decisions, operating procedures, rollback, and incident response. The project shows that I can translate requirements into an automated, scalable, and supportable cloud solution.

