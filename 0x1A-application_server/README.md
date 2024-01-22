# Application Server Configuration

## Overview

This project involves setting up an application server for an Airbnb clone, using Nginx as a reverse proxy. The server configuration includes serving dynamic content using Gunicorn and handling different routes for the application.

## Project Structure

- **0x1A-application_server/**
  - **0-set_up_development/**: Development setup for Python and Flask application.
  - **1-set_up_production/**: Production setup with Gunicorn for serving dynamic content.
  - **2-serve_a_page_with_nginx/**: Nginx configuration to serve a page from the Flask application.
  - **3-add_a_route_with_query_parameters/**: Nginx configuration to proxy requests to a Gunicorn instance with a route that includes query parameters.
  - **4-serve_your_API/**: Setup for serving a RESTful API using Gunicorn and Nginx.
  - **5-serve_your_AirBnB_clone/**: Configuration to serve the web dynamic content of the Airbnb clone using Gunicorn and Nginx.

## Requirements

- All Python-related tasks should use `python3`.
- Config files and Bash scripts must be commented.
- Bash scripts should pass Shellcheck without any error.
- Servers should be running Ubuntu 16.04 LTS.
- All files should end with a new line.
- Bash script files must be executable.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without errors.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## Task Details

### 0. Set up development with Python

- Install `net-tools` package.
- Clone the Airbnb clone v2 project.
- Configure Flask application to serve content from the route `/airbnb-onepage/` on port 5000.
- Flask application object must be named `app`.

### 1. Set up production with Gunicorn

- Install Gunicorn and required libraries.
- Configure Gunicorn to serve the same content as in Task 0.
- Flask application object should be named `app`.
- Gunicorn should bind to localhost on port 5000.
- Ensure nothing is listening on port 6000.

### 2. Serve a page with Nginx

- Configure Nginx to serve content from the route `/airbnb-onepage/`.
- Nginx should proxy requests to the process listening on port 5000.

### 3. Add a route with query parameters

- Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance listening on port 5001.

### 4. Serve your API

- Clone the Airbnb clone v3 project.
- Setup Nginx to route `/api/` to a Gunicorn instance listening on port 5002.

### 5. Serve your AirBnB clone

- Clone the Airbnb clone v4 project.
- Configure Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Setup Nginx to route `/` to the Gunicorn instance and serve static assets from `web_dynamic/static/`.
- Update the `web_dynamic/static/scripts/2-hbnb.js` to the correct IP.

## Testing

For each task, follow the provided examples to test your configurations and ensure everything works as expected.

Feel free to reach out if you have any questions or encounter issues.

