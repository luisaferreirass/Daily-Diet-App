from flask import Flask, request, jsonify
from meal import Meal

app = Flask(__name__)

meals = []
mealsId = 1


@app.route('/meals', methods= ['POST'])
def create_meal():
    global mealsId
    data = request.get_json()
    new_meal = Meal(id= mealsId, name= data.get("name"), description= data.get("description"), date= data.get("date"), hour= data.get("hour"), inTheDiet= data.get("inTheDiet"))
    mealsId += 1
    meals.append(new_meal)
    return jsonify({"message": "refeição adicionada com sucesso"})

@app.route('/meals', methods=['GET'])
def get_meals():
    all_meals = []
    for meal in meals:
        all_meals.append(meal.to_dict())
    
    output = {
        "Meals": all_meals,
        "total meals": len(all_meals)
    }

    return jsonify(output)

@app.route('/meals/<int:id>', methods=['GET'])
def get_meal(id):
    for meal in meals:
        if meal.id == id:
            return jsonify(meal.to_dict())
            break
    
    return jsonify({"message": "Não foi possível encontrar essa refeição"}), 404

@app.route('/meals/<int:id>', methods=['PUT'])
def update_meal(id):
    meal = None
    for m in meals:
        if m.id == id:
            meal = m
            break
    
    if meal == None:
        return jsonify({"message": "Não foi possível encontar essa refeição"}), 404
    
    data = request.get_json()

    meal.name = data["name"]
    meal.description = data["description"]
    meal.date = data["date"]
    meal.hour = data["hour"]
    meal.inTheDiet = data["inTheDiet"]

    return jsonify({"message": "Refeição atualizada com sucesso"})

@app.route('/meals/<int:id>', methods=['DELETE'])
def delete_meal(id):
    meal = None
    for m in meals:
        if m.id == id:
            meal = m
            break
    
    if meal == None:
        return jsonify({"message": "Não foi possível encontar essa refeição"}), 404
    
    meals.remove(meal)

    return jsonify({"message": "Refeição deletada com sucesso"})
            

if __name__ == '__main__':
    app.run(debug=True)