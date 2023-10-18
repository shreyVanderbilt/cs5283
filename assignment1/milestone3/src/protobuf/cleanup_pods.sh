echo "Cleaning deployment..."
kubectl delete job protobuf-grpc-client -n protobuf-grpc-local
kubectl delete deployment protobuf-grpc-svr-deploy -n protobuf-grpc-local
kubectl delete service protobuf-grpc-svr-svc -n protobuf-grpc-local
echo "Done!"