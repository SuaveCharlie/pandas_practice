dev_local_setup_windows:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	source $HOME/.local/bin/env

dev_build:
	docker build -f ./infrastructure/docker/python/Dockerfile . -t pandas_practice
