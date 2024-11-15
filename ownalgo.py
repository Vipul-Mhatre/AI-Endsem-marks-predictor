import difflib  

def calculate_similarity(user_answer, ideal_answer):
    similarity_score = difflib.SequenceMatcher(None, user_answer.lower(), ideal_answer.lower()).ratio()
    return round(similarity_score * 10)  

def get_module_score(preparation_score, answer_score):
    return (preparation_score + answer_score) / 2

def calculate_final_score(module_scores, weights):
    total_weighted_score = sum(score * weight for score, weight in zip(module_scores, weights))
    total_weight = sum(weights)
    final_score = (total_weighted_score / total_weight) * 65
    return min(final_score, 65) 

def ask_module_questions(module_number):
    questions = {
        1: [
            ("What is Artificial Intelligence?", "AI is the simulation of human intelligence in machines."),
            ("Name any two subfields of AI.", "Machine Learning, Natural Language Processing."),
        ],
        2: [
            ("What is the difference between BFS and DFS?", "BFS explores all nodes at present depth level, while DFS explores as far as possible down one branch."),
            ("Explain A* search algorithm.", "A* search uses both the cost to reach the node and the heuristic to estimate the cost to reach the goal."),
        ],
        3: [
            ("What is Forward Chaining in First-Order Logic (FOL)?", "Forward chaining starts from known facts and applies inference rules to derive new facts."),
            ("Explain Unification in FOL.", "Unification is the process of making two logical expressions identical by substituting variables."),
        ],
        4: [
            ("What is STRIPS in AI Planning?", "STRIPS is a formal language used to describe actions in AI planning, focusing on preconditions and effects."),
            ("Explain Goal Stack Planning.", "Goal Stack Planning uses a stack to manage subgoals and solves them in a last-in, first-out order."),
        ],
        5: [
            ("What is the architecture of an Expert System?", "It typically includes a knowledge base, inference engine, and user interface."),
            ("What is the role of the knowledge base in Expert Systems?", "It stores the facts and rules the system uses to infer solutions to problems."),
        ],
        6: [
            ("What are Generative Adversarial Networks (GANs)?", "GANs consist of two neural networks that compete to generate realistic data."),
            ("What is the difference between GANs and VAEs?", "GANs use a generator and discriminator in competition, while VAEs use an encoder-decoder structure for data generation."),
        ],
    }
    return questions.get(module_number, [])

def get_valid_preparation_score(module_number):
    while True:
        try:
            preparation_score = int(input(f"Enter preparation score (1-10) for Module {module_number} ({get_module_name(module_number)}): "))
            if 1 <= preparation_score <= 10:
                return preparation_score
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_module_name(module_number):
    module_names = {
        1: "Introduction to Artificial Intelligence",
        2: "Problem Solving: Search Algorithms",
        3: "Knowledge and Reasoning",
        4: "Planning",
        5: "Expert Systems",
        6: "Generative AI"
    }
    return module_names.get(module_number, "Unknown Module")

def main():
    weights = [1, 2, 1.5, 1, 0.5, 0.5]  
    module_scores = [] 

    for i in range(1, 7):  
        module_name = get_module_name(i) 
        print(f"\nModule {i}: {module_name}")
        
        preparation_score = get_valid_preparation_score(i)
        
        questions = ask_module_questions(i)
        total_answer_score = 0
        
        for question, ideal_answer in questions:
            print(f"Question: {question}")
            user_answer = input("Your answer: ")
            answer_score = calculate_similarity(user_answer, ideal_answer)
            print(f"Similarity score: {answer_score}/10")
            total_answer_score += answer_score
        
        average_answer_score = total_answer_score / len(questions)
        
        module_score = get_module_score(preparation_score, average_answer_score)
        print(f"Module {i} ({module_name}) score: {module_score:.2f}")
        
        module_scores.append(module_score)

    predicted_score = calculate_final_score(module_scores, weights)
    print(f"\nPredicted score in Engineering End Semester Exam: {predicted_score:.2f} out of 65")

if __name__ == "__main__":
    main()