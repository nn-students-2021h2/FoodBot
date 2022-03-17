import pymysql


def add_learned_dish_note(
    learned_dish_dish: str,
    learned_dish_average_calories: float,
    learned_dish_average_proteins: float,
    learned_dish_average_fats: float,
    learned_dish_average_carbs: float,
) -> None:
    """
    Adds one dish entry to learned_dish database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )
    cursor = con.cursor()
    sql = (
        f"INSERT INTO learned_dish (learned_dish_dish, learned_dish_average_calories, learned_dish_average_proteins,"
        f" learned_dish_average_fats, learned_dish_average_carbs) "
        f"VALUES ('{learned_dish_dish}', {learned_dish_average_calories}, {learned_dish_average_proteins},"
        f" {learned_dish_average_fats}, {learned_dish_average_carbs})"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print("learned_dish added")
    except pymysql.Error as e:
        con.rollback()
        print(f"error of learned_dish adding error pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def delete_learned_dish_note(learned_dish_dish: str) -> None:
    """
    Deletes one dish entry in learned_dish database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"DELETE FROM learned_dish WHERE learned_dish_dish='{learned_dish_dish}'"
    try:
        cursor.execute(sql)
        con.commit()
        print("learned_dish_note deleted")
    except pymysql.Error as e:
        con.rollback()
        print(f"error of learned_dish_note deleting error pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def get_learned_dish_note(learned_dish_dish: str) -> dict | None:
    """
    Returns all data about a dish from learned_dish database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"SELECT * FROM learned_dish WHERE learned_dish_dish='{learned_dish_dish}'"

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = dict(
            learned_dish_dish=database_result[0][0],
            learned_dish_average_calories=database_result[0][1],
            learned_dish_average_proteins=database_result[0][2],
            learned_dish_average_fats=database_result[0][3],
            learned_dish_average_carbs=database_result[0][4],
        ) if database_result != () else None
        print("record received")
    except pymysql.Error as e:
        print(f"error of record receiving error pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


if __name__ == "__main__":
    print(get_learned_dish_note("jkk"))
