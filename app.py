from flask import Flask, render_template, request, redirect, url_for
from models import db, SeasonalFlavor, Ingredient, Suggestion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_house.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables

@app.route('/')
def index():
    seasonal_flavors = SeasonalFlavor.query.all()
    return render_template('index.html', flavors=seasonal_flavors)

@app.route('/add_flavor', methods=['POST'])
def add_flavor():
    name = request.form['name']
    description = request.form['description']
    new_flavor = SeasonalFlavor(name=name, description=description)
    db.session.add(new_flavor)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_flavor/<int:id>', methods=['GET', 'POST'])
def update_flavor(id):
    flavor = SeasonalFlavor.query.get_or_404(id)
    if request.method == 'POST':
        flavor.name = request.form['name']
        flavor.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_flavor.html', flavor=flavor)

@app.route('/delete_flavor/<int:id>', methods=['POST'])
def delete_flavor(id):
    flavor = SeasonalFlavor.query.get_or_404(id)
    db.session.delete(flavor)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/inventory')
def inventory():
    ingredients = Ingredient.query.all()
    return render_template('inventory.html', ingredients=ingredients)

@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    name = request.form['name']
    quantity = request.form['quantity']
    new_ingredient = Ingredient(name=name, quantity=quantity)
    db.session.add(new_ingredient)
    db.session.commit()
    return redirect(url_for('inventory'))

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        flavor_suggestion = request.form['flavor_suggestion']
        allergy_concern = request.form['allergy_concern']
        new_suggestion = Suggestion(customer_name=customer_name, flavor_suggestion=flavor_suggestion, allergy_concern=allergy_concern)
        db.session.add(new_suggestion)
        db.session.commit()
        return redirect(url_for('suggestions'))
    
    suggestions = Suggestion.query.all()
    return render_template('suggestions.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
