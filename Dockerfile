WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin

RUN uv init 