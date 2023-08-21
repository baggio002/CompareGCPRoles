drop database gcp_permissions_roles;
create database gcp_permissions_roles;
use gcp_permissions_roles;

-- drop table permissions_roles;
-- drop table gcp_permissions;
-- drop table gcp_roles;

CREATE TABLE gcp_permissions(
    pid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    permission VARCHAR(100)
);

CREATE TABLE gcp_roles(
    rid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    role VARCHAR(100)
);

CREATE TABLE permissions_roles(
    prid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    pid INT,
    rid INT,
    FOREIGN KEY(pid) REFERENCES gcp_permissions(pid),
    FOREIGN KEY(rid) REFERENCES gcp_roles(rid)
)
