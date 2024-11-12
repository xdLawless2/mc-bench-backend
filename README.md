# Development

This is known to work with python 3.12.7

# Pre-Requisites

1. python installed. We recommend [pyenv]("https://github.com/pyenv/pyenv").

```shell
pyenv install 3.12.7
```

2. A virtual environment created and activated somewhere

    via pyenv
    ```shell
   pyenv virtualenv 3.12.7 mc-bench-backend
   pyenv activate mc-bench-backend
   ```
   
    via vanilla venv

    ```shell
    pyenv shell 3.12.7
    python -m venv .venv
    source .venv/bin/activate
    ```
   
Any other mechanism should work as well

3. editably install the project
    
    ```pip install -e .[dev,api,worker]
    ```

# Services run via docker

The following command will start all the services up

    docker-compose up -d --build

See the docker-compose.yml file for what services are started up and which ports they are listening on

`TODO: figure out hot reloading in the containers`

# Tail the logs

docker-compose logs -f

# Formatting/Linting

Run the ruff formatter
```shell
make fmt
````

Run the ruff checker
```shell
make check
```

Run the ruff checker with --fix option
```shell
make check-fix
```
