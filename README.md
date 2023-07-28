# Docker ETL Application

This repository contains a Docker-based ETL application. Follow the steps below to clone the repository, start the Docker app, trigger the ETL process, and then query the database.

## Prerequisites

- Docker: Make sure you have Docker installed on your machine. If not, you can download it [here](https://www.docker.com/products/docker-desktop).

- Git: Git is required to clone the repository. If not already installed, you can download it [here](https://git-scm.com/downloads).

- Python 3: Make sure you have Python 3 installed on your machine to run the database query script. You can download Python 3 [here](https://www.python.org/downloads/).

## Getting Started

1. **Clone the Git Repository**
    Open a terminal and run the following command to clone the repository:
    ```
    git clone <repository_url>
    ```
    Replace `<repository_url>` with the URL of the Git repository.

2. **Start the Docker App**
    Navigate to the cloned repository's directory:
    ```
    cd <directory_name>
    ```
    Replace `<directory_name>` with the name of the directory where the repository was cloned.
    Run the following command to start the Docker app:
    ```
    ./scripts/start_services.sh
    ```

3. **Trigger the ETL Process**
    Run the following command to trigger the ETL process:
    ```
    ./scripts/trigger_etl.sh
    ```

4. **Query the Database**
    Run the following command to query the database:
    ```
    python3 ./scripts/query_db.py
    ```


## Conclusion
You should now have the Docker ETL application up and running on your machine. The ETL process should be triggered and you should be able to query the database using the provided script.
