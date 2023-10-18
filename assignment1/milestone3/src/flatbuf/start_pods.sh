echo "Starting all of the pods..."
kubectl apply -f flatbuf-zmq-svr-svc.yml 
kubectl apply -f flatbuf-zmq-svr-deploy.yml 
kubectl apply -f flatbuf-zmq-client-job.yml 
echo "Done!"