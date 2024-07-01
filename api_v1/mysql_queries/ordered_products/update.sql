UPDATE ordered_products
SET ordered_quantity=?, note=?
WHERE id=? OR (order_id=? AND product_id=?);
