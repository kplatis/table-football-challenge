# Table Football Challenge

## How to run this project

This project can run using Docker and Docker Compose

### Prerequisites

- Install [Docker](https://www.docker.com/get-started/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

### Usage

1. Clone this repository

```bash
   git clone https://github.com/kplatis/table-football-challenge
```

2. Build and start the services using Docker Compose on the root of the project

```bash
docker-compose up --build
```

This command will build the Docker images for both services and start the containers.

3. Access the backend application at `http://localhost:8000` and the frontend application at `http://localhost:3000` in your web browser. The OpenAPI documentation of the backend can be found in `http://localhost:8000/docs`
