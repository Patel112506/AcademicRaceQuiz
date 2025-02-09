import random

questions = [
    # Literature
    {"question": "Who wrote 'The Great Gatsby'?", "answer": "F Scott Fitzgerald"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "Author of 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "Who wrote 'The Canterbury Tales'?", "answer": "Chaucer"},
    {"question": "Author of 'The Scarlet Letter'?", "answer": "Hawthorne"},
    {"question": "Who wrote 'The Catcher in the Rye'?", "answer": "Salinger"},
    {"question": "Author of 'The Road'?", "answer": "McCarthy"},
    {"question": "Who wrote 'Beloved'?", "answer": "Morrison"},
    {"question": "Author of 'Their Eyes Were Watching God'?", "answer": "Hurston"},
    {"question": "Who wrote 'One Hundred Years of Solitude'?", "answer": "Marquez"},

    # World Literature
    {"question": "Author of 'Crime and Punishment'?", "answer": "Dostoevsky"},
    {"question": "Who wrote 'Don Quixote'?", "answer": "Cervantes"},
    {"question": "Author of 'The Metamorphosis'?", "answer": "Kafka"},
    {"question": "Who wrote 'The Odyssey'?", "answer": "Homer"},
    {"question": "Author of 'Les Misérables'?", "answer": "Hugo"},

    # History
    {"question": "Year American Civil War ended?", "answer": "1865"},
    {"question": "First African American MLB player?", "answer": "Jackie Robinson"},
    {"question": "Year of Moon Landing?", "answer": "1969"},
    {"question": "Who wrote the Declaration of Independence?", "answer": "Thomas Jefferson"},
    {"question": "Year World War 2 ended?", "answer": "1945"},
    {"question": "First US President?", "answer": "Washington"},
    {"question": "Year of Pearl Harbor attack?", "answer": "1941"},
    {"question": "Which amendment ended slavery?", "answer": "13"},
    {"question": "Year Berlin Wall fell?", "answer": "1989"},
    {"question": "Cuban Missile Crisis year?", "answer": "1962"},

    # AP US History
    {"question": "Year Louisiana Purchase?", "answer": "1803"},
    {"question": "Author of Common Sense?", "answer": "Paine"},
    {"question": "First Secretary of Treasury?", "answer": "Hamilton"},
    {"question": "Year of Stock Market Crash?", "answer": "1929"},
    {"question": "Manhattan Project leader?", "answer": "Oppenheimer"},

    # AP World History
    {"question": "First Emperor of China?", "answer": "Qin"},
    {"question": "Who founded the Mongol Empire?", "answer": "Genghis Khan"},
    {"question": "Fall of Roman Empire year?", "answer": "476"},
    {"question": "Who discovered America in 1492?", "answer": "Columbus"},
    {"question": "French Revolution start year?", "answer": "1789"},

    # AP Government
    {"question": "How many Supreme Court Justices?", "answer": "9"},
    {"question": "How many amendments?", "answer": "27"},
    {"question": "Which amendment protects speech?", "answer": "1"},
    {"question": "How many senators per state?", "answer": "2"},
    {"question": "Electoral votes needed to win?", "answer": "270"},

    # Math - AP Calculus
    {"question": "Derivative of e^x?", "answer": "e^x"},
    {"question": "Derivative of ln(x)?", "answer": "1/x"},
    {"question": "Derivative of sin(x)?", "answer": "cos(x)"},
    {"question": "Integral of 1/x?", "answer": "ln|x|"},
    {"question": "Derivative of x^2?", "answer": "2x"},

    # Algebra 2
    {"question": "What's log base e called?", "answer": "ln"},
    {"question": "Square root of 144?", "answer": "12"},
    {"question": "sin^2(x) + cos^2(x) = ?", "answer": "1"},
    {"question": "Cube root of 27?", "answer": "3"},
    {"question": "i^2 = ?", "answer": "-1"},
    {"question": "log(1) = ?", "answer": "0"},
    {"question": "2^3 * 2^4 = 2^?", "answer": "7"},

    # Art History
    {"question": "Who painted Starry Night?", "answer": "Van Gogh"},
    {"question": "Who painted The Scream?", "answer": "Munch"},
    {"question": "Who sculpted David?", "answer": "Michelangelo"},
    {"question": "Who painted Guernica?", "answer": "Picasso"},
    {"question": "Who painted The Last Supper?", "answer": "Da Vinci"},
    {"question": "Who painted American Gothic?", "answer": "Wood"},
    {"question": "Who painted The Persistence of Memory?", "answer": "Dali"},

    # Science
    {"question": "Symbol for Gold?", "answer": "Au"},
    {"question": "Closest planet to Sun?", "answer": "Mercury"},
    {"question": "Number of chromosomes in humans?", "answer": "46"},
    {"question": "Element symbol for Silver?", "answer": "Ag"},
    {"question": "Atomic number of Carbon?", "answer": "6"},
    {"question": "Symbol for Potassium?", "answer": "K"},
    {"question": "Largest planet?", "answer": "Jupiter"},
    {"question": "Human body temperature (F)?", "answer": "98.6"},
    {"question": "Speed of light (x10^8 m/s)?", "answer": "3"},
    {"question": "Number of bones in human body?", "answer": "206"}
]

def get_random_question():
    return random.choice(questions)