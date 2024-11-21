# ecommerce-lab 
<!-- Create virtual env named ecom -->

```shell
python -m venv ecom
```

<!-- Activate ecom macos-->
```shell
$source ecom/bin/activate
(ecom) bihan@Bihans-MacBook-Pro ecommerce-lab %
```

<!-- Deactive ecom -->
deactivate

<!-- Install requirements -->
pip install -r requirements.txt

<!-- Check installation -->
pip show gunicorn 
pip show flask


<!-- Run from terminal -->
```shell
$ gunicorn --bind 0.0.0.0:5001 market:app
```

<!-- Run from terminal with reload -->
```shell
$ gunicorn --reload --bind 0.0.0.0:5001 market:app
```

<!-- Simply run with python -->
```shell
$ python market.py # 
```

$ gunicorn --workers 9 --threads 2 --bind 0.0.0.0:5001 market:app
$ ps aux | grep gunicorn



<!-- Check Docker -->
```shell
$docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
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


# References
1. https://www.youtube.com/watch?v=Qr4QMBUPxWo&t=555s
2. https://github.com/jimdevops19/codesnippets/tree/main/Flask%20Full%20Series

