dev_local_setup_windows:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	source $HOME/.local/bin/env
	uv tool install pre-commit
