import sys
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

emojis = {
     "lol": {
        "emoji": "😂",
        "alternatives": ["laughing", "funny", "hilarious", "haha", "hehe", "rofl", "lmao", "roflmao", "humor", "joke", "jest", "giggle", "chuckle", "crack up", "laughed", "laughs", "laughing out loud"]
    },
    "sad": {
        "emoji": "😔",
        "alternatives": ["unhappy", "down", "depressed", "blue", "gloomy", "melancholy", "sorrowful", "miserable", "heartbroken", "dejected", "discouraged", "disheartened", "glumly", "sadden", "saddened", "saddens", "saddening"]
    },
    "happy": {
        "emoji": "😃",
        "alternatives": ["smile", "joy", "delighted", "cheerful", "content", "pleased", "jubilant", "elated", "ecstatic", "merry", "jovial", "gleeful", "beaming", "grinning", "enjoy", "enjoyed", "enjoying", "enjoys"]
    },
    "angry": {
        "emoji": "😡",
        "alternatives": ["mad", "furious", "enraged", "irate", "outraged", "fuming", "seething", "livid", "irritated", "annoyed", "cross", "heated", "anger", "angered", "angers", "angering", "rage", "raged", "raging", "rages"]
    },
    "love": {
        "emoji": "❤️",
        "alternatives": ["heart", "affection", "adore", "cherish", "devotion", "fondness", "passion", "beloved", "darling", "sweetheart", "loves", "loved", "loving", "romantic", "romance", "infatuated"]
    },
    "run": {
        "emoji": "🏃",
        "alternatives": ["jog", "sprint", "dash", "race", "bolt", "hurry", "running", "ran", "runs", "flee", "fled", "escape", "escaped", "escaping", "escapes", "exercise", "exercising", "exercised", "exercises"]
    },
    "eat": {
        "emoji": "🍽️",
        "alternatives": ["dining", "consume", "devour", "feast", "munch", "ate", "eaten", "eating", "eats", "dine", "dined", "dining", "dines", "feed", "fed", "feeding", "feeds", "hungry", "famished", "starving"]
    },
    "sleep": {
        "emoji": "😴",
        "alternatives": ["doze", "rest", "nap", "snooze", "slumber", "hibernate", "sleeping", "slept", "sleeps", "tired", "exhausted", "fatigued", "drowsy", "yawn", "yawned", "yawning", "yawns"]
    },
    "think": {
        "emoji": "🤔",
        "alternatives": ["ponder", "contemplate", "consider", "reflect", "meditate", "brainstorm", "thought", "thinking", "thinks", "thought", "thoughtful", "analyze", "analyzed", "analyzing", "analyzes", "wonder", "wondered", "wondering", "wonders"]
    },
    "work": {
        "emoji": "💼",
        "alternatives": ["job", "career", "occupation", "profession", "employ", "task", "working", "worked", "works", "labor", "labored", "laboring", "labors", "toil", "toiled", "toiling", "toils", "busy", "occupied"]
    },
    "dance": {
        "emoji": "💃",
        "alternatives": ["dancing", "danced", "dances", "boogie", "groove", "sway", "twirl", "spin", "ballet", "waltz", "tango", "choreography", "party", "celebrate", "celebrating", "celebrated", "celebrates"]
    },
    "cook": {
        "emoji": "👩‍🍳",
        "alternatives": ["cooking", "cooked", "cooks", "bake", "baked", "baking", "bakes", "fry", "fried", "frying", "fries", "grill", "grilled", "grilling", "grills", "chef", "prepare", "prepared", "preparing", "prepares", "recipe"]
    },
    "travel": {
        "emoji": "✈️",
        "alternatives": ["journey", "trip", "voyage", "touring", "traveled", "travels", "traveling", "fly", "flew", "flying", "flies", "vacation", "vacationing", "vacationed", "vacations", "adventure", "adventuring", "adventured", "adventures"]
    },
    "music": {
        "emoji": "🎶",
        "alternatives": ["melody", "tune", "song", "singing", "sang", "sings", "play", "played", "playing", "plays", "perform", "performed", "performing", "performs", "concert", "orchestra", "band", "musical", "musician"]
    },
    "read": {
        "emoji": "📚",
        "alternatives": ["reading", "reads", "study", "studying", "studied", "studies", "learn", "learning", "learned", "learns", "book", "novel", "literature", "text", "peruse", "perusing", "perused", "peruses"]
    },
    "write": {
        "emoji": "✍️",
        "alternatives": ["writing", "wrote", "written", "writes", "compose", "composing", "composed", "composes", "author", "authoring", "authored", "authors", "scribble", "scribbling", "scribbled", "scribbles", "pen", "pencil"]
    },
    "lol": {"emoji": "😂", "alternatives": ["laughing", "funny"]},
    "xD": {"emoji": "😆", "alternatives": ["laugh", "grin"]},
    "sad": {"emoji": "😔", "alternatives": ["unhappy", "down"]},
    "happy": {"emoji": "😃", "alternatives": ["smile", "joy"]},
    "angry": {"emoji": "😡", "alternatives": ["mad", "furious"]},
    "heart": {"emoji": "❤️", "alternatives": ["love", "affection"]},
    "thumbs_up": {"emoji": "👍", "alternatives": ["approve", "good"]},
    "thumbs_down": {"emoji": "👎", "alternatives": ["disapprove", "bad"]},
    "clap": {"emoji": "👏", "alternatives": ["applause", "cheer"]},
    "fire": {"emoji": "🔥", "alternatives": ["hot", "flame"]},
    "star": {"emoji": "⭐", "alternatives": ["shine", "favorite"]},
    "party": {"emoji": "🥳", "alternatives": ["celebrate", "festive"]},
    "cry": {"emoji": "😭", "alternatives": ["tears", "sorrow"]},
    "kiss": {"emoji": "😘", "alternatives": ["smooch", "affection"]},
    "wink": {"emoji": "😉", "alternatives": ["playful", "flirt"]},
    "love": {"emoji": "😍", "alternatives": ["adoration", "crush"]},
    "thinking": {"emoji": "🤔", "alternatives": ["ponder", "contemplate"]},
    "sunglasses": {"emoji": "😎", "alternatives": ["cool", "chill"]},
    "surprised": {"emoji": "😲", "alternatives": ["shock", "wow"]},
    "tired": {"emoji": "😩", "alternatives": ["exhausted", "drained"]},
    "sleepy": {"emoji": "😴", "alternatives": ["dozy", "rest"]},
    "confused": {"emoji": "😕", "alternatives": ["perplexed", "baffled"]},
    "scream": {"emoji": "😱", "alternatives": ["fear", "panic"]},
    "laugh": {"emoji": "🤣", "alternatives": ["hilarious", "funny"]},
    "money": {"emoji": "💰", "alternatives": ["cash", "wealth"]},
    "cat": {"emoji": "🐱", "alternatives": ["kitten", "feline"]},
    "dog": {"emoji": "🐶", "alternatives": ["puppy", "canine"]},
    "bear": {"emoji": "🐻", "alternatives": ["grizzly", "wildlife"]},
    "fish": {"emoji": "🐟", "alternatives": ["aquatic", "seafood"]},
    "tiger": {"emoji": "🐯", "alternatives": ["big cat", "wild cat"]},
    "chicken": {"emoji": "🐔", "alternatives": ["poultry", "bird"]},
    "pizza": {"emoji": "🍕", "alternatives": ["food", "slice"]},
    "burger": {"emoji": "🍔", "alternatives": ["hamburger", "sandwich"]},
    "cake": {"emoji": "🎂", "alternatives": ["dessert", "birthday"]},
    "coffee": {"emoji": "☕", "alternatives": ["caffeine", "brew"]},
    "beer": {"emoji": "🍺", "alternatives": ["ale", "brew"]},
    "wine": {"emoji": "🍷", "alternatives": ["red", "beverage"]},
    "ice_cream": {"emoji": "🍦", "alternatives": ["dessert", "frozen"]},
    "popcorn": {"emoji": "🍿", "alternatives": ["snack", "movie"]},
    "basketball": {"emoji": "🏀", "alternatives": ["sport", "hoop"]},
    "soccer": {"emoji": "⚽", "alternatives": ["football", "kick"]},
    "baseball": {"emoji": "⚾", "alternatives": ["bat", "game"]},
    "football": {"emoji": "🏈", "alternatives": ["gridiron", "tackle"]},
    "guitar": {"emoji": "🎸", "alternatives": ["music", "string"]},
    "piano": {"emoji": "🎹", "alternatives": ["keys", "musical"]},
    "music": {"emoji": "🎶", "alternatives": ["melody", "tune"]},
    "dance": {"emoji": "💃", "alternatives": ["celebrate", "party"]},
    "run": {"emoji": "🏃", "alternatives": ["jog", "sprint"]},
    "swim": {"emoji": "🏊", "alternatives": ["dive", "water"]},
    "bike": {"emoji": "🚴", "alternatives": ["cycling", "bicycle"]},
    "car": {"emoji": "🚗", "alternatives": ["vehicle", "automobile"]},
    "bus": {"emoji": "🚌", "alternatives": ["transport", "public"]},
    "train": {"emoji": "🚆", "alternatives": ["rail", "commute"]},
    "airplane": {"emoji": "✈️", "alternatives": ["flight", "travel"]},
    "rocket": {"emoji": "🚀", "alternatives": ["launch", "space"]},
    "star_struck": {"emoji": "🤩", "alternatives": ["excited", "amazed"]},
    "exploding_head": {"emoji": "🤯", "alternatives": ["mind blown", "shock"]},
    "face_with_thermometer": {"emoji": "🤒", "alternatives": ["sick", "illness"]},
    "face_with_head_bandage": {"emoji": "🤕", "alternatives": ["hurt", "injury"]},
    "nauseated_face": {"emoji": "🤢", "alternatives": ["sick", "ill"]},
    "vomiting_face": {"emoji": "🤮", "alternatives": ["nauseous", "disgusted"]},
    "sneezing_face": {"emoji": "🤧", "alternatives": ["sneeze", "allergy"]},
    "hot_face": {"emoji": "🥵", "alternatives": ["heat", "sweating"]},
    "cold_face": {"emoji": "🥶", "alternatives": ["chill", "frost"]},
    "woozy_face": {"emoji": "🥴", "alternatives": ["dizzy", "drunk"]},
    "partying_face": {"emoji": "🥳", "alternatives": ["celebration", "fun"]},
    "smiling_face_with_horns": {"emoji": "😈", "alternatives": ["devilish", "sly"]},
    "ghost": {"emoji": "👻", "alternatives": ["spooky", "haunt"]},
    "alien": {"emoji": "👽", "alternatives": ["extraterrestrial", "space"]},
    "robot": {"emoji": "🤖", "alternatives": ["android", "mechanical"]},
    "sun": {"emoji": "☀️", "alternatives": ["day", "bright"]},
    "moon": {"emoji": "🌙", "alternatives": ["night", "lunar"]},
    "cloud": {"emoji": "☁️", "alternatives": ["weather", "overcast"]},
    "rain": {"emoji": "🌧️", "alternatives": ["wet", "storm"]},
    "snow": {"emoji": "❄️", "alternatives": ["winter", "cold"]},
    "lightning": {"emoji": "⚡", "alternatives": ["storm", "electric"]},
    "rainbow": {"emoji": "🌈", "alternatives": ["colorful", "pride"]},
    "umbrella": {"emoji": "☔", "alternatives": ["rain", "protection"]},
    "leaf": {"emoji": "🍃", "alternatives": ["nature", "green"]},
    "tree": {"emoji": "🌳", "alternatives": ["wood", "forest"]},
    "flower": {"emoji": "🌸", "alternatives": ["blossom", "floral"]},
    "cactus": {"emoji": "🌵", "alternatives": ["desert", "plant"]},
    "earth": {"emoji": "🌍", "alternatives": ["globe", "planet"]},
    "mooncake": {"emoji": "🥮", "alternatives": ["festival", "dessert"]},
    "taco": {"emoji": "🌮", "alternatives": ["mexican", "food"]},
    "bento": {"emoji": "🍱", "alternatives": ["meal", "lunch"]},
    "sushi": {"emoji": "🍣", "alternatives": ["japanese", "food"]},
    "dumpling": {"emoji": "🥟", "alternatives": ["asian", "snack"]},
    "chocolate": {"emoji": "🍫", "alternatives": ["sweet", "dessert"]},
    "candy": {"emoji": "🍬", "alternatives": ["sweets", "treat"]},
    "lollipop": {"emoji": "🍭", "alternatives": ["sucker", "candy"]},
    "balloon": {"emoji": "🎈", "alternatives": ["party", "celebration"]},
    "gift": {"emoji": "🎁", "alternatives": ["present", "surprise"]},
    "party_popper": {"emoji": "🎉", "alternatives": ["celebrate", "festive"]},
    "confetti_ball": {"emoji": "🎊", "alternatives": ["celebration", "party"]},
    "sparkles": {"emoji": "✨", "alternatives": ["magic", "shine"]},
    "sparkler": {"emoji": "🎇", "alternatives": ["fireworks", "celebration"]},
    "fireworks": {"emoji": "🎆", "alternatives": ["explosion", "celebration"]},
    "scarf": {"emoji": "🧣", "alternatives": ["winter", "clothing"]},
    "hat": {"emoji": "🎩", "alternatives": ["formal", "clothing"]},
    "socks": {"emoji": "🧦", "alternatives": ["footwear", "clothing"]},
    "shoes": {"emoji": "👟", "alternatives": ["footwear", "sneakers"]},
    "dress": {"emoji": "👗", "alternatives": ["clothing", "fashion"]},
    "jacket": {"emoji": "🧥", "alternatives": ["outerwear", "clothing"]},
    "sunglasses": {"emoji": "🕶️", "alternatives": ["accessory", "cool"]},
    "purse": {"emoji": "👜", "alternatives": ["bag", "accessory"]},
    "wallet": {"emoji": "👛", "alternatives": ["money", "accessory"]},
    "watch": {"emoji": "⌚", "alternatives": ["timepiece", "accessory"]},
    "ring": {"emoji": "💍", "alternatives": ["jewelry", "marriage"]},
    "crown": {"emoji": "👑", "alternatives": ["royalty", "king"]},
    "mushroom": {"emoji": "🍄", "alternatives": ["fungus", "nature"]},
    "candy_cane": {"emoji": "🍭", "alternatives": ["holiday", "sweet"]},
    "cheese": {"emoji": "🧀", "alternatives": ["dairy", "food"]},
    "egg": {"emoji": "🥚", "alternatives": ["breakfast", "food"]},
    "hot_dog": {"emoji": "🌭", "alternatives": ["snack", "food"]},
    "cucumber": {"emoji": "🥒", "alternatives": ["vegetable", "food"]},
    "banana": {"emoji": "🍌", "alternatives": ["fruit", "snack"]},
    "apple": {"emoji": "🍏", "alternatives": ["fruit", "healthy"]},
    "grapes": {"emoji": "🍇", "alternatives": ["fruit", "bunch"]},
    "strawberry": {"emoji": "🍓", "alternatives": ["fruit", "berry"]},
    "watermelon": {"emoji": "🍉", "alternatives": ["fruit", "summer"]},
    "peach": {"emoji": "🍑", "alternatives": ["fruit", "soft"]},
    "pineapple": {"emoji": "🍍", "alternatives": ["fruit", "tropical"]},
    "lemon": {"emoji": "🍋", "alternatives": ["fruit", "sour"]},
    "kiwi": {"emoji": "🥝", "alternatives": ["fruit", "exotic"]},
    "carrot": {"emoji": "🥕", "alternatives": ["vegetable", "healthy"]},
    "eggplant": {"emoji": "🍆", "alternatives": ["vegetable", "food"]},
    "potato": {"emoji": "🥔", "alternatives": ["vegetable", "starch"]},
    "tomato": {"emoji": "🍅", "alternatives": ["fruit", "vegetable"]},
    "nuts": {"emoji": "🥜", "alternatives": ["snack", "healthy"]},
    "bread": {"emoji": "🍞", "alternatives": ["food", "carbohydrate"]},
    "tropical_drink": {"emoji": "🍹", "alternatives": ["cocktail", "beverage"]},
    "cocktail": {"emoji": "🍸", "alternatives": ["drink", "beverage"]},
    "milk": {"emoji": "🥛", "alternatives": ["dairy", "drink"]},
    "coconut": {"emoji": "🥥", "alternatives": ["fruit", "tropical"]},
    "cheers": {"emoji": "🥂", "alternatives": ["toast", "celebration"]},
    "face_with_hand_over_mouth": {"emoji": "🤭", "alternatives": ["surprise", "gossip"]},
    "face_with_monocle": {"emoji": "🧐", "alternatives": ["curious", "detective"]},
    "face_with_rolling_eyes": {"emoji": "🙄", "alternatives": ["sarcasm", "disbelief"]},
    "smiling_face_with_smiling_eyes": {"emoji": "😊", "alternatives": ["happy", "content"]},
    "smiling_face_with_heart_eyes": {"emoji": "😍", "alternatives": ["infatuated", "love"]},
    "hugging_face": {"emoji": "🤗", "alternatives": ["affection", "comfort"]},
    "kissing_heart": {"emoji": "😘", "alternatives": ["love", "smooch"]},
    "smirking_face": {"emoji": "😏", "alternatives": ["sly", "playful"]},
    "unamused_face": {"emoji": "😒", "alternatives": ["displeased", "meh"]},
    "grimacing_face": {"emoji": "😬", "alternatives": ["awkward", "nervous"]},
    "face_screaming_in_fear": {"emoji": "😱", "alternatives": ["fear", "panic"]},
    "sweat_smile": {"emoji": "😅", "alternatives": ["nervous", "relief"]},
    "upside_down_face": {"emoji": "🙃", "alternatives": ["silly", "confused"]},
    "zipper_mouth_face": {"emoji": "🤐", "alternatives": ["secret", "silent"]},
    "money_mouth_face": {"emoji": "🤑", "alternatives": ["rich", "wealthy"]},
    "shushing_face": {"emoji": "🤫", "alternatives": ["quiet", "hush"]},
    "face_with_symbols_on_mouth": {"emoji": "🤬", "alternatives": ["angry", "swear"]},
    "thinking_face": {"emoji": "🤔", "alternatives": ["pondering", "considering"]},
    "face_with_diagonal_mouth": {"emoji": "😬", "alternatives": ["grimace", "awkward"]},
    "man_shrugging": {"emoji": "🤷‍♂️", "alternatives": ["shrug", "uncertain"]},
    "woman_shrugging": {"emoji": "🤷‍♀️", "alternatives": ["shrug", "uncertain"]},
    "man_facepalming": {"emoji": "🤦‍♂️", "alternatives": ["facepalm", "embarrassed"]},
    "woman_facepalming": {"emoji": "🤦‍♀️", "alternatives": ["facepalm", "embarrassed"]},
    "man_dancing": {"emoji": "🕺", "alternatives": ["dance", "celebrate"]},
    "woman_dancing": {"emoji": "💃", "alternatives": ["dance", "celebrate"]},
    "man_and_woman_holding_hands": {"emoji": "👫", "alternatives": ["couple", "together"]},
    "two_women_holding_hands": {"emoji": "👭", "alternatives": ["friends", "support"]},
    "two_men_holding_hands": {"emoji": "👬", "alternatives": ["friends", "support"]},
    "family": {"emoji": "👪", "alternatives": ["household", "group"]},
    "couple": {"emoji": "💑", "alternatives": ["love", "relationship"]},
    "couple_with_heart": {"emoji": "💏", "alternatives": ["romance", "intimacy"]},
    "baby": {"emoji": "👶", "alternatives": ["infant", "newborn"]},
    "child": {"emoji": "👧", "alternatives": ["kid", "girl"]},
    "adult": {"emoji": "👩", "alternatives": ["woman", "female"]},
    "older_adult": {"emoji": "👵", "alternatives": ["elder", "senior"]},
    "man": {"emoji": "👨", "alternatives": ["male", "guy", "person"]},
    "woman": {"emoji": "👩", "alternatives": ["female", "lady"]},
    "boy": {"emoji": "👦", "alternatives": ["kid", "young boy"]},
    "girl": {"emoji": "👧", "alternatives": ["kid", "young girl"]},
    "grandfather": {"emoji": "👴", "alternatives": ["elder", "grandpa"]},
    "grandmother": {"emoji": "👵", "alternatives": ["elder", "grandma"]},
    "person_in_lotus_position": {"emoji": "🧘", "alternatives": ["meditating", "calm"]},
    "person_with_ball": {"emoji": "⛹️", "alternatives": ["basketball", "sport"]},
    "person_biking": {"emoji": "🚴", "alternatives": ["cycling", "bike"]},
    "person_running": {"emoji": "🏃", "alternatives": ["jogging", "exercise"]},
    "person_swimming": {"emoji": "🏊", "alternatives": ["swims", "swim"]},
    "person_golfing": {"emoji": "🏌️", "alternatives": ["golf", "sport"]},
    "person_with_umbrella": {"emoji": "🌂", "alternatives": ["rain", "weather"]},
    "man_in_tuxedo": {"emoji": "🤵", "alternatives": ["formal", "groom"]},
    "woman_in_tuxedo": {"emoji": "👰", "alternatives": ["bride", "formal"]},
    "water": {"emoji": "💦", "alternatives": ["wet"]},
     "home": {"emoji": "🏡", "alternatives": ["house", "dwelling"]},
    "school": {"emoji": "🏫", "alternatives": ["education", "learning"]},
    "office": {"emoji": "🏢", "alternatives": ["work", "business"]},
    "park": {"emoji": "🏞️", "alternatives": ["nature", "recreation"]},
    "beach": {"emoji": "🏖️", "alternatives": ["sea", "vacation"]},
    "city": {"emoji": "🏙️", "alternatives": ["urban", "metropolis"]},
    "restaurant": {"emoji": "🍽️", "alternatives": ["dining", "food"]},
    "hospital": {"emoji": "🏥", "alternatives": ["health", "care"]},
    "library": {"emoji": "📚", "alternatives": ["books", "reading"]},
    "gym": {"emoji": "🏋️", "alternatives": ["exercise", "fitness"]},
    "running": {"emoji": "🏃", "alternatives": ["going", "jogging", "sprinting"]},
    "walking": {"emoji": "🚶", "alternatives": ["strolling", "moving"]},
    "jumping": {"emoji": "🤸", "alternatives": ["leaping", "bounding"]},
    "swimming": {"emoji": "🏊", "alternatives": ["diving", "floating"]},
    "driving": {"emoji": "🚗", "alternatives": ["traveling", "commuting"]},
    "flying": {"emoji": "✈️", "alternatives": ["traveling", "soaring"]},
    "shopping": {"emoji": "🛍️", "alternatives": ["buying", "purchasing"]},
    "cooking": {"emoji": "👩‍🍳", "alternatives": ["baking", "preparing"]},
}


def adjust_emoji_based_on_sentiment(emoji, sentiment):
    if sentiment['compound'] >= 0.05:
        return emoji + " 😊"
    elif sentiment['compound'] <= -0.05:
        return emoji + " 😢"
    else:
        return emoji

def emojify(text, sentiment):
    words = text.split()
    output = []
    for word in words:
        found_emoji = False
        for key, value in emojis.items():
            if word.lower() == key or word in value['alternatives']:
                emoji = adjust_emoji_based_on_sentiment(value['emoji'], sentiment)
                alternatives = [adjust_emoji_based_on_sentiment(alt, sentiment) for alt in value['alternatives']]
                output.append({"word": word, "emoji": emoji, "alternatives": alternatives})
                found_emoji = True
                break
        if not found_emoji:
            output.append({"word": word, "emoji": word, "alternatives": []})
    return output

if __name__ == "__main__":
    input_text = sys.argv[1]
    sentiment = json.loads(sys.argv[2])
    emojified_text = emojify(input_text, sentiment)
    print(json.dumps(emojified_text))