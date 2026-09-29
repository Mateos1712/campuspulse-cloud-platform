variable "project_name" {
  description = "Project name used for resource names."
  type        = string
}

variable "environment" {
  description = "Environment name used for resource names."
  type        = string
}

variable "vpc_id" {
  description = "VPC ID for the load balancer and service."
  type        = string
}

variable "public_subnets" {
  description = "Subnet IDs for the ALB and Fargate tasks in the low-cost dev design."
  type        = list(string)
}

variable "image_uri" {
  description = "Full ECR image URI including immutable tag."
  type        = string
}

variable "desired_count" {
  description = "Desired number of Fargate tasks."
  type        = number
}

