#!bin/bash


minikube start --driver=docker
#kubectl create namespace microservices
kubectl config set-context $(kubectl config current-context) --namespace=microservices



