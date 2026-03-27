from flask import Blueprint, jsonify, request
import json
from validators import validate_product_data

product_bp = Blueprint("product_api", __name__)

def read_products():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def write_products(data):
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

@product_bp.route("/products", methods=["GET"])
def get_products():
    products = read_products()
    search_name = request.args.get("name")

    if search_name:
        filtered_products = [p for p in products if search_name.lower() in p["name"].lower()]
        return jsonify(filtered_products)
    
    return jsonify(products)

@product_bp.route("/product/<int:id>", methods=["GET"])
def get_product_by_id(id):
    products = read_products()

    for p in products:
        if p["id"] == id:
            return jsonify(p)
    
    return jsonify({"message": "Không tìm thấy sản phẩm"}), 404

@product_bp.route("/products", methods=["POST"])
def add_product():
    products = read_products()

    data = request.get_json()
    
    error_message = validate_product_data(data, is_update=False)
    if error_message:
        return jsonify({"message": error_message}), 400
    
    new_id = max(p["id"] for p in products) + 1 if len(products) > 0 else 1

    new_product = {
        "id": new_id,
        "name": data.get("name"),
        "price": data.get("price")
    }
    
    products.append(new_product)
    write_products(products)
    
    return jsonify({"message": "Thêm sản phẩm thành công!", "product": new_product}), 201

@product_bp.route("/product/<int:id>", methods=["PUT", "PATCH"])
def update_product(id):
    products = read_products()
    
    product_index = None
    for i, p in enumerate(products):
        if p["id"] == id:
            product_index = i
            break
            
    if product_index is None:
        return jsonify({"message": f"Không tìm thấy sản phẩm với ID {id}!"}), 404
        
    data = request.get_json()
    error_message = validate_product_data(data, is_update=True)
    if error_message:
        return jsonify({"message": error_message}), 400
        
    if "name" in data:
        products[product_index]["name"] = data["name"]
    if "price" in data:
        products[product_index]["price"] = data["price"]
        
    write_products(products)
    
    return jsonify({
        "message": "Cập nhật sản phẩm thành công!", 
        "product": products[product_index]
    }), 200

@product_bp.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    products = read_products()
    
    new_products = [p for p in products if p["id"] != id]
    
    if len(new_products) == len(products):
        return jsonify({"message": f"Không tìm thấy sản phẩm với ID {id} để xóa!"}), 404
        
    write_products(new_products)
    
    return jsonify({"message": f"Đã xóa sản phẩm có ID {id} thành công!"}), 200