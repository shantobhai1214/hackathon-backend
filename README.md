# Hackathon backend based on FastAPI, Pydantic, and uv for fast development and shipping optimized feedbacks from previous hackathons (Mistral, OpenAI, Deepmind)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) ![Maintainer](https://img.shields.io/badge/maintainer-@louisbrulenaudet-blue) ![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg) ![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg) ![Package Manager](https://img.shields.io/badge/package%20manager-uv-purple.svg)

In order to run the backend the fastest way possible, you can use the makefile setup and uv for Python dependency management.

If the frontend team needs to run their application separately, the recommended and most secure approach is to clone this repository twice: once for production (e.g., with a `-prod` suffix) and once for development (e.g., with a `-dev` suffix). Keep the production backend on the `main` branch and the development backend on the appropriate development branches. Start the production backend using `make prod`, then share your IP address with the frontend team so they can connect to the backend.

You can get your IP address by running the following command:

```sh
ipconfig getifaddr en0
```

Note: do not forget to disable your firewall or allow the port 8001 in your firewall settings to allow the frontend team to connect to your backend. Make commands are only available in unix-like systems (Linux, macOS). For Windows users, you can use the WSL (Windows Subsystem for Linux) to run these commands.

To ensure smooth development and minimize conflicts, it is recommended to implement each component in its own dedicated router and corresponding business logic files within the `core` directory. This modular approach enables you to test and develop components independently, reducing the risk of interfering with other parts of the application. Organizing your code in this way enhances maintainability, scalability, and clarity, making it easier to merge core features across branches and integrate them into different routers as the project evolves.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose for containerization and deployment.
- [uv](https://github.com/astral-sh/uv) (Python dependency manager)
- [ruff](https://docs.astral.sh/ruff/) (linter/formatter)

In order to run the backend the fastest way possible, you can use the makefile setup and uv for Python dependency management as this:

```sh
make init
make upgrade
make dev
```

Then you can ping the API at [http://127.0.0.1:8000/api/v1/ping](http://127.0.0.1:8000/api/v1/ping).

If you need to install packages such as transformers, you can do so with the following command:

```sh
uv add transformers
```

## Environment Setup

1. Copy `.env.template` to `.env` and adjust variables as needed.

---

## Quick Start

### 1. Initialize the environment

```sh
make init
```

### 2. Start FastAPI server

The backend can be run in two modes: development and production. The development mode is intended for local development with hot-reloading, while the production mode is optimized for performance and stability. Here's how to start the development server:

```sh
make dev
```

- The API will be available at [http://localhost:8000](http://localhost:8000) by default with a ping endpoint at [http://localhost:8000/api/v1/ping](http://localhost:8000/api/v1/ping).

### 2.1 Start production server

Here's how to start the production server:

```sh
make prod
```

- The production server will run on port 8001 by default at [http://0.0.0.0:8001](http://0.0.0.0:8001) with a ping endpoint at [http://0.0.0.0:8001/api/v1/ping](http://0.0.0.0:8001/api/v1/ping).

## Code Quality

- Lint and check code:
  ```sh
  make check
  ```

- Format code:
  ```sh
  make format
  ```
