# Webstack Monitoring Project

## Overview

In the world of technology, monitoring our software systems is crucial for understanding and improving their performance. This project focuses on implementing a monitoring tool for both application and server aspects of a web stack.

## Servers

| Name             | Username | IP            | State |
|------------------|----------|---------------|-------|
| 269788-web-01    |          | [web-01 IP]   |       |
| 269788-web-02    |          | [web-02 IP]   |       |
| 269788-lb-01     |          | [lb-01 IP]    |       |

## Tasks

### 0. Sign up for Datadog and install datadog-agent

- Sign up for a Datadog account at [Datadog](https://www.datadoghq.com/).
- Use the US1 region.
- Install the Datadog agent on web-01.
- Create an application key.

### 1. Validate Datadog Setup

- Ensure that web-01 is visible in Datadog under the hostname XX-web-01.
- Validate visibility using the Datadog API.

### Additional Notes

- Use the Datadog API Key and Application Key for authentication.
- Update the Intranet user profile with the keys.
- Check the GitHub repository `alx-system_engineering-devops` and directory `0x18-webstack_monitoring` for project files.

## Datadog API Validation

To validate web-01 visibility, use the following command:

```bash
curl -X GET "https://api.datadoghq.com/api/v1/hosts" -H "Content-Type: application/json" -H "DD-API-KEY: YOUR_API_KEY" -H "DD-APPLICATION-KEY: YOUR_APPLICATION_KEY"

