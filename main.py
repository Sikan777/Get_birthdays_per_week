from datetime import date, datetime


def get_birthdays_per_week(users):
     #створюєму змінну, яка приймає теперішню дату 
    current_data = datetime.today()
    
    #це є той словник з пустими словниками  без суботи і неділі
    birthday_dict = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
    }

    #шукаємо дні народження у списку користувачів
    for user in users:
        birthday = user['birthday']
        name = user['name']
        if birthday.year < 1913: # провіряємо чи людину вартує відкопувати і вітати
            print(f"The birth year {birthday.year}, maybe you have  Frodo`s ring?")
            continue
        if birthday.year > current_data.year: # провіряємо чи людина не з майбутнього
            print(f"The birth year {birthday.year}, maybe you are traveler from the future?")
            continue
        # Перевіряємо, чи день народження співпадає з поточним місяцем.
        if birthday.month == current_data.month:
            if birthday.day <= current_data.day + 7 and birthday.day >= (current_data).day:
                try_day =datetime(current_data.year,birthday.month,birthday.day)
                # Перетягуємо наших іменинників на понеділок
                week_day = try_day.strftime('%A') if try_day.strftime('%A') not in ('Sunday' ,'Saturday') else 'Monday'
                birthday_dict[week_day].append(name)
        # Перевіряємо, чи день народження співпадає з наступним місяцем.        
        if birthday.month - current_data.month == 1:
            if birthday.day <= (current_data + date.timedelta(days=7)).day:
                try_day = datetime(current_data.year,birthday.month,birthday.day)
                week_day = try_day.strftime('%A') if try_day.strftime('%A') not in ('Sunday' ,'Saturday') else 'Monday'
                birthday_dict[week_day].append(name)
                

    return birthday_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Yura Skeba", "birthday": datetime(1993, 5, 4).date()},
        {"name": "Denys Parandiy", "birthday": datetime(1994, 5, 5).date()},
        {"name": "Bohdan Sikan", "birthday": datetime(1991, 9, 5).date()},
        {"name": "Jorjio Pistolero", "birthday": datetime(1991, 9, 9).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")