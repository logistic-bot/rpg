test:
	@pytest --cov=src --ff tests --durations=2 --cov-report term-missing:skip-covered --testmon -x
	@make style

style:
	@mypy src --strict --show-error-context --pretty
	@./venv/bin/pylint src -f colorized -j 4 --ignore-patterns='test*'
	@flake8 --max-line-length=100 --max-doc-length=100 --show-source --statistics --jobs 4 --doctests src
