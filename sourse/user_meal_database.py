import pymysql
import datetime


def add_meal_note(
    user_id: int,
    meal_id: int,
    meal_dish: str,
    meal_size: float,
    meal_average_calories: float,
    meal_average_proteins: float,
    meal_average_fats: float,
    meal_average_carbohydrates: float,
    meal_date: str,
    meal_time: str,
) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )
    cursor = con.cursor()
    sql = (
        f"INSERT INTO meal (user_id, meal_id, meal_dish, meal_size, meal_average_calories, meal_average_proteins, meal_average_fats, meal_average_carbohydrates, meal_date, meal_time) VALUES ({user_id},"
        f" {meal_id}, '{meal_dish}', {meal_size}, {meal_average_calories}, {meal_average_proteins}, {meal_average_fats}, {meal_average_carbohydrates}, '{meal_date}', '{meal_time}')"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_note added")
    except:
        con.rollback()
        print("error of meal adding")
    cursor.close()
    con.close()


def delete_all_meal_notes(user_id: int) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"DELETE FROM meal WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("all user's notes deleted")
    except:
        con.rollback()
        print("error of all user's notes deleting")
    cursor.close()
    con.close()


def delete_meal_note(user_id: int, meal_id: int) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"DELETE FROM meal WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("user's note deleted")
    except:
        con.rollback()
        print("error of user's note deleting")
    cursor.close()
    con.close()


def get_number_of_user_meals(user_id: int) -> int:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"SELECT count(*) FROM meal WHERE user_id={user_id}"
    result = -1
    try:
        cursor.execute(sql)
        result = cursor.fetchall()[0][0]
        print("number of entries received")
    except:
        print("error getting record count")
    cursor.close()
    con.close()

    return result


def update_meal_dish(user_id: int, meal_id: int, meal_dish: str) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_dish='{meal_dish}' WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_dish updated")
    except:
        con.rollback()
        print("error of meal_dish updating")
    cursor.close()
    con.close()


def update_meal_mass(user_id: int, meal_id: int, meal_mass: float) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_mass={meal_mass} WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_mass updated")
    except:
        con.rollback()
        print("error of meal_mass updating")
    cursor.close()
    con.close()


def update_meal_average_calories(
    user_id: int, meal_id: int, meal_average_calories: int
) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_average_calories={meal_average_calories} WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_average_calories updated")
    except:
        con.rollback()
        print("error of meal_average_calories updating")
    cursor.close()
    con.close()


def update_meal_average_proteins(
    user_id: int, meal_id: int, meal_average_proteins: int
) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_average_proteins={meal_average_proteins} WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_average_proteins updated")
    except:
        con.rollback()
        print("error of meal_average_proteins updating")
    cursor.close()
    con.close()


def update_meal_average_fats(
    user_id: int, meal_id: int, meal_average_fats: int
) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_average_fats={meal_average_fats} WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_average_fats updated")
    except:
        con.rollback()
        print("error of meal_average_fats updating")
    cursor.close()
    con.close()


def update_meal_average_carbohydrates(
    user_id: int, meal_id: int, meal_average_carbohydrates: int
) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_average_carbohydrates={meal_average_carbohydrates} WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_average_carbohydrates updated")
    except:
        con.rollback()
        print("error of meal_average_carbohydrates updating")
    cursor.close()
    con.close()


def update_meal_date(user_id: int, meal_id: int, meal_date: str) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_date='{meal_date}' WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_date updated")
    except:
        con.rollback()
        print("error of meal_date updating")
    cursor.close()
    con.close()


def update_meal_time(user_id: int, meal_id: int, meal_time: str) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_time='{meal_time}' WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("meal_time updated")
    except:
        con.rollback()
        print("error of meal_time updating")
    cursor.close()
    con.close()


def get_meal_object(user_id: int, meal_id: int) -> dict:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"SELECT * FROM meal WHERE user_id={user_id} AND meal_id={meal_id}"

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = dict(
            user_id=database_result[0][0],
            meal_id=database_result[0][1],
            meal_dish=database_result[0][2],
            meal_mass=database_result[0][3],
            meal_average_calories=database_result[0][4],
            meal_average_proteins=database_result[0][5],
            meal_average_fats=database_result[0][6],
            meal_average_carbohydrates=database_result[0][7],
            meal_date=database_result[0][8],
            meal_time=database_result[0][9],
        )
        print("record received")
    except:
        print("error of record receiving")
    cursor.close()
    con.close()

    return result


def get_all_meals(user_id: int) -> dict:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"SELECT * FROM meal WHERE user_id={user_id}"

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = {
            i: dict(
                user_id=database_result[0][0],
                meal_id=database_result[0][1],
                meal_dish=database_result[0][2],
                meal_mass=database_result[0][3],
                meal_average_calories=database_result[0][4],
                meal_average_proteins=database_result[0][5],
                meal_average_fats=database_result[0][6],
                meal_average_carbohydrates=database_result[0][7],
                meal_date=database_result[0][8],
                meal_time=database_result[0][9],
            )
            for i in range(len(database_result))
        }
        print("record received")
    except:
        print("error of record receiving")
    cursor.close()
    con.close()

    return result


def generate_meal_id(user_id: int) -> int:
    meal_id = get_number_of_user_meals(user_id) + 1
    return meal_id


def get_user_meal_for_day(user_id: int) -> dict:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"SELECT * FROM meal WHERE user_id={user_id} AND meal_date='{datetime.date.today()}'"

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = {
            i: dict(
                user_id=database_result[0][0],
                meal_id=database_result[0][1],
                meal_dish=database_result[0][2],
                meal_mass=database_result[0][3],
                meal_average_calories=database_result[0][4],
                meal_average_proteins=database_result[0][5],
                meal_average_fats=database_result[0][6],
                meal_average_carbohydrates=database_result[0][7],
                meal_date=database_result[0][8],
                meal_time=database_result[0][9],
            )
            for i in range(len(database_result))
        }
        print("time successfully taken")
    except:
        print("timing error")
    cursor.close()
    con.close()

    return result


if __name__ == "__main__":
    # print(get_number_of_user_meals(1983880200))
    # add_meal_note(1983880200, 1, "молоко", 200, 55, 3, 2.5, 4.7, "2022-02-17", "17:48:00")
    print(get_user_meal_for_day(1983880200))
