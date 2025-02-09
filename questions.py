import random

questions = [
    # Literature
    {"question": "Who wrote 'The Great Gatsby'?", "answer": "F Scott Fitzgerald"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "Author of 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "Who wrote 'The Canterbury Tales'?", "answer": "Chaucer"},
    
    # History
    {"question": "Year American Civil War ended?", "answer": "1865"},
    {"question": "First African American MLB player?", "answer": "Jackie Robinson"},
    {"question": "Year of Moon Landing?", "answer": "1969"},
    {"question": "Who wrote the Declaration of Independence?", "answer": "Thomas Jefferson"},
    
    # Math
    {"question": "Derivative of e^x?", "answer": "e^x"},
    {"question": "What's log base e called?", "answer": "ln"},
    {"question": "Square root of 144?", "answer": "12"},
    {"question": "sin^2(x) + cos^2(x) = ?", "answer": "1"},
    
    # Art
    {"question": "Who painted Starry Night?", "answer": "Van Gogh"},
    {"question": "Who painted The Scream?", "answer": "Munch"},
    {"question": "Who sculpted David?", "answer": "Michelangelo"},
    
    # Science
    {"question": "Symbol for Gold?", "answer": "Au"},
    {"question": "Closest planet to Sun?", "answer": "Mercury"},
    {"question": "Human body has how many chromosomes?", "answer": "46"}
]

def get_random_question():
    return random.choice(questions)
