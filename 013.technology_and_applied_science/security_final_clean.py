
import re

file_path = "/home/0xjb/Documents/my-knowledge-base/securityplus-questions.md"

with open(file_path, "r") as f:
    content = f.read()

# Pattern to find each question block
# Starts with "Question:" followed by a number
sections = re.split(r"(Question:\s*\d+)", content)

new_content = sections[0] # Intro if any

for i in range(1, len(sections), 2):
    header_raw = sections[i]
    body = sections[i+1]
    
    # 1. Clean Header
    q_num = re.search(r"(\d+)", header_raw).group(1)
    new_header = f"Question {q_num}"

    # 2. Extract Existing Explanation
    # Pattern: Look for Explanation: followed by anything until next question
    exp_match = re.search(r"Explanation:\s*(.*)", body, re.DOTALL)
    existing_explanation = exp_match.group(1).strip() if exp_match else ""
    
    # Remove Reference block and Explanation block from body for processing
    body_no_exp = re.split(r"Explanation:|Reference:", body)[0]

    # 3. Normalize Body for text
    # We want to replace newlines inside the question text but keep them for options
    clean_body = re.sub(r"\s+", " ", body_no_exp)

    # 4. Extract Options
    options_map = {}
    for m in re.finditer(r" ([A-F])\. (.*?)(?= [A-F]|$| Answer\(s\):)", clean_body):
        letter = m.group(1)
        text = m.group(2).strip()
        if letter not in options_map:
            options_map[letter] = text

    # 5. Extract Question Text
    q_text_match = re.search(r"(.*?)(?= [A-F]|$| Answer\(s\):)", clean_body)
    question_text = q_text_match.group(1).strip() if q_text_match else ""

    # 6. Extract Answer Letters
    ans_match = re.search(r"Answer\(s\): (.*)", clean_body)
    unique_letters = []
    if ans_match:
        ans_part = ans_match.group(1)
        raw_letters = re.sub(r"[\s,]+", "", ans_part)
        for char in raw_letters:
            if char in "ABCDEF" and char in options_map and char not in unique_letters:
                unique_letters.append(char)

    # 7. Format Output
    formatted_options = [f"  {L}. {options_map[L]}" for L in sorted(options_map.keys())]
    
    ans_text_parts = [f"{L}. {options_map[L]}" for L in unique_letters]
    new_ans_line = "Answer(s): " + ", ".join(ans_text_parts)
    
    final_block = f"\n{new_header}\n\n{question_text}\n\n"
    if formatted_options:
        final_block += "\n".join(formatted_options) + "\n\n"
    
    final_block += f"{new_ans_line}\n\n"
    final_block += f"Explanation: {existing_explanation}\n"
    
    new_content += final_block

with open(file_path, "w") as f:
    f.write(new_content.strip())
