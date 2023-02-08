resource "random_id" "name" {
  byte_length = 2
}

module "mysql-db" {
  source               = "../../modules/mysql"
  name                 = var.db_name
  random_instance_name = true
  database_version     = var.db_version
  project_id           = var.project_id
  zone                 = "us-central1-c"
  region               = "us-central1"
  tier                 = "db-n1-standard-1"

  deletion_protection = false

  ip_configuration = {
    ipv4_enabled        = true
    private_network     = null
    require_ssl         = false
    allocated_ip_range  = null
    authorized_networks = var.authorized_networks
  }

}
