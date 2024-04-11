# Prometheus Exporter for DockerHub Image Pulls

This Prometheus Exporter app gathers and exposes metrics detailing the count of Docker image pulls within a specified DockerHub organization. It operates on port 2113 and serves metrics through a GET request to /metrics.

# Installation and Setup

Clone the repository or download and unzip the app folder to your local system.

Navigate to the main folder.

Set your name and programming language in the settings.sh file. For example:

- CLUSTER_NAME=simon.ejilogo
- APP_LANGUAGE=python

Ensure you have the required tools installed and properly configured. Verify this by running:
- make check

# Configuration

#Environment Variables
DOCKERHUB_ORGANIZATION: Specify the name of the DockerHub organization. You can find this value in the .env file.

# Local Deployment
To run the app locally (non-dockerized), use:
- make run

Access the metrics by sending a GET request to http://localhost:2113/metrics.

You can test your app locally with:
- make test-local

# Kubernetes Deployment
To deploy the test cluster using kind, utilize the following command:
- make create

# Docker Deployment
To build and deploy the Docker image, execute:
- make build

# Prepare the test environment with:
- make prepare

# Test the app's functionality on the kind cluster:
- make test

# Cleanup
To teardown the local cluster and associated resources, run:
- make teardown
