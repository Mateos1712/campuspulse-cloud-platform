# Runbook operacional

## Despliegue de desarrollo

1. Verificar identidad y región:

   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```

2. Validar IaC:

   ```bash
   cd infra/terraform/environments/dev
   terraform fmt -check -recursive
   terraform init
   terraform validate
   terraform plan -out=campuspulse.tfplan
   ```

3. Crear VPC y ECR antes de la primera imagen:

   ```bash
   terraform apply -var='enable_runtime=false'
   ```

4. Construir y publicar la imagen con el SHA del commit.
5. Crear o actualizar el runtime:

   ```bash
   terraform apply \
     -var='enable_runtime=true' \
     -var="image_tag=$(git rev-parse --short=12 HEAD)"
   ```

6. Ejecutar la prueba de humo contra `terraform output -raw application_url`.

## Diagnóstico de incidente

Orden recomendado:

1. Confirmar el impacto y registrar hora de inicio.
2. Revisar health check del ALB y eventos del servicio ECS.
3. Revisar la última ejecución de Jenkins y el SHA desplegado.
4. Consultar logs de aplicación en CloudWatch.
5. Revisar CPU, memoria, respuestas 5xx y latencia.
6. Comparar la revisión actual con la última conocida como estable.
7. Decidir corrección directa o rollback.

Comandos útiles:

```bash
aws ecs describe-services --cluster campuspulse-dev --services campuspulse-dev
aws ecs list-tasks --cluster campuspulse-dev --service-name campuspulse-dev
aws logs tail /ecs/campuspulse-dev --since 15m --follow
```

## Rollback ECS

1. Identificar el último SHA estable en ECR/Jenkins.
2. Aplicar Terraform con ese `image_tag`:

   ```bash
   terraform apply \
     -var='enable_runtime=true' \
     -var='image_tag=REPLACE_WITH_STABLE_SHA'
   ```

3. Esperar estabilidad del servicio:

   ```bash
   aws ecs wait services-stable \
     --cluster campuspulse-dev \
     --services campuspulse-dev
   ```

4. Ejecutar `scripts/smoke_test.sh`.
5. Registrar causa, recuperación y acción preventiva.

## Rollback Kubernetes

```bash
kubectl -n campuspulse rollout status deployment/campuspulse
kubectl -n campuspulse rollout history deployment/campuspulse
kubectl -n campuspulse rollout undo deployment/campuspulse
kubectl -n campuspulse rollout status deployment/campuspulse
```

## Destrucción del laboratorio

```bash
cd infra/terraform/environments/dev
terraform destroy
```

Después, verificar manualmente EKS, NAT Gateway, ALB, ECS, EC2 y volúmenes. Un `destroy` exitoso no sustituye la revisión de facturación.

## Plantilla de postmortem

- Incidente:
- Inicio y fin:
- Impacto:
- Detección:
- Línea de tiempo:
- Causa raíz:
- Resolución:
- Qué funcionó:
- Qué falló:
- Acciones preventivas y propietario:

