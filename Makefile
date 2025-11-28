.PHONY: setup install test run check clean docker-build docker-run

setup:
	@bash setup.sh

install:
	@pip install -r requirements.txt
	@playwright install chromium

test:
	@python test_agent.py

run:
	@python bot.py

check:
	@python check_env.py

clean:
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.log" -delete

docker-build:
	@docker-compose build

docker-run:
	@docker-compose up -d

docker-logs:
	@docker-compose logs -f

docker-stop:
	@docker-compose down

