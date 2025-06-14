import time

def typing_animation(message, delay=0.05):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to next line after the message

# Life Path Number Descriptions
life_path_descriptions = {
    1: "You are a natural leader, independent and ambitious.",
    2: "You are a peacemaker, cooperative and sensitive.",
    3: "You are creative, expressive, and full of joy.",
    4: "You are practical, disciplined, and hardworking.",
    5: "You are adventurous, dynamic, and freedom-loving.",
    6: "You are caring, responsible, and family-oriented.",
    7: "You are analytical, spiritual, and a seeker of truth.",
    8: "You are powerful, goal-driven, and business-minded.",
    9: "You are compassionate, wise, and humanitarian."
}

# Zodiac Sign Descriptions
zodiac_descriptions = {
    "Aries": "Bold and energetic, you love to take initiative.",
    "Taurus": "Reliable and patient, you appreciate the finer things in life.",
    "Gemini": "Curious and adaptable, you thrive on new experiences.",
    "Cancer": "Emotional and nurturing, you deeply care for others.",
    "Leo": "Confident and charismatic, you naturally draw attention.",
    "Virgo": "Detail-oriented and thoughtful, you strive for perfection.",
    "Libra": "Balanced and fair, you seek harmony in all aspects of life.",
    "Scorpio": "Intense and passionate, you have a magnetic presence.",
    "Sagittarius": "Optimistic and adventurous, you love exploring the unknown.",
    "Capricorn": "Ambitious and disciplined, you work steadily towards success.",
    "Aquarius": "Innovative and independent, you think outside the box.",
    "Pisces": "Dreamy and compassionate, you are in tune with emotions."
}

# Welcome Section
typing_animation("Welcome to the Astrology & Numerology Calculator! ✨\n")
typing_animation("Discover your Life Path Number and Zodiac Sign! 🌟\n")

def calculate_life_path(dob):
    dob_numbers = [int(num) for num in dob if num.isdigit()]
    total = sum(dob_numbers)
    
    while total > 9:
        digits = [int(d) for d in str(total)]
        total = sum(digits)
    
    return total

def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

# Input
birth_date = input("Enter your birth date (DD/MM/YYYY): ")
day, month, year = map(int, birth_date.split('/'))

# Calculate Life Path Number
life_path = calculate_life_path(birth_date)
life_path_description = life_path_descriptions.get(life_path, "A unique individual with special traits!")

# Find Zodiac Sign
zodiac = get_zodiac_sign(day, month)
zodiac_description = zodiac_descriptions.get(zodiac, "A special soul with unique cosmic energy!")

# Output with Animation
typing_animation(f"Your Life Path Number is: {life_path}")
typing_animation(f"Meaning: {life_path_description}\n")

typing_animation(f"Your Zodiac Sign is: {zodiac}")
typing_animation(f"Meaning: {zodiac_description}")
