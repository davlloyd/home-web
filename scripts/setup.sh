
# Create MySQL Instance
docker run -d -v mysqldata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=test -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3306:3306 --name mysql1 mysql

# Create Jenkins instance
docker run --name jenkins -p 8080:8080 -p 50000:50000 -v jenkinsdata:/var/jenkins_home jenkins
