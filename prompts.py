import logging
import datetime

general_prompt = """
Твоя задача - написать текст для генератора изображений. Он должен содержать
подробные инструкции о том, что и как нужно нарисовать на картинке.

Указания для генератора должны соответствовать следующим ограничениям:

- Обязательно должно содержать существо (людей, животных, вымышленных персонажей);
- Картинка должна быть выполнена в мультяшном стиле;
{{placeholder}}

В остальном - можешь придумывать что угодно. Ответ должен содержать лишь
текстовые инструкции для генератора.
"""

morning_prompt = '- тема изображения - "Доброе утро".'

evening_prompt = '- тема изображения - "Хорошего вечера".'

night_prompt = '- тема изображения - "Спокойной ночи и сладких снов".'


def get_picture_prompt():
    """
    Generates a picture prompt based on the current time of day.

    Returns:
        str: The generated picture prompt.
    """
    logging.info("# Generate prompt based on current time")
    current_time = datetime.datetime.now()
    if current_time.hour >= 20:
        return general_prompt.replace("{{placeholder}}", night_prompt)

    if current_time.hour >= 16:
        return general_prompt.replace("{{placeholder}}", evening_prompt)

    return general_prompt.replace("{{placeholder}}", morning_prompt)
