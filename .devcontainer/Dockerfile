FROM jhale1805/python-poetry:1.1.13-py3.8-slim
ENV PROJECT_ROOT_DIR=/workspaces

RUN apt update \
    && apt install git --assume-yes --no-install-recommends

WORKDIR $PROJECT_ROOT_DIR
ENV PATH="$PROJECT_ROOT_DIR/.venv/bin:$PATH"

COPY poetry.lock pyproject.toml ./
RUN poetry install
