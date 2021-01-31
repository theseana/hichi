# Enter Mysql
LINUX
```
mysql -u poulstar -p
```
# Create Database
```
CREATE DATABASE hichi;
```

# Use Databse
```
USE hichi;
```
# Create Table
PERSON
```
CREATE TABLE person(
    personId INT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    PRIMARY KEY(personId)
);
```
GRADE
```
CREATE TABLE grade(
    gradeId INT NOT NULL AUTO_INCREMENT,
    math VARCHAR(3) NOT NULL,
    history VARCHAR(3) NOT NULL,
    chemistry VARCHAR(3) NOT NULL,
    people INT,
    PRIMARY KEY(gradeId),
    FOREIGN KEY(people) REFERENCES person(personId)
);
```