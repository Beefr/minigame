#!bin/bash


kubectl delete deploy front-deploy
#kubectl delete deploy anog-deploy


kubectl delete svc mariadb-front
kubectl delete svc nginx
#kubectl delete svc anog


kubectl delete pvc nginx-pvc
kubectl delete pvc bdd-front-pvc
#kubectl delete pvc bdd-back-pvc


kubectl delete pv nginx-volume
kubectl delete pv bdd-front-volume
#kubectl delete pv bdd-back-volume