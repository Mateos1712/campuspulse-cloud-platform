# Kubernetes deployment

## Local with kind

```bash
docker build -t campuspulse:local .
kind create cluster --name campuspulse
kind load docker-image campuspulse:local --name campuspulse
kubectl apply -k platform/kubernetes/base
kubectl -n campuspulse port-forward service/campuspulse 8000:80
```

The `ServiceMonitor` requires the Prometheus Operator. Install the `kube-prometheus-stack` Helm chart before applying it, or temporarily remove `service-monitor.yml` from `kustomization.yml` during the first Kubernetes exercise.

For EKS, replace the image in `kustomization.yml` with the immutable ECR URI produced by Jenkins. Create EKS only during Phase 7 and destroy it after collecting portfolio evidence.

## Ephemeral EKS demo

```bash
eksctl create cluster -f platform/eks/cluster.yml
kubectl get nodes

# Update the image to the immutable ECR URI before applying.
kubectl apply -k platform/kubernetes/base

# Destroy the paid control plane and workers after the demo.
eksctl delete cluster -f platform/eks/cluster.yml --wait
```

The EKS configuration intentionally uses one Spot worker for a short-lived portfolio demonstration. It is not a production high-availability topology.

