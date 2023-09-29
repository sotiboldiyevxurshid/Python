# docker-build:
# 	docker build --tag crm-dev:tag .
# docker-run:
# 	docker run -p 8080:8080 --name=golang -d docker.io/library/crm-dev:tag  
# docker-start:
# 	make docker-build && make docker-run


# docker-remove:
# 	docker stop golang
# docker-delete:
# 	docker rm golang  
# docker-stop:
# 	make docker-remove && make docker-delete


