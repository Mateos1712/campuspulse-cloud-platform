# Knowledge base — troubleshooting

## ECS tasks do not start

Check, in order:

1. The image tag exists in `campuspulse-dev` ECR.
2. The task execution role can pull from ECR and write logs.
3. The Fargate subnets assign a public IP in the development design.
4. The task stopped reason and container reason.
5. The health command can reach `127.0.0.1:8000/healthz`.

## ALB reports unhealthy targets

- Confirm target type is `ip`, required for Fargate with `awsvpc`.
- Confirm the target group checks `/healthz` on port 8000.
- Confirm the service security group accepts port 8000 only from the ALB security group.
- Review application startup logs and the 60-second health-check grace period.

## Jenkins cannot run Docker

- Confirm `/var/run/docker.sock` is mounted.
- Compare the socket group ID on the host with `group_add` in Compose.
- Confirm Docker is active: `systemctl status docker`.
- Do not solve the problem by making the socket world-writable.

## Jenkins cannot push to ECR

- Run `aws sts get-caller-identity` from the Jenkins container.
- Confirm the host role or injected credentials have least-privilege ECR permissions.
- Confirm `AWS_REGION=us-east-1` and repository name `campuspulse-dev`.
- Confirm the tag was not already published; the repository is immutable by design.

## Prometheus target is down

- Open Prometheus → Status → Targets.
- From the Prometheus container, resolve `app` and request `http://app:8000/metrics`.
- Confirm both services share the `campuspulse` network.
- Confirm the API exposes metrics in Prometheus text format.

## Grafana dashboard has no data

- Confirm the provisioned data source UID is `prometheus`.
- Generate traffic using `scripts/generate_traffic.sh`.
- Test the PromQL expression directly in Prometheus.
- Expand the dashboard time range to the last hour.

## Kubernetes pods are not ready

```bash
kubectl -n campuspulse get pods
kubectl -n campuspulse describe pod POD_NAME
kubectl -n campuspulse logs POD_NAME
kubectl -n campuspulse get events --sort-by=.lastTimestamp
```

For kind, ensure `campuspulse:local` was loaded into the named cluster. For EKS, ensure the manifest references a reachable ECR image and the nodes can pull it.

