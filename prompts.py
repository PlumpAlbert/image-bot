import logging
import datetime

general_prompt = """
Ты профессиональный писатель. Твоя задача - написать текст, описывающий
окружение и заставляющий испытывать эмоции. Текст, что ты напишешь, будет
использован в генераторе изображений, учитывай это при составлении описания.

Полученный текст должен соответствовать следующим ограничениям:

- Должно содержать существ (людей, животных, вымышленных персонажей);
{{placeholder}}

В остальном - можешь придумывать что угодно.
"""

morning_prompt='- тема изображения - "Доброе утро".'

evening_prompt='- тема изображения - "Хорошего вечера".'

night_prompt='- тема изображения - "Спокойной ночи".'

def get_picture_prompt():
    """
    Generates a picture prompt based on the current time of day.

    Returns:
        str: The generated picture prompt.
    """
    logging.info('# Generate prompt based on current time')
    current_time = datetime.datetime.now()
    if current_time.hour >= 20:
        return general_prompt.replace('{{placeholder}}', night_prompt)

    if current_time.hour >= 16:
        return general_prompt.replace('{{placeholder}}', evening_prompt)

    return general_prompt.replace('{{placeholder}}', morning_prompt)

