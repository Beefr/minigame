#!/bin/bash


kubectl delete deploy front-deploy
kubectl delete deploy anog-deploy


kubectl delete svc frontend
kubectl delete svc mariadb-front
kubectl delete svc nginx
kubectl delete svc mariadb-anog
kubectl delete svc anog


#kubectl delete pvc nginx-pvc
#kubectl delete pvc bdd-front-pvc
#kubectl delete pvc bdd-anog-pvc
#kubectl delete pvc anog-pvc


#kubectl delete pv nginx-volume
#kubectl delete pv bdd-front-volume
#kubectl delete pv bdd-anog-volume
#kubectl delete pv anog-volume