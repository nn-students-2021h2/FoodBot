import pymysql

con = pymysql.connect(host='localhost', user='foodbot',
                      password='FoodBot1234', database='telegram_user')


def add_note(user_id: int, user_name: str, user_age: int, user_sex: str, user_height: float, user_weight: float,
             user_activity: str, user_goal: str, user_calorie_norm: float, user_protein_norm: float,
             user_fat_norm: float, user_carbohydrate_norm: float) -> None:
    cursor = con.cursor()
    sql = f"INSERT INTO user (user_id, user_name, user_age, user_sex, user_height, user_weight, " \
          f"user_activity, user_goal, user_calorie_norm, user_protein_norm, user_fat_norm, user_carbohydrate_norm)" \
          f" VALUES ({user_id}, '{user_name}', {user_age}, '{user_sex}', {user_height}, " \
          f"{user_weight}, '{user_activity}', '{user_goal}', {user_calorie_norm}, {user_protein_norm}, " \
          f"{user_fat_norm}, {user_carbohydrate_norm})"
    print(sql)
    try:
        # Выполнить SQL для вставки данных
        cursor.execute(sql)

        # Сохранить данные в базу данных
        con.commit()
        print('ok')

    except:
        # Откатить состояние, если при выполнении произошла ошибка
        con.rollback()
        print('error of user adding')

    # Наконец, закройте соединение с базой данных
    con.close()
