terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("playground-s-11-a07c7985-387966409d32.json")

  project = "playground-s-11-a07c7985"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_storage_bucket" "bucket" {
  name     = "playground-s-11-a07c7985-test-bucket"
  location = "us-central1"
}

resource "google_storage_bucket_object" "archive" {
  name   = "main.zip"
  bucket = google_storage_bucket.bucket.name
  source = "./code/function.zip"
}

resource "google_cloudfunctions_function" "function" {
  name        = "function-test"
  description = "My function"
  runtime     = "python39"

  available_memory_mb          = 128
  source_archive_bucket        = google_storage_bucket.bucket.name
  source_archive_object        = google_storage_bucket_object.archive.name
  trigger_http                 = true
  timeout                      = 60
  entry_point                  = "hello_world"
  labels = {
    my-label = "my-label-value"
  }

  environment_variables = {
    MY_ENV_VAR = "my-env-var-value"
  }
}


