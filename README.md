this repo is a clone of https://github.com/miguelgrinberg/flasky

sudo docker build -t ece444-lab4:latest .
sudo docker-compose build

sudo docker run -d -p 5000:5000 ece444-lab4
sudo docker-compose up
