# GCP-ConfigDeployAppOnNetworkLB
## Configuration and Deployment of application based on Network Load Balancer

•	A Compute Engine instance hosts a MySQL database for the application.

•	An instance template for frontend instances, uses a Docker image for the Node.js application.

•	A managed instance group, uses the instance template to create two frontend instances.

•	An autoscaler, starts or stops additional frontend instances based on incoming traffic.

•	A health check, checks whether the frontend instances are available to do work.

•	A network load balancer with a forwarding rule.

•	A target pool for the managed instance group.
