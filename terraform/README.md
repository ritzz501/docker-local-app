# Terraform Infrastructure CI

## Objective
Automate Terraform plan validation using GitHub Actions.

## Pipeline
1. Checkout repository.
2. Setup Terraform.
3. Check Terraform formatting.
4. Initialize Terraform.
5. Validate configuration.
6. Generate Terraform execution plan.
7. Upload plan artifact.

## Trigger
Runs on every push and pull request.

## Artifact
terraform-plan containing the binary plan and readable report.

## Note
This project validates Terraform configuration without deploying cloud infrastructure.
