variable "project_name" {
  description = "Project name used for resource names."
  type        = string
}

variable "environment" {
  description = "Environment name used for resource names."
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC."
  type        = string
}

