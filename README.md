this repo is a clone of https://github.com/miguelgrinberg/flasky

# Docker
Using Docker, I experimented with both plain Docker and Docker-Compose.

In order to build the container, I use either of the commands below. 
The first command allows me to name the container whereas docker-compose build remains nameless but much easier to memorize.
sudo docker build -t ece444-lab4:latest .
sudo docker-compose build

![Image of the Flask App](https://raw.githubusercontent.com/Hangukkid/ECE444-F2020-Lab3/lab4_Microservice_Experiment/build_docker.png)\

In order to run my container, I use either of the two commands. They DO NOT do the same thing, the first one will 
run my container in detached mode, allowing me to use my terminal. The second command reads docker-compose.yml to run the container.
sudo docker run -d -p 5000:5000 ece444-lab4
sudo docker-compose up

![Image of the Flask App](https://raw.githubusercontent.com/Hangukkid/ECE444-F2020-Lab3/lab4_Microservice_Experiment/run_headless_and_display.png)\
In this picture, I show the detatched run of the container since it's easier to show as well as using the command "sudo docker ps -a" to\
display the running containers.

The final image is of the flask app that is run in the contianer.
![Image of the Flask App](https://raw.githubusercontent.com/Hangukkid/ECE444-F2020-Lab3/lab4_Microservice_Experiment/flask_screenshot.png)\

# Dockers vs VMs
The main difference is that VMs contain their own OS (operating system) kernel. Processes that run in Docker Containers interact directly with the OS kernel of the host running docker. The other differences that make Docker Containers unique to VMs are that containers are more lightweight, require less memory space and less startup time.
