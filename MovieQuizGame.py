# Function to ask a question and return if the answer is correct
def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if 1 <= user_answer <= len(options):
                break
            else:
                print("Please select a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if options[user_answer - 1] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}\n")
        return False

# Main function to run the quiz
def run_quiz():
    questions = [
        {
            "question": "Which movie won the Best Film award at the 2023 Filmfare Awards?",
            "options": ["Gangubai Kathiawadi", "RRR", "Brahmastra", "The Kashmir Files"],
            "correct_answer": "Gangubai Kathiawadi"
        },
        {
            "question": "Which actor played the lead role in the movie 'Shershaah'?",
            "options": ["Sidharth Malhotra", "Ranveer Singh", "Vicky Kaushal", "Ayushmann Khurrana"],
            "correct_answer": "Sidharth Malhotra"
        },
        {
            "question": "Which movie features the popular song 'Naatu Naatu'?",
            "options": ["Pushpa: The Rise", "KGF: Chapter 2", "RRR", "Liger"],
            "correct_answer": "RRR"
        },
        {
            "question": "Which actress played the role of Gangubai in the movie 'Gangubai Kathiawadi'?",
            "options": ["Alia Bhatt", "Deepika Padukone", "Kangana Ranaut", "Kriti Sanon"],
            "correct_answer": "Alia Bhatt"
        },
        {
            "question": "Which Bollywood movie is based on the life of cricketer Kapil Dev?",
            "options": ["83", "MS Dhoni: The Untold Story", "Dangal", "Chak De! India"],
            "correct_answer": "83"
        },
        {
            "question": "Which actor starred in the movie 'Brahmastra: Part One – Shiva'?",
            "options": ["Ranbir Kapoor", "Shah Rukh Khan", "Hrithik Roshan", "Akshay Kumar"],
            "correct_answer": "Ranbir Kapoor"
        },
        {
            "question": "Who directed the movie 'Pathaan'?",
            "options": ["Siddharth Anand", "Rohit Shetty", "Rajkumar Hirani", "Karan Johar"],
            "correct_answer": "Siddharth Anand"
        },
        {
            "question": "Which 2022 Bollywood movie is based on a true story involving a plane hijacking?",
            "options": ["Runway 34", "Airlift", "Bell Bottom", "Mission Majnu"],
            "correct_answer": "Runway 34"
        },
        {
            "question": "Which movie won the Best Picture award at the 2022 IIFA Awards?",
            "options": ["Shershaah", "Mimi", "Sooryavanshi", "Tanhaji"],
            "correct_answer": "Shershaah"
        },
        {
            "question": "Which Bollywood actor played a double role in the movie 'Cirkus' (2022)?",
            "options": ["Ranveer Singh", "Varun Dhawan", "Tiger Shroff", "Kartik Aaryan"],
            "correct_answer": "Ranveer Singh"
        }
    ]
    
    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1

    print(f"Quiz Complete! Your final score is: {score} out of {len(questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()