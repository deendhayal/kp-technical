
variable "project_id" {
  description = "The ID of the project in which resources will be provisioned."
  type        = string
}

variable "db_name" {
  description = "The name of the SQL Database instance"
  type        = string
}

variable "authorized_networks" {
#   example = [{
#     name  = "sample-gcp-health-checkers-range"
#     value = "130.211.0.0/28"
#   }]
  type        = list(map(string))
  description = "List of mapped public networks authorized to access to the instances. Default - short range of GCP health-checkers IPs"
  default = []
}

variable "db_version" {
  description = "Database version"
  default     = "MYSQL_5_6"
}