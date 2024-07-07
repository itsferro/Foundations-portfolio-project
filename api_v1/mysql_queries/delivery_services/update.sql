UPDATE delivery_services
SET
	delivery_service_name=%(delivery_service_name)s,
	description=%(description)s,
	note=%(note)s
WHERE id=%(id)s;