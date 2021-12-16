docker pull mysql:latest
docker run -it --name my-own-mysql  -p 3306:3306  -e MYSQL_ROOT_PASSWORD=mypass123 -d mysql:latest
docker pull phpmyadmin/phpmyadmin:latest
docker run --name my-own-phpmyadmin -d --link my-own-mysql:db -p 8081:80 phpmyadmin/phpmyadmin

echo 'Access http://localhost:8081 with password = mypass123'