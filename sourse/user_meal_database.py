import pymysql
import datetime


def add_meal_note(
    user_id: int,
    meal_id: int,
    meal_name: str,
    meal_size: float,
    meal_average_calories: float,
    meal_average_proteins: float,
    meal_average_fats: float,
    meal_average_carbs: float,
    meal_date: str,
    meal_time: str,
) -> None:
    """
    Adds one meal entry to meal database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )
    cursor = con.cursor()
    sql = (
        f"INSERT INTO meal (user_id, meal_id, meal_name, meal_size, meal_average_calories, meal_average_proteins,"
        f" meal_average_fats, meal_average_carbs, meal_date, meal_time) VALUES ({user_id},"
        f" {meal_id}, '{meal_name}', {meal_size}, {meal_average_calories}, {meal_average_proteins},"
        f" {meal_average_fats}, {meal_average_carbs}, '{meal_date}', '{meal_time}')"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of adding '{meal_name}' by user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of adding '{meal_name}' by user_id = '{user_id} ' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def delete_all_meal_notes(user_id: int) -> None:
    """
    Deletes all meal entries for a single user from the meal database
    """
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
        print(f"SUCCESS of deleting all notes with user_id = '{user_id}' from user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of deleting all notes with user_id = '{user_id}' from user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def delete_meal_note(user_id: int, meal_id: int) -> None:
    """
    Deletes one meal entry for a single user from the meal database
    """
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
        print(f"SUCCESS of deleting note with user_id = '{user_id}' from user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of deleting note with user_id = '{user_id}' from user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def get_number_of_user_meals(user_id: int) -> int:
    """
    Returns the number of meal entries for single user in the meal database
    """
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
        print(f"SUCCESS of getting number_of_meals with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        print(f"ERROR of getting number_of_meals with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


def update_meal_name(user_id: int, meal_id: int, meal_name: str) -> None:
    """
    Updates the name of the meal of single user in meal database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_name='{meal_name}' WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating meal_name with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_name with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_meal_mass(user_id: int, meal_id: int, meal_mass: float) -> None:
    """
    Updates the mass of the meal of single user in meal database
    """
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
        print(f"SUCCESS of updating meal_mass with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_mass with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_meal_average_calories(
    user_id: int, meal_id: int, meal_average_calories: int
) -> None:
    """
    Updates average calories of the meal of single user in meal database
    """
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
        print(f"SUCCESS of updating meal_average_calories with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_average_calories with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_meal_average_proteins(
    user_id: int, meal_id: int, meal_average_proteins: int
) -> None:
    """
    Updates average proteins of the meal of single user in meal database
    """
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
        print(f"SUCCESS of updating meal_average_proteins with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_average_proteins with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_meal_average_fats(
    user_id: int, meal_id: int, meal_average_fats: int
) -> None:
    """
    Updates average fats of the meal of single user in meal database
    """
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
        print(f"SUCCESS of updating meal_average_fats with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_average_fats with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_meal_average_carbs(
    user_id: int, meal_id: int, meal_average_carbs: int
) -> None:
    """
    Updates average carbs of the meal of single user in meal database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE meal SET meal_average_carbs={meal_average_carbs} WHERE user_id={user_id} AND meal_id={meal_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating meal_average_carbs with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_average_carbs with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_meal_date(user_id: int, meal_id: int, meal_date: str) -> None:
    """
    Updates date of the meal of single user in meal database
    """
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
        print(f"SUCCESS of updating meal_date with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_date with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_meal_time(user_id: int, meal_id: int, meal_time: str) -> None:
    """
    Updates time of the meal of single user in meal database
    """
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
        print(f"SUCCESS of updating meal_time with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating meal_time with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def get_meal_object(user_id: int, meal_id: int) -> dict:
    """
    Returns all data about meal of single user from meal database
    """
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
            meal_name=database_result[0][2],
            meal_mass=database_result[0][3],
            meal_average_calories=database_result[0][4],
            meal_average_proteins=database_result[0][5],
            meal_average_fats=database_result[0][6],
            meal_average_carbs=database_result[0][7],
            meal_date=database_result[0][8],
            meal_time=database_result[0][9],
        )
        print(f"SUCCESS of getting meal_object with user_id = '{user_id}' and "
              f"meal_id = '{meal_id}' in user_meal database")
    except pymysql.Error as e:
        print(f"ERROR of getting meal_object with user_id = '{user_id}' and "
              f"meal_id = '{meal_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


def get_all_meals(user_id: int) -> dict:
    """
    Returns all data about all meals of single user from meal database
    """
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
                meal_name=database_result[0][2],
                meal_mass=database_result[0][3],
                meal_average_calories=database_result[0][4],
                meal_average_proteins=database_result[0][5],
                meal_average_fats=database_result[0][6],
                meal_average_carbs=database_result[0][7],
                meal_date=database_result[0][8],
                meal_time=database_result[0][9],
            )
            for i in range(len(database_result))
        }
        print(f"SUCCESS of getting all meal_objects with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        print(f"ERROR of getting all meal_objects with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


def generate_meal_id(user_id: int) -> int:
    """
    Returns unique generated id for new meal of single user
    """
    meal_id = get_number_of_user_meals(user_id) + 1
    return meal_id


def get_user_meal_for_day(user_id: int) -> dict:
    """
    Returns all data about a meal of single user for 1 day from meal database
    """
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
                meal_name=database_result[0][2],
                meal_mass=database_result[0][3],
                meal_average_calories=database_result[0][4],
                meal_average_proteins=database_result[0][5],
                meal_average_fats=database_result[0][6],
                meal_average_carbs=database_result[0][7],
                meal_date=database_result[0][8],
                meal_time=database_result[0][9],
            )
            for i in range(len(database_result))
        }
        print(f"SUCCESS of getting user_meal_for_day with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        print(f"ERROR of getting user_meal_for_day with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


def get_user_meal_for_week(user_id: int) -> dict:
    """
    Returns all data about a meal of single user for last 7 days from meal database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = (
        f"SELECT * FROM meal WHERE user_id={user_id} AND"
        f" meal_date >= '{datetime.date.today()-datetime.timedelta(days=7)}' AND"
        f" meal_date < '{datetime.date.today()}'"
    )

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = {
            i: dict(
                user_id=database_result[i][0],
                meal_id=database_result[i][1],
                meal_name=database_result[i][2],
                meal_mass=database_result[i][3],
                meal_average_calories=database_result[i][4],
                meal_average_proteins=database_result[i][5],
                meal_average_fats=database_result[i][6],
                meal_average_carbs=database_result[i][7],
                meal_date=database_result[i][8],
                meal_time=database_result[i][9],
            )
            for i in range(len(database_result))
        }
        print(f"SUCCESS of getting user_meal_for_week with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        print(f"ERROR of getting user_meal_for_week with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


def get_user_meal_for_month(user_id: int) -> dict:
    """
    Returns all data about a meal of single user for last 31 days from meal database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = (
        f"SELECT * FROM meal WHERE user_id={user_id} AND"
        f" meal_date >= '{datetime.date.today()-datetime.timedelta(days=31)}' AND"
        f" meal_date < '{datetime.date.today()}'"
    )

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = {
            i: dict(
                user_id=database_result[i][0],
                meal_id=database_result[i][1],
                meal_name=database_result[i][2],
                meal_mass=database_result[i][3],
                meal_average_calories=database_result[i][4],
                meal_average_proteins=database_result[i][5],
                meal_average_fats=database_result[i][6],
                meal_average_carbs=database_result[i][7],
                meal_date=database_result[i][8],
                meal_time=database_result[i][9],
            )
            for i in range(len(database_result))
        }
        print(f"SUCCESS of getting user_meal_for_month with user_id = '{user_id}' in user_meal database")
    except pymysql.Error as e:
        print(f"ERROR of getting user_meal_for_month with user_id = '{user_id}' in user_meal database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


if __name__ == "__main__":
    # print(get_number_of_user_meals(1983880200))
    # add_meal_note(1983880200, 1, "молоко", 200, 55, 3, 2.5, 4.7, "2022-02-17", "17:48:00")
    # print(get_user_meal_for_day(1983880200))
    # print(datetime.date.today()-datetime.timedelta(days=31))
    # print(len(get_user_meal_for_day(1983880200)))
    print(f"количество блюд за неделю {len(get_user_meal_for_week(1983880200))}")
    for i, j in get_user_meal_for_week(1983880200).items():
        print(j)
    print(f"количество блюд за месяц {len(get_user_meal_for_month(1983880200))}")
    for i, j in get_user_meal_for_month(1983880200).items():
        print(j)
