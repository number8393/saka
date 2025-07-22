import datetime

def get_news():
    now = datetime.datetime.now()
    if now.hour < 10:
        return "📰 Утренние новости: Низкая активность, ждем открытия Европы."
    elif now.hour < 14:
        return "🌍 Европейская сессия активна. Возможны движения."
    elif now.hour < 18:
        return "💼 Американская сессия начинается. Будьте внимательны."
    else:
        return "🌙 Вечерняя сессия. Волатильность снижается."