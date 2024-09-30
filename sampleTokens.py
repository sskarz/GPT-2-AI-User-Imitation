import re

def clean_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # Remove content within curly braces and the subsequent line
    text = re.sub(r'{[^}]*}\n[^\n]*\n', '', text)
    return text

def simple_tokenization(text):
    tokenized = []
    lines = text.strip().split('\n')
    for line in lines:
        # Ensure the line has the expected format
        if '] ' not in line:
            print(f"Skipping line due to missing '] ': {line}")
            continue
        
        timestamp, content = line.split('] ', 1)
        
        if ': ' not in content:
            print(f"Skipping line due to missing ': ': {line}")
            continue

        speaker, message = content.split(': ', 1)
        
        # Only tokenize "sskarz" messages for focused training
        if speaker == "sskarz":
            if len(speaker) > 4:
                speaker_token = speaker[:4] + '+ ' + speaker[4:]
            else:
                speaker_token = speaker

            tokenized.append(f"{speaker_token}: {message}")
    return tokenized

def save_to_file(content, file_path):
    with open(file_path, 'w') as file:
        for line in content:
            file.write(line + "\n")

data = clean_text_from_file('sample_input.txt')
tokenized_data = simple_tokenization(data)

print("=== Cleaned Data ===")
print(data)

print("\n=== Tokenized Data ===")
print(tokenized_data)

save_to_file(tokenized_data, 'tokenized_sample3.txt')
