# ecommerce-lab
<!-- Create virtual env named ecom -->
python -m venv ecom 

<!-- Activate ecom -->
source ecom/bin/activate

<!-- Deactive ecom -->
deactivate

<!-- Install requirements -->
pip install -r requirements.txt

``` shell
$docker ps
CONTAINER ID   IMAGE   COMMAND    CREATED    STATUS    PORTS     NAMES
```

<!-- This command removes all stopped containers, unused networks, dangling images, and unused volumes.
Ensure you don't need these resources before executing the command. -->
docker system prune -a --volumes

<!-- Builds docker image -->
docker build -t flask_app_image .

<!-- Run Container -->
docker run -d -p 5001:5001 --name flask_app_container flask_app_image

<!-- Stop Container -->
docker stop flask_app_container

<!-- Logs -->
docker logs -f flask_app_container

<!-- Remove Container -->
docker rm flask_app_container

