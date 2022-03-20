<h1 align="center">Team 11 — FoodBot</h1>
<h4 align="center">A personal Telegram assistant for those who want to have a balanced diet :stew:</h4>

<div align="center">

  <a href="">![](https://img.shields.io/badge/bot-%40intel__11__food__bot-orange)</a>
  <a href="">![](https://img.shields.io/badge/language-ru-lightgray)</a>
  <a href="">![](https://img.shields.io/badge/python-3.9%2B-yellow)</a>
  <a href="">![](https://img.shields.io/badge/linter-flake8-brightgreen)</a>
  <a href="">![](https://img.shields.io/badge/database-pymysql-blue)</a>
  <a href="">![](https://img.shields.io/badge/API-python--telegram--bot-9cf)</a>

</div>


## Contributors

Alexey Ershov [@BadRedSL](https://github.com/BadRedSL) — Team Leader    
Daria Malikova [@damalikova](https://github.com/damalikova) — QA    
Nikita Chekmarev [@IamLimeCake](https://github.com/IamLimeCake) — Code Reviewer

## Project Status
**Project is**: in progress


*****


## Table of Contents
* [What FoodBot can do?](#what-foodbot-can-do)
* [How to use FoodBot? Setup](#how-to-use-foodbot-setup)
* [How to use FoodBot? Supported commands](#how-to-use-foodbot-supported-commands)
* [Project Structure](#project-structure)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)


## What FoodBot can do?
- [x] count user's daily amount of nutrients needed based on their physiological characteristics (e.g. age, sex, physical activity level etc.)
- [x] collect data on user's meals, namely portion size, calorific value, proteins/fats/carbs amount
- [x] edit user's personal data and make nutrients recount according to changes
- [x] provide daily, weekly, and monthly statistics of nutrient intake
- [x] send daily info about nutrient intake


## How to use FoodBot? Setup
### For personal use
Find FoodBot in Telegram and start a conversation with the `\start` command:

pic

### For creating your own bot

Requirements:
- **Python** 3.9+
- **PyMySQL**
- **python-telegram-api**

1. Clone the `Food_bot_Team_11` repository. 
2. Create Telegram bot following [Telegram documentation](https://core.telegram.org/bots).
3. Save your token into TOKEN variable at `token.json`. Make sure the file is stored one level above your project, so it won't be available on GitHub.
4. Install `MySQL` and start a connection.
5. Enjoy!

## How to use FoodBot? Supported commands
- [x] `\start` — begins acquaintance with a user, i.e. collects their personal information needed for nutrients count. If the user already exists, the bot deletes their personal information and meal database.
- [x] `\go` — provides the main menu:
  - `Внести прием пищи` aka `Add meal`
  - `Вспомнить свою норму КБЖУ` aka `Get nutrients norm`
  - `Получить статистику` aka `Get statistics`
  - `Изменить персональные данные` aka `Edit personal data`
  - `Удалить запись о последнем приеме пищи` aka `Delete the last meal info`
- [ ] `\help` — provides the list of available commands.


## Project Structure
The project contains the following modules:
module | description
------------ | ------------- 
`foodbot.py` | bot main file
`handlers.py` | bot handlers
`foodbot_filters.py` | custom filter class for user input check. Takes `state` as an argument for a specific filter activation
`user_class.py` | class for user instance creating, their nutrients count, adding to `user_database`, and getting statistics
`meal_class.py` | class for meal instance creating, adding to `meal_database`, and calculating nutrients norm for various time spans
`user_database.py` | database for all bot users
`user_meal_database.py` | database for users' meals (unique for each user)
`learned_dish_database.py` | database containing a list of unique dishes added by users


## Room for Improvement
- [ ] Implement a database with various dishes ([like this one](https://cross.expert/zdorovoe-pitanie/calories/tablitsa-kalorijnosti-gotovyh-produktov-i-blyud.html)), from which nutrient facts will be taken (so that user doesn't need to enter the facts themselves) 
- [ ] Implement asynchronous database support
- [ ] to be defined


## Acknowledgements
- The project was carried out with the support of [Intel Programming School](https://github.com/nn-students-2021h2). Thank you for the opportunity to grow professionally!
- Many thanks to [Malgorzata Rita Ły](https://github.com/ritaly) for `readme.md` template