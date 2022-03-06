import pymysql


def add_learned_dish_note(
    learned_dish_dish: str,
    learned_dish_average_calories: float,
    learned_dish_average_proteins: float,
    learned_dish_average_fats: float,
    learned_dish_average_carbohydrates: float,
) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )
    cursor = con.cursor()
    sql = (
        f"INSERT INTO learned_dish (learned_dish_dish, learned_dish_average_calories, learned_dish_average_proteins, learned_dish_average_fats, learned_dish_average_carbohydrates) "
        f"VALUES ('{learned_dish_dish}', {learned_dish_average_calories}, {learned_dish_average_proteins}, {learned_dish_average_fats}, {learned_dish_average_carbohydrates})"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print("learned_dish added")
    except:
        con.rollback()
        print("error of learned_dish adding")
    cursor.close()
    con.close()


def delete_learned_dish_note(learned_dish_dish: str) -> None:
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
    except:
        con.rollback()
        print("error of learned_dish_note deleting")
    cursor.close()
    con.close()


def get_learned_dish_note(learned_dish_dish: str) -> dict:
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
            learned_dish_average_carbohydrates=database_result[0][4],
        )
        print("record received")
    except:
        print("error of record receiving")
    cursor.close()
    con.close()

    return result


if __name__ == "__main__":
    delete_learned_dish_note(
        "<built-in method lower of str object at 0x000001AB56086070>"
    )
