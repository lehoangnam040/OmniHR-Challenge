INSERT INTO company (id, "name") VALUES (generate_series(1, 10),  'company ' || md5(random()::text));   
INSERT INTO "position" (id, "name") VALUES (generate_series(1, 10),  'position ' || md5(random()::text));
INSERT INTO "location"  (id, "name") VALUES (generate_series(1, 10),  'location ' || md5(random()::text));
INSERT INTO department (id, "name", company_id) VALUES (generate_series(1, 30),  'department ' || md5(random()::text), floor(random() * 10));

INSERT INTO employee (id, first_name, last_name, email, phone_number, status, department_id, position_id, location_id)
VALUES(
	generate_series(1, 10000000),
	substr(md5(random()::text), 0, 25),
	substr(md5(random()::text), 0, 25),
	CASE WHEN random() < 0.5 THEN substr(md5(random()::text), 0, 25) ELSE NULL END,
	CASE WHEN random() < 0.5 THEN substr(md5(random()::text), 0, 25) ELSE NULL END,
	('{ACTIVE,NOT_STARTED,TERMINATED}'::text[])[ceil(random()*3)],
	floor(random() * 30),
	floor(random() * 10),
	floor(random() * 10)
);