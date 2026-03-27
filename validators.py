def validate_product_data(data, is_update=False):
    if not data:
        return "Dữ liệu không hợp lệ hoặc trống!"

    if not is_update:
        if 'name' not in data or 'price' not in data:
            return "Dữ liệu không hợp lệ, cần cung cấp đầy đủ 'name' và 'price'!"

    if 'name' in data:
        name = str(data['name']).strip()
        if not name:
            return "Tên sản phẩm không được để trống!"

    if 'price' in data:
        price = data['price']
        if not isinstance(price, (int, float)):
            return "Giá sản phẩm phải là một số!"
        
        if price < 0:
            return "Giá sản phẩm không được là số âm!"

    return None