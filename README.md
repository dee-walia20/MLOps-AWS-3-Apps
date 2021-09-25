# MLOps-AWS-3-Apps
### Step-1 Create AWS VM Instance
![AWS VM Instance](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/1.png) 
### Step-2 Open MobaXterm and connect to AWS Instance via SSH
![SSH connect](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/2.jpg)
![MobaXterm](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/4.png)
### Step-3 Add the Security groups Inbound rules (port 80, 8000 etc)
![Inbound Rules](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/3.jpg)
### Step-4 Install the necessary python libraries and package managers
``` bash
sudo apt install update
sudo apt update
sudo apt-get update
sudo apt install python3-pip
pip3 install flask
sudo apt install unzip
pip3 install numpy
pip3 install scikit-learn
sudo apt-get install gunicorn3
sudo apt-get install nginx
pip3 install tensorflow==2.0.0
```
#### Note- Run main.py inside Image_Classification directory to save the Tensorflow DL model in .h5 format

### Step-5 Create Gunicorn Socket file for each Web appication
Create the following three Service files inside **cd /etc/systemd/system/** directory with .service extension
``` bash
[Unit]
Description=Flaskapp Gunicorn Service
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/CO2_emission
ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:flaskapp.sock -m 007 app:app
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target

```
``` bash
[Unit]
Description=DL Flaskapp Gunicorn Service
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Image_Classification
ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:dlapp.sock -m 007 app:app
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target

```
``` bash
[User]
Description= Python Calculator app
After=network.target

[Service]
User=Ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/calculator
ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:pyapp.sock -m 007 app:app
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target

```
### Step-6 Reload the Daemon and Restart the service created in previous step
``` bash
sudo systemctl daemon-reload
sudo systemctl enable [service_name.service]
sudo systemctl restart [service_name.service]
```
### Step-7 Create Nginx file & restart the Nginx service
Create a new Nginx file inside **  cd /etc/nginx/sites-enabled/** directory
``` bash
server {
       listen 80;

       server_name 18.216.131.99;

       location / {
               proxy_pass http://unix:/home/ubuntu/CO2_emission/flaskapp.sock;
       }
}

server {
       listen 8080;

       server_name 18.216.131.99;

       location / {
               proxy_pass http://unix:/home/ubuntu/Image_Classification/dlapp.sock;
       }
}

server {
       listen 8050;

       server_name 18.216.131.99;

       location / {
               proxy_pass http://unix:/home/ubuntu/calculator/pycal.sock;
       }
}

server {
       listen 8051;

       server_name 18.216.131.99;

       location / {

       }
}

```
Run the command to restart Nginx service
``` bash
sudo service nginx restart
```
### Step-8 Launch your Web browser and got to the Public IP provided by AWS Instance
By Default port 80 is launched when launching via IP Address.
* **Port-80** ML App
* **Port-8080** DL App
* **Port-8050** Python App
* **Port-8051** Nginx default message
![ML App](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/5.png)
![DL App](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/6.png)
![Python App](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/7.png)
![Nginx default message](https://github.com/dee-walia20/MLOps-AWS-3-Apps/blob/master/images/8.png)

