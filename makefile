setup-zsh: # setup virtual env and open a zsh shell, add precommit hooks
	make venv && make zsh && pre-commit install
setup-bash: # setup virtual env and open a bash shell, add precommit hooks
	make venv && make bash && pre-commit install
setup-shell: # setup virtual env and open a shell, add precommit hooks
	make venv && make shell && pre-commit install
test: venv # run tests
	set -o allexport; source .env; set +o allexport; python3 -m pytest tests
run-docker: # run via docker image
	docker-compose up
run: # run main.py
	set -o allexport; source .env; set +o allexport; python3 -m src.main
scratch: # run scratch.py
	set -o allexport; source .env; set +o allexport; python3 -m scratch

include nMakefile
