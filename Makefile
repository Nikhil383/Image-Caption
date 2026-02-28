.PHONY: install run test clean docker-build docker-run

install:
	uv sync

run:
	uv run python -m image_caption.app

test:
	uv run pytest tests/

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf src/image_caption/__pycache__
	rm -rf tests/__pycache__

docker-build:
	docker build -t image-caption .

docker-run:
	docker run -p 5000:10000 --env-file .env image-caption
