UPDATE orders 
SET
	customer_name=?,
	customer_phone_1=?,
	customer_phone_2=?,
	customer_main_address_id=?,
	customer_address_1=?,
	customer_address_2=?,
	preferred_delivery_day=?,
	preferred_delivery_time=?,
	order_type=?,
	is_it_pickup=?,
	products_total_price=?,
	delivery_fee=?,
	discount_amount=?,
	total=?,
	delivery_service_id=?,
	note=?
WHERE id=?;
