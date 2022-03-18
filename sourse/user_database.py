import pymysql


def add_note(
    user_id: int,
    user_name: str,
    user_age: int,
    user_sex: str,
    user_height: float,
    user_weight: float,
    user_activity: str,
    user_goal: str,
    user_calorie_norm: float,
    user_protein_norm: float,
    user_fat_norm: float,
    user_carb_norm: float,
) -> None:
    """
    Adds one user entry to user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )
    cursor = con.cursor()
    sql = (
        f"INSERT INTO user (user_id, user_name, user_age, user_sex, user_height, user_weight, "
        f"user_activity, user_goal, user_calorie_norm, user_protein_norm, user_fat_norm, user_carb_norm)"
        f" VALUES ({user_id}, '{user_name}', {user_age}, '{user_sex}', {user_height}, "
        f"{user_weight}, '{user_activity}', '{user_goal}', {user_calorie_norm}, {user_protein_norm}, "
        f"{user_fat_norm}, {user_carb_norm})"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of adding user_note with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of adding user_note with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def delete_note_with_id(user_id: int) -> None:
    """
    Deletes one user entry from user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"DELETE FROM user WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of deleting user_note with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of deleting user_note with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_name(user_id: int, new_user_name: str) -> None:
    """
    Updates the name of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_name='{new_user_name}' WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_name with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_name with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_age(user_id: int, new_user_age: int) -> None:
    """
    Updates the age of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_age={new_user_age} WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_age with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_age with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_sex(user_id: int, new_user_sex: str) -> None:
    """
    Updates the sex of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_sex='{new_user_sex}' WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_sex with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_sex with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_height(user_id: int, user_height: float) -> None:
    """
    Updates the height of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_height={user_height} WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_height with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_height with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_weight(user_id: int, user_weight: float) -> None:
    """
    Updates the weight of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_weight={user_weight} WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_weight with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_weight with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_activity(user_id: int, user_activity: str) -> None:
    """
    Updates the activity of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_activity='{user_activity}' WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_activity with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_activity with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_goal(user_id: int, user_goal: str) -> None:
    """
    Updates the goal of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_goal='{user_goal}' WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_goal with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_goal with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_calorie_norm(user_id: int, user_calorie_norm: float) -> None:
    """
    Updates the calorie norm of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = (
        f"UPDATE user SET user_calorie_norm={user_calorie_norm} WHERE user_id={user_id}"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_calorie_norm with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_calorie_norm with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_protein_norm(user_id: int, user_protein_norm: float) -> None:
    """
    Updates the protein norm of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = (
        f"UPDATE user SET user_protein_norm={user_protein_norm} WHERE user_id={user_id}"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_protein_norm with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_protein_norm with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_fat_norm(user_id: int, user_fat_norm: float) -> None:
    """
    Updates the fat norm of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_fat_norm={user_fat_norm} WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_fat_norm with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_fat_norm with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def update_user_carb_norm(user_id: int, user_carb_norm: float) -> None:
    """
    Updates the carb norm of the user in user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_carb_norm={user_carb_norm} WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print(f"SUCCESS of updating user_carb_norm with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        con.rollback()
        print(f"ERROR of updating user_carb_norm with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()


def get_user_object(user_id: int) -> dict:
    """
    Returns all data about user from user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"SELECT * FROM user WHERE user_id={user_id}"

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = dict(
            user_id=database_result[0][0],
            user_name=database_result[0][1],
            user_age=database_result[0][2],
            user_sex=database_result[0][3],
            user_height=database_result[0][4],
            user_weight=database_result[0][5],
            user_activity=database_result[0][6],
            user_goal=database_result[0][7],
            user_calorie_norm=database_result[0][8],
            user_protein_norm=database_result[0][9],
            user_fat_norm=database_result[0][10],
            user_carb_norm=database_result[0][11],
        )
        print(f"SUCCESS of getting user_object with user_id = '{user_id}' in user database")
    except pymysql.Error as e:
        print(f"ERROR of getting user_object with user_id = '{user_id}' in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


def get_all_user_info() -> dict:
    """
    Returns all data about all users from user database
    """
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"SELECT * FROM user"

    result = {}
    try:
        cursor.execute(sql)
        database_result = cursor.fetchall()
        result = {
            i: dict(
                user_id=database_result[i][0],
                user_name=database_result[i][1],
                user_age=database_result[i][2],
                user_sex=database_result[i][3],
                user_height=database_result[i][4],
                user_weight=database_result[i][5],
                user_activity=database_result[i][6],
                user_goal=database_result[i][7],
                user_calorie_norm=database_result[i][8],
                user_protein_norm=database_result[i][9],
                user_fat_norm=database_result[i][10],
                user_carb_norm=database_result[i][11],
            )
            for i in range(len(database_result))
        }
        print(f"SUCCESS of getting all user_objects in user database")
    except pymysql.Error as e:
        print(f"ERROR of getting all user_objects in user database - "
              f"pymysql {e.args[0]}: {e.args[1]}")
    cursor.close()
    con.close()

    return result


if __name__ == "__main__":
    print(get_all_user_info())
