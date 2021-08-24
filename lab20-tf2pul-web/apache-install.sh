#! /bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo systemctl enable httpd
sudo service httpd start  
echo "<h1>Welcome to Pulumi Training ! AWS Infra created using Pulumi in us-east-1 Regions</h1>" | sudo tee /var/www/html/index.html