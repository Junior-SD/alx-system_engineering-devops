# Web Stack Debugging #4

## Overview

This project involves debugging a web server setup featuring Nginx under pressure using ApacheBench. The initial benchmarking revealed a significant number of failed requests, and the goal is to optimize the stack to handle the load efficiently.

## Task 0: Sky is the limit, let's bring that limit higher

### Description
The initial benchmark showed a high number of failed requests. The Puppet manifest `0-the_sky_is_the_limit_not.pp` addresses this issue by making necessary adjustments to the Nginx configuration.

### Execution
```bash
puppet apply 0-the_sky_is_the_limit_not.pp

