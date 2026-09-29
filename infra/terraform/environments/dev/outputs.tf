output "vpc_id" {
  description = "ID of the CampusPulse VPC."
  value       = module.network.vpc_id
}

output "ecr_repository_url" {
  description = "Repository URL used by the CI pipeline."
  value       = module.ecr.repository_url
}

output "application_url" {
  description = "HTTP endpoint of the development service when enabled."
  value       = var.enable_runtime ? module.ecs[0].application_url : null
}

output "ecs_cluster_name" {
  description = "ECS cluster name when the runtime is enabled."
  value       = var.enable_runtime ? module.ecs[0].cluster_name : null
}

output "ecs_service_name" {
  description = "ECS service name when the runtime is enabled."
  value       = var.enable_runtime ? module.ecs[0].service_name : null
}

