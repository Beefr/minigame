#!bin/bash


kubectl apply -f frontend/persistent-volume.yaml
kubectl apply -f anog-backend/persistent-volume.yaml

kubectl apply -f frontend/service-front.yaml
kubectl apply -f anog-backend/service-back.yaml

kubectl apply -f frontend/frontend.yaml
kubectl apply -f anog-backend/application.yaml
