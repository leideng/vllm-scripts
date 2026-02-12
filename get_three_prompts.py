import os


def get_three_prompts(context_length: int = 5000, 
                      question_index: int = 1, 
                      prompt_save_path: str = None)->str:
    book_path = "data/three/three.txt"
    question_path = f"data/three/questions/q{question_index}.txt"
    with open(book_path, "r", encoding="utf-8") as f:
        book = f.read()
    with open(question_path, "r", encoding="utf-8") as f:
        question = f.read()
    prompt = f"请阅读以下小说节选: {book[:context_length]}。\n\n请回答问题: {question}\n"
    
    print(prompt)
    
    if prompt_save_path is not None:
        with open(prompt_save_path, "w", encoding="utf-8") as f:
            f.write(prompt)
    
    return prompt

if __name__ == "__main__":
    context_length = 10000
    question_index = 1
    get_three_prompts(context_length, question_index, f"data/three/prompts/prompt_{context_length}_q{question_index}.txt")