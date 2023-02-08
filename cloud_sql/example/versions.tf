terraform {
  backend "gcs" {
    bucket = "bucket_name"
    prefix = "mysql-public"
    #credentials = "service-account.json"
  }
  required_providers {
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 4.0"
    }
  }
  required_version = ">= 0.13"
}