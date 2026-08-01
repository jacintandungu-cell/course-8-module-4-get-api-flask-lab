from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Homepage route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200

# GET /products route with optional category filter
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        # Normalize case for comparison
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered), 200
    return jsonify(products), 200

# GET /products/<id> route
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": f"Product with id {id} not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)