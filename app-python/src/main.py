
# import os
# import time
# import requests
# from prometheus_client import start_http_server, Gauge
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Environment variables
# DOCKERHUB_ORGANIZATION = os.getenv('DOCKERHUB_ORGANIZATION')

# # Function to fetch Docker image pulls from DockerHub API
# def fetch_docker_image_pulls(organization):
#     url = f"https://hub.docker.com/v2/repositories/{organization}/?page_size=25&page=1"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data['results']

# # Prometheus metrics
# DOCKER_IMAGE_PULLS = Gauge('docker_image_pulls', 'The total number of Docker image pulls', ['organization', 'image'])

# # Function to update Prometheus metrics
# def update_prometheus_metrics():
#     # Fetch Docker image pulls
#     image_pulls = fetch_docker_image_pulls(DOCKERHUB_ORGANIZATION)

#     # Update Prometheus metrics
#     for image_data in image_pulls:
#         image_name = image_data['name']
#         pull_count = image_data['pull_count']
#         organization = DOCKERHUB_ORGANIZATION

#         # Set Prometheus metric
#         DOCKER_IMAGE_PULLS.labels(organization=organization, image=image_name).set(pull_count)

# if __name__ == '__main__':
#     # Start up the server to expose the metrics
#     start_http_server(2113)

#     # Add the initial update of metrics
#     update_prometheus_metrics()

#     while True:
#         # Update Prometheus metrics
#         update_prometheus_metrics()

#         # Sleep for 5 minutes before fetching again (to match the requirement)
#         time.sleep(300)


# import os
# import sys
# import time
# import requests
# from prometheus_client import start_http_server, Gauge
# from dotenv import load_dotenv
# # Load environment variables from .env file
# load_dotenv()

# # Environment variables
# DOCKERHUB_ORGANIZATION = os.getenv('DOCKERHUB_ORGANIZATION')

# def fetch_docker_image_pulls(organization):
#     """
#     Fetch Docker image pulls from DockerHub API.
#     Returns a list of image pulls.
#     """
#     try:
#         url = f"https://hub.docker.com/v2/repositories/{organization}/?page_size=25&page=1"
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for non-200 status codes
#         data = response.json()
#         return data.get('results', [])
#     except requests.exceptions.RequestException as err:
#         print(f"Error fetching Docker image pulls: {err}")
#         return []

# DOCKER_IMAGE_PULLS = Gauge('docker_image_pulls', 'The total number of Docker image pulls', ['organization', 'image'])

# def update_prometheus_metrics():
#     """
#     Update Prometheus metrics with Docker image pull counts.
#     """
#     image_pulls = fetch_docker_image_pulls(DOCKERHUB_ORGANIZATION)
#     for image_data in image_pulls:
#         image_name = image_data.get('name', '')
#         pull_count = image_data.get('pull_count', 0)
#         DOCKER_IMAGE_PULLS.labels(organization=DOCKERHUB_ORGANIZATION, image=image_name).set(pull_count)

# if __name__ == '__main__':
#     if not DOCKERHUB_ORGANIZATION:
#         print("DOCKERHUB_ORGANIZATION environment variable is not set.")
#         sys.exit(1)  # Use sys.exit instead of exit

#     start_http_server(2113)
#     update_prometheus_metrics()

#     while True:
#         update_prometheus_metrics()
#         time.sleep(300)



import os
import time
import requests
from prometheus_client import start_http_server, Gauge
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
DOCKERHUB_ORGANIZATION = os.getenv('DOCKERHUB_ORGANIZATION')

# Function to fetch Docker image pulls from DockerHub API
def fetch_docker_image_pulls(organization):
    url = f"https://hub.docker.com/v2/repositories/{organization}/?page_size=25&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('results', [])  # Ensure a default value is returned if 'results' key is not present
    return []  # Remove unnecessary "else" statement and de-indent the code inside it

# Prometheus metrics
DOCKER_IMAGE_PULLS = Gauge('docker_image_pulls', 'The total number of Docker image pulls', ['organization', 'image'])

# Function to update Prometheus metrics
def update_prometheus_metrics():
    # Fetch Docker image pulls
    image_pulls = fetch_docker_image_pulls(DOCKERHUB_ORGANIZATION)

    # Update Prometheus metrics
    for image_data in image_pulls:
        image_name = image_data.get('name', '')  # Use .get() method to handle missing keys gracefully
        pull_count = image_data.get('pull_count', 0)  # Use .get() method to handle missing keys gracefully
        organization = DOCKERHUB_ORGANIZATION

        # Set Prometheus metric
        DOCKER_IMAGE_PULLS.labels(organization=organization, image=image_name).set(pull_count)

if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(2113)

    # Add the initial update of metrics
    update_prometheus_metrics()

    while True:
        # Update Prometheus metrics
        update_prometheus_metrics()

        # Sleep for 5 minutes before fetching again (to match the requirement)
        time.sleep(300)
