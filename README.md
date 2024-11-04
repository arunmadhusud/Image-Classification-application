# Image Classification Application

This is a simple image classification application using the ResNet18 model. This mini-project aims to understand how to deploy a computer vision model using **FastAPI**, **Docker**, and **AWS ECS**.

## Project Checkpoints

1. **Model Development**: Utilized the pre-trained ResNet18 model from the torchvision library.
2. **Application Development**: Developed the application using FastAPI.
3. **Model Containerization**: Containerized the FastAPI application using Docker.
4. **Model Deployment using AWS ECS**: Deployed the FastAPI application on AWS ECS Fargate.

# Instructions to run the application

1. Clone the repository
2. Build the Docker image using the following command:
```bash
docker build -t image-classification-app -f Dockerfile.model .
```
3. You can see the image using the following command:
```bash
docker images
```
4. Run the Docker container using the following command:
```bash
docker run -d -p 80:80 image-classification-app
```
5. You can see the running container using the following command:
```bash
docker ps
```
6. Open the browser and go to the following URL. You can upload an image at predict endpoint and get the prediction.
```bash
http://localhost/docs
```
7. To stop the running container, use the following command:
```bash
docker stop <container_id>
```
8. To remove the container, use the following command:
```bash
docker rm <container_id>
```
9. if you are not able to remove the container, use the following command to kill the process and remove the container (using steps 7 and 8):
```bash
ps aux | grep <container_id> | grep -v grep | awk '{print $1, $2}' 
sudo kill -9 <pid>
```
10. To remove the image, use the following command:
```bash
docker rmi <image_id>
```

# AWS ECS Deployment
To understand how to deploy the FastAPI application on AWS ECS Fargate, following youtube tutorial from IAAS Academy is a good source:
- [AWS Fargate Tutorial - AWS Container Tutorial](https://www.youtube.com/watch?v=C6v1GVHfOow)
<!-- AWS Fargate Tutorial - AWS Container Tutorial(https://www.youtube.com/watch?v=C6v1GVHfOow) -->






