DELETE FROM ordered_products
WHERE id=? OR (order_id=? AND product_id=?);
