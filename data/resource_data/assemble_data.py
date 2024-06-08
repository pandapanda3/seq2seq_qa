import json

def read_and_process_json(file_path):
    # read the data from json
    with open(file_path, "r", encoding="utf-8") as f:
        dataset_data = json.load(f)
    
    # transform the data into T5
    t5_formatted_data = []
    for entry in dataset_data:
        context = entry['context']
        question = entry['question_by_gpt']
        answer = entry['answer_by_gpt']
        
        t5_input = f"question: {question} context: {context}"
        t5_formatted_data.append({
            "input_text": t5_input,
            "target_text": answer
        })
    
    return t5_formatted_data

if __name__ == '__main__':
    
    # declare the file path
    file_path = "dataset.json"
    
    # get data from json file
    t5_data = read_and_process_json(file_path)
    
    # print the data
    for item in t5_data:
        print(f"Input Text: {item['input_text']}")
        print(f"Target Text: {item['target_text']}")
        print("-" * 80)

