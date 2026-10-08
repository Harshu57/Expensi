@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]
    expense_date = request.form["expense_date"]
    description = request.form["description"]

    cursor = db.cursor()

    sql = """
    INSERT INTO expenses (title, amount, category, expense_date, description)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (title, amount, category, expense_date, description)

    cursor.execute(sql, values)

    db.commit()

    return title