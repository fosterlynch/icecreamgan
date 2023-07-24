start:
	docker run -it --network=host \
	--name musicgan \
	musicgan \
	bash
stop:
	docker container stop musicgan
	docker container rm musicgan
create-container:
	docker build  --network=host --file=dockerfile --tag musicgan .

restart:
	docker container stop musicgan
	docker container rm musicgan
	docker build  --network=host --file=dockerfile --tag musicgan .
	docker run -it --network=host \
	--name musicgan \
	musicgan \
	bash