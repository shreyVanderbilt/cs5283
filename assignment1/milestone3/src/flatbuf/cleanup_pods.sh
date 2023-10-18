echo "Cleaning deployment..."
kubectl delete job flatbuf-zmq-client -n flatbuf-zmq-local
kubectl delete deployment flatbuf-zmq-svr-deploy -n flatbuf-zmq-local
kubectl delete service flatbuf-zmq-svr-svc -n flatbuf-zmq-local
echo "Done!"