build-ui:
	cd central-ui && npm run build && cp -r dist/* ../

docker-build:
	docker-compose up -d --build

run-server:
	python app.py

serve-ui:
	cd central-ui && npm run serve