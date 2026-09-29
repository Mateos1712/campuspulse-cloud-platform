variable "aws_region" {
  description = "AWS region for the development environment."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name prefix for project resources."
  type        = string
  default     = "campuspulse"
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"
}

variable "owner" {
  description = "Owner tag used for cost attribution."
  type        = string
  default     = "amateos"
}

variable "vpc_cidr" {
  description = "CIDR block for the project VPC."
  type        = string
  default     = "10.40.0.0/16"
}

variable "enable_runtime" {
  description = "Create the ECS runtime and ALB after the first image exists in ECR."
  type        = bool
  default     = false
}

variable "image_tag" {
  description = "Immutable image tag deployed to ECS, normally the Git commit SHA."
  type        = string
  default     = "bootstrap"
}

variable "desired_count" {
  description = "Number of Fargate tasks for the development environment."
  type        = number
  default     = 1

  validation {
    condition     = var.desired_count >= 1 && var.desired_count <= 3
    error_message = "desired_count must be between 1 and 3 for this lab."
  }
}

