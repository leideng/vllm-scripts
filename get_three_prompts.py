import os
import argparse


def get_three_prompt(context_length: int = 5000, 
                      question_index: int = 1, 
                      prompt_save_path: str = None)->str:
    book_path = "data/three/three.txt"
    question_path = f"data/three/questions/q{question_index}.txt"
    with open(book_path, "r", encoding="utf-8") as f:
        book = f.read()
    with open(question_path, "r", encoding="utf-8") as f:
        question = f.read()
    prompt = f"请阅读以下小说节选: {book[:context_length]}。\n\n请回答问题: {question}\n"
    
    #print(prompt)
    
    if prompt_save_path is not None:
        with open(prompt_save_path, "w", encoding="utf-8") as f:
            f.write(prompt)
    
    return prompt
    
if __name__ == "__main__":
    print("Getting three prompts...")
    parser = argparse.ArgumentParser()
    parser.add_argument("--context_length", type=int, default=1000, help="The length of the context to be read")
    parser.add_argument("--question_index", type=int, default=1, help="The index of the question to be answered")
    parser.add_argument("--prompt_save_path", type=str, default=None, help="The path to save the prompt, if not provided (None)," +
                                                                           "the prompt will not be saved; if provided as \"default\"," +
                                                                           "the prompt will be saved to the default path: " +
                                                                           "data/three/prompts/prompt_{context_length}_q{question_index}.txt")
    args = parser.parse_args()

    context_length = args.context_length
    question_index = args.question_index
    prompt_save_path = args.prompt_save_path

    if prompt_save_path is None:
        prompt  = get_three_prompt(context_length, question_index)
    elif prompt_save_path == "default":
        prompt_save_path = f"data/three/prompts/prompt_{context_length}_q{question_index}.txt"
        prompt = get_three_prompt(context_length, question_index, prompt_save_path)
    else:
        prompt = get_three_prompt(context_length, question_index, prompt_save_path)
    
    print(prompt)