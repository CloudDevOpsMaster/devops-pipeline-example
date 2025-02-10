#!/bin/bash
echo "Deploying application..."
kubectl apply -f k8s/deployment.yaml
