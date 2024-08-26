from flask import Flask, render_template
import random
import string

app = Flask(__name__)

menu_items = [
    {"name": "Smoked Burger Deluxe", "description": "A delicious smoked burger with lots of spices", "price": "$8", "image": "https://static.vecteezy.com/system/resources/thumbnails/028/293/357/small_2x/food-truck-indulgence-pork-burger-topped-with-cheese-paired-with-fries-ai-generated-photo.jpg"},
    {"name": "Fresh Pancakes", "description": "3 freshly made pancakes with honey syrup and an assortment of fruits", "price": "$10", "image": "https://www.foodiesfeed.com/wp-content/uploads/2023/06/pouring-honey-on-pancakes.jpg"},
    {"name": "Fried Chicken", "description": "A crispy bucket of tender chicken that can feed the whole family", "price": "$13", "image": "https://www.jollibeefoods.com/cdn/shop/files/29351737_2152446668377854_356570745477300982_o_2152446668377854.jpg?v=1634843436&width=1080"},
    {"name": "Authentic Philly", "description": "A delicious philly cheesesteak created with authentic ingredients", "price": "$6", "image": "https://static01.nyt.com/images/2024/02/06/multimedia/KD-philly-cheesesteak-mhqc/KD-philly-cheesesteak-mhqc-superJumbo.jpg"},
    {"name": "Shrimp Alfredo", "description": "Tasty shrimp alfredo with the perfect amount of seasoning and freshly caught shrimp", "price": "$11", "image": "https://www.budgetbytes.com/wp-content/uploads/2022/01/Shrimp-Alfredo-Pasta-bowl2-500x500.jpg"},
    {"name": "Italian Beef", "description": "A regular italian beef that comes with a side of fries.", "price": "$9", "image": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Buona_Chicago%27s_Original_Italian_Beef.jpg"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)


@app.route('/order/<item_name>', methods=['POST'])
def order(item_name):
    # Create the delivery people names
    deliverers = ["Ava Williams", "Sophia Johnson", "Isabella Martinez", "Liam Lee", "Ethan Taylor", "Noah Anderson"]

    # Generate a random order ID
    order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Find the food details
    item = next((item for item in menu_items if item['name'] == item_name), None)
    total_cost = item['price'] if item else "N/A"

    # Select a random deliverer
    deliverer = random.choice(deliverers)

    return render_template('order.html', item_name=item_name, order_id=order_id, total_cost=total_cost,
                           deliverer=deliverer)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title="Gallery")

@app.route('/contact')
def contact():
    return render_template('coming_soon.html', title="Contact")


if __name__ == '__main__':
    app.run(debug=True)

