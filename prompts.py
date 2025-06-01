import logging
import datetime

general_prompt="""
Write prompt that will be used for generative LLM which will generate image
forbased on your text.
{{placeholder}}
Respond with only the prompt text and nothing else.
The prompt should not contain any placeholders.
"""

morning_prompt="""
The text that you will generate should inspire people to wake up from their beds
in the morning. It should be fun, playful and childish. Be sure to instruct LLM
to add custom text, like 'Good morning!'.
"""

evening_prompt="""
Make sure to instruct LLM to generate picture for the end of the day. It
should be calm, soothing and relaxing. For example, an image of a sunset or a
fireplace.
"""

night_prompt="""
The prompt should describe a nighttime. Make sure to include a bed, sleepy animal
or anything else related to the bedtime. For example, an image of a sleeping animal
in clothes.
"""

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

