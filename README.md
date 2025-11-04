In this project, we build a simple web application using Python Flask (app.py).
✔ The project demonstrates CI/CD automation using Jenkins, GitHub, and Docker.
✔ The source code of the application is stored in a GitHub repository.
✔ Whenever we push or commit changes to GitHub, Jenkins detects it (via Git webhook) and automatically starts a pipeline job.
✔ The Jenkins pipeline does the following:

Pulls latest code from GitHub

Builds a Docker image using the code

Tags the image using DockerHubUsername/flaskapp:$BUILD_NUMBER (example: mkappera/flaskapp:5)

Optionally tags latest image as :latest

Pushes the built image to Docker Hub

Deploys the new container on the server (EC2) and exposes it on port 5001
✔ Each successful build in Jenkins = new version of image is created and stored in Docker with that Jenkins $BUILD_NUMBER.
