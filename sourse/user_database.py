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
    user_carbohydrate_norm: float,
) -> None:

    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )
    cursor = con.cursor()
    sql = (
        f"INSERT INTO user (user_id, user_name, user_age, user_sex, user_height, user_weight, "
        f"user_activity, user_goal, user_calorie_norm, user_protein_norm, user_fat_norm, user_carbohydrate_norm)"
        f" VALUES ({user_id}, '{user_name}', {user_age}, '{user_sex}', {user_height}, "
        f"{user_weight}, '{user_activity}', '{user_goal}', {user_calorie_norm}, {user_protein_norm}, "
        f"{user_fat_norm}, {user_carbohydrate_norm})"
    )
    try:
        cursor.execute(sql)
        con.commit()
        print("note added")
    except:
        con.rollback()
        print("error of user adding")
    cursor.close()
    con.close()


def delete_note_with_id(user_id: int) -> None:
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
        print("note deleted")
    except:
        con.rollback()
        print("error of user deleting")
    cursor.close()
    con.close()


def update_user_name(user_id: int, new_user_name: str) -> None:
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
        print("user_name updated")
    except:
        con.rollback()
        print("error of user_name updating")
    cursor.close()
    con.close()


def update_user_age(user_id: int, new_user_age: int) -> None:
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
        print("user_age updated")
    except:
        con.rollback()
        print("error of user_age updating")
    cursor.close()
    con.close()


def update_user_height(user_id: int, user_height: float) -> None:
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
        print("user_height updated")
    except:
        con.rollback()
        print("error of user_height updating")
    cursor.close()
    con.close()


def update_user_weight(user_id: int, user_weight: float) -> None:
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
        print("user_weight updated")
    except:
        con.rollback()
        print("error of user_weight updating")
    cursor.close()
    con.close()


def update_user_activity(user_id: int, user_activity: str) -> None:
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
        print("user_activity updated")
    except:
        con.rollback()
        print("error of user_activity updating")
    cursor.close()
    con.close()


def update_user_goal(user_id: int, user_goal: str) -> None:
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
        print("user_goal updated")
    except:
        con.rollback()
        print("error of user_goal updating")
    cursor.close()
    con.close()


def update_user_calorie_norm(user_id: int, user_calorie_norm: float) -> None:
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
        print("user_calorie_norm updated")
    except:
        con.rollback()
        print("error of user_calorie_norm updating")
    cursor.close()
    con.close()


def update_user_protein_norm(user_id: int, user_protein_norm: float) -> None:
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
        print("user_protein_norm updated")
    except:
        con.rollback()
        print("error of user_protein_norm updating")
    cursor.close()
    con.close()


def update_user_fat_norm(user_id: int, user_fat_norm: float) -> None:
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
        print("user_fat_norm updated")
    except:
        con.rollback()
        print("error of user_fat_norm updating")
    cursor.close()
    con.close()


def update_user_carbohydrate_norm(user_id: int, user_carbohydrate_norm: float) -> None:
    con = pymysql.connect(
        host="localhost",
        user="foodbot",
        password="FoodBot1234",
        database="telegram_user",
    )

    cursor = con.cursor()
    sql = f"UPDATE user SET user_carbohydrate_norm={user_carbohydrate_norm} WHERE user_id={user_id}"
    try:
        cursor.execute(sql)
        con.commit()
        print("user_carbohydrate_norm updated")
    except:
        con.rollback()
        print("error of user_carbohydrate_norm updating")
    cursor.close()
    con.close()


def get_user_object(user_id: int) -> dict:
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
            user_carbohydrate_norm=database_result[0][11],
        )
        print("record received")
    except:
        print("error of record receiving")
    cursor.close()
    con.close()

    return result


if __name__ == "__main__":
    print(get_user_object(1983880200))
