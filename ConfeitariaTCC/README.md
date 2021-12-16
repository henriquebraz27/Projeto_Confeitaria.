### Steps
 
* Run `./destroy_mysql.sh` to remove any container related to MySql and PhpMyAdmin
* Run `./run_mysql.sh` to execute all the needed containers for MySql
* Run `./run.sh` to execute the application
* Access http://localhost:8081 with user = `root` and password = `mypass123`
* Create the database `confeitaria`
* Execute the SQL commands in `confeitaria.sql` into `confeitaria` database in PhpMyAdmin