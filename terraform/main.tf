terraform {
  required_version = ">= 1.4.0"
}

resource "terraform_data" "infrastructure" {
  input = {
    project = "docker-local-app"
    purpose = "Terraform CI Plan Validation"
    status  = "Infrastructure CI Trigger"
  }
}
