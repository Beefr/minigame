
FROM nginxflask-frontend:latest

WORKDIR /app
COPY ./frontend/app /app
COPY ./frontend/nginx.conf /usr/local/nginx/conf

CMD ["python", "/app/main.py"]


