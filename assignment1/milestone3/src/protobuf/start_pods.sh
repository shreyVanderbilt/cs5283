echo "Starting all of the pods..."
kubectl apply -f protobuf-grpc-svr-svc.yml 
kubectl apply -f protobuf-grpc-svr-deploy.yml 
kubectl apply -f protobuf-grpc-client-job.yml 
echo "Done!"