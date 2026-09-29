module "network" {
  source = "../../modules/network"

  project_name = var.project_name
  environment  = var.environment
  vpc_cidr     = var.vpc_cidr
}

module "ecr" {
  source = "../../modules/ecr"

  project_name = var.project_name
  environment  = var.environment
}

module "ecs" {
  count  = var.enable_runtime ? 1 : 0
  source = "../../modules/ecs"

  project_name   = var.project_name
  environment    = var.environment
  vpc_id         = module.network.vpc_id
  public_subnets = module.network.public_subnet_ids
  image_uri      = "${module.ecr.repository_url}:${var.image_tag}"
  desired_count  = var.desired_count
}

