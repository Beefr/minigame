#!bin/bash


kubectl apply -f frontend/persistent-volume.yaml
kubectl apply -f backend/persistent-volume.yaml
kubectl apply -f service.yaml
kubectl apply -f frontend/frontend.yaml
kubectl apply -f anog-backend/anog.yaml
