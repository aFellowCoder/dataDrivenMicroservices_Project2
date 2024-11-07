Data-Driven Microservices Project - Kubernetes Deployment

Overview

This project is an extension of a microservices-based system initially developed as part of Assignment 1 for the Data-driven Microservices module. The project simulates real-time data streaming, processes data with gRPC, and displays analytics on a web page. For Assignment 2, the project has been migrated to run within a Kubernetes (k3s) environment, scaled to handle multiple data sources, and enhanced with testing, monitoring, and a serverless function.

Project Structure

The repository includes the following core components:

	•	Microservice 1: Data Collection - Reads and streams data from multiple sources via gRPC.
	•	Microservice 2: Data Analytics - Processes incoming data, computes metrics, and feeds the results.
	•	Microservice 3: Data Visualization - Hosts a Flask-based dashboard that presents the metrics.
	•	Deployment and Orchestration - Kubernetes YAML files for deploying, scaling, and managing services.

Features Added in Assignment 2

1. Kubernetes Deployment

	•	The entire system is containerized and managed in a Kubernetes (k3s) environment.
	•	Pods are scaled appropriately based on the service needs (e.g., more replicas for data analytics).
	•	The deployment includes multiple data sources processed in parallel to ensure a robust and flexible analysis system.

2. Multiple Data Sources

	•	The architecture has been adapted to handle more than one data source simultaneously.
	•	Data can be passed as a parameter to the data extraction microservices, or separate microservices can be used for different formats.

3. Testing

	•	A functional or non-functional test has been created to validate the application’s performance and accuracy.
	•	The test details include:
	•	Explanation of the type of test implemented (e.g., load test with Gatling, API test with Postman, etc.).
	•	A guide on how to run the test, along with any necessary scripts.
	•	Screenshots showcasing the test in action.

4. Monitoring

	•	A monitoring solution is implemented to track the health and performance of the application.
	•	Visualized metrics (e.g., using tools like Prometheus and Grafana) are shown through charts and dashboards.
	•	Documentation includes the rationale behind the chosen monitoring tools and their configuration details.

5. Serverless Function

	•	A serverless function developed using Kubeless adds further utility to the project. This function is designed to enhance or support the main application and runs from the command line per the Kubeless quick-start guide.
	•	Explanation of where this function would fit within the application architecture, with details on its input/output and how it improves functionality.
