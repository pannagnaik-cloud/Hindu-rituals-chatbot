# knowledge_base.py

# A list of dictionaries, where each dictionary is a topic about a Hindu ritual.
# Each topic has a name, keywords to trigger it, and the rules/information.
# IMPORTANT: This is a simplified, generalized knowledge base for demonstration.

RITUAL_DATA = [
    {
        "topic": "Daily Puja (Worship)",
        "keywords": ["daily puja", "morning worship", "aarti", "puja", "worship"],
        "rules": """
Daily Puja is a personal ritual to connect with the divine. General steps include:
1.  **Personal Cleanliness**: Take a bath, wear clean clothes.
2.  **Cleanliness of the Altar**: Clean the place of worship.
3.  **Setting up the Deities**: Arrange the idols or pictures of deities.
4.  **Offerings (Upachara)**:
    *   **Avahana**: Invoking the deity.
    *   **Asana**: Offering a seat.
    *   **Padya**: Offering water to wash the feet.
    *   **Arghya**: Offering water to wash the hands.
    *   **Achamana**: Sipping water for purification.
    *   **Snana**: Bathing the idol with holy water (or symbolically).
    *   **Vastra**: Offering clothes.
    *   **Gandha**: Applying sandalwood paste.
    *   **Pushpa**: Offering flowers.
    *   **Dhupa**: Lighting incense.
    *   **Dipa**: Lighting a lamp (diya).
    *   **Naivedya**: Offering food (e.g., fruits, sweets).
5.  **Aarti**: Waving a lit lamp in a circular motion while singing aarti.
6.  **Pradakshina & Namaskar**: Circumambulating the altar and bowing down.

DISCLAIMER: The specific steps and mantras can vary greatly based on tradition.
        """
    },
    {
        "topic": "Diwali (Festival of Lights)",
        "keywords": ["diwali", "deepavali", "festival of lights", "lakshmi puja"],
        "rules": """
Diwali is a major festival celebrating the return of Lord Rama to Ayodhya. Key rituals include:
1.  **Cleaning and Decorating**: Homes are thoroughly cleaned and decorated with rangoli and lights.
2.  **Lakshmi Puja**: The main ritual, performed on the darkest night (Amavasya) to welcome Goddess Lakshmi, the goddess of wealth.
    *   A new cloth is spread on a raised platform.
    *   Idols of Goddess Lakshmi and Lord Ganesha are placed and decorated.
    *   Offerings of sweets, fruits, and coins are made.
    *   Lakshmi Ashtottara Shatanamavali (108 names) is recited.
3.  **Lighting Diyas**: Oil lamps (diyas) are lit all around the house to ward off darkness and negativity.
4.  **Bursting Firecrackers**: Traditionally done to celebrate the joyous occasion.
5.  **Sharing Sweets and Gifts**: Exchanging gifts and sweets with family and friends.

DISCLAIMER: The day of Lakshmi Puja and specific traditions can vary by region.
        """
    },
    {
        "topic": "Hindu Marriage (Vivaha)",
        "keywords": ["marriage", "vivaha", "wedding", "kanyadaan", "pheras"],
        "rules": """
A Hindu Vivaha is a sacred sacrament. Key rituals include:
1.  **Sagai (Engagement)**: Formal announcement of the wedding.
2.  **Sangeet & Mehendi**: A night of music and dance, and applying henna to the bride's hands.
3.  **Baraat**: The groom's procession, where he arrives at the wedding venue.
4.  **Jaimala/Varmala**: The bride and groom exchange garlands.
5.  **Kanyadaan**: The bride's parents formally give her away to the groom.
6.  **Saptapadi (Seven Pheras)**: The couple takes seven rounds around the sacred fire (Agni), each round representing a sacred vow.
7.  **Sindoor & Mangalsutra**: The groom applies sindoor (vermilion) to the bride's hair parting and ties a mangalsutra (sacred necklace).

DISCLAIMER: Wedding rituals are extremely diverse and can last for several days, varying immensely by community.
        """
    },
    {
        "topic": "Fasting (Vrata)",
        "keywords": ["fasting", "vrata", "upavasa", "ekadashi", "fast"],
        "rules": """
Fasting, or Vrata, is a common practice for spiritual purification and self-discipline.
1.  **Types of Fasts**:
    *   **Nirjala**: No food or water.
    *   **Phalahar**: Eating only fruits, milk, and nuts.
    *   **Partial Fasting**: Avoiding grains and specific vegetables.
2.  **Common Fasting Days**:
    *   **Ekadashi**: The 11th day of the lunar fortnight, dedicated to Lord Vishnu.
    *   **Pradosh Vrat**: The 13th day of the lunar fortnight, dedicated to Lord Shiva.
    *   **Navratri**: A nine-night festival where many people fast or avoid specific foods.
3.  **Rules**: On a fasting day, one is expected to maintain a pure mind, avoid anger, and chant mantras or read scriptures. The fast is typically broken at a specific time (parana) after performing puja.

DISCLAIMER: The rules and type of fast depend entirely on the specific vrat being observed and personal capacity.
        """
    }
]

def get_available_topics():
    """Returns a list of all available topics for the user."""
    return [item['topic'] for item in RITUAL_DATA]
