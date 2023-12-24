CREATE TABLE company (
    id bigint primary key,
    "name" varchar(128) not null
)

CREATE TABLE department (
    id bigint primary key,
    company_id bigint not null,
    "name" varchar(128) not null
)

CREATE TABLE position (
    id bigint primary key,
    "name" varchar(128) not null
)

CREATE TABLE location (
    id bigint primary key,
    "name" varchar(128) not null
)

CREATE TABLE employee (
    id bigint primary key,
    first_name varchar(128) not null,
    last_name varchar(128) not null,
    email varchar(128) null,
    phone_number varchar(64) null,
    "status" varchar(64) not null,  -- enum: ACTIVE, NOT_STARTED, TERMINATED
    department_id bigint null,
    position_id bigint null,
    location_id bigint null
)