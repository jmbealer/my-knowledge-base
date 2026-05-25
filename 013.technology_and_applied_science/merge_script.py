import re
import os

source_file = "test/00 CompTIA Network+ N10-009 Exam Objectives (Domains).md"
dest_file = "networkplus-wip.md"
output_file = "networkplus-wip.md" # Overwrite directly as requested/implied by "redo"

def parse_source(filepath):
    content_map = {}
    current_section = None
    current_content = []
    
    # Regex to match sections like "    - **1.1 Explain..."
    # Matches any leading whitespace, then dash, then whitespace, then **, then digits.digits
    section_regex = re.compile(r"^\s*-\s*\*\*(\d+\.\d+)\s+.*")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # Check for section header
                match = section_regex.match(line)
                if match:
                    # New section found
                    if current_section:
                        content_map[current_section] = current_content
                    
                    current_section = match.group(1)
                    current_content = []
                    
                    # Add the header line itself, formatted
                    # line = line.rstrip() + " <!-- newly added -->\n"
                    # current_content.append(line) 
                    # Actually, usually we don't want to duplicate the header if the dest already has it.
                    # But the instruction says "add the whole file".
                    # Let's add the content *under* the header.
                    pass
                else:
                    if current_section:
                        # Add comment to line if it's not empty
                        if line.strip():
                            # clean up line ending
                            line_content = line.rstrip()
                            new_line = f"{line_content} <!-- newly added -->\n"
                            current_content.append(new_line)
                        else:
                            current_content.append(line)
            
            # Add the last section
            if current_section:
                content_map[current_section] = current_content
                
    except FileNotFoundError:
        print(f"Error: Source file {filepath} not found.")
        return {}

    return content_map

def merge_files(dest_path, content_map, out_path):
    # Regex for destination headers: "### 1.1 Explain..."
    dest_header_regex = re.compile(r"^###\s+(\d+\.\d+)\s+.*")
    
    # Regex for main Domain headers: "## 1.0 ...", "## 2.0 ..." to detect end of a section
    dest_domain_regex = re.compile(r"^##\s+\d+\.0\s+.*")
    
    new_lines = []
    
    try:
        with open(dest_path, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()
            
            i = 0
            while i < len(lines):
                line = lines[i]
                new_lines.append(line)
                
                match = dest_header_regex.match(line)
                if match:
                    section_id = match.group(1)
                    
                    # We found a header (e.g. 1.1).
                    # We need to find where to insert the new content.
                    # Insertion point: End of this section.
                    # The end of this section is defined by:
                    # 1. The start of the next sub-objective (### X.X)
                    # 2. The start of the next domain (## X.0)
                    # 3. End of file
                    
                    # Look ahead to find the insertion point
                    j = i + 1
                    insertion_index = j
                    while j < len(lines):
                        next_line = lines[j]
                        if dest_header_regex.match(next_line) or dest_domain_regex.match(next_line):
                            # Found the start of next section, insertion point is here (before this line)
                            insertion_index = j
                            break
                        j += 1
                        insertion_index = j # if we reach EOF, index is valid
                    
                    # Now we append lines from i+1 to insertion_index to new_lines
                    # But we already appended lines[i].
                    # Wait, my logic above in the loop is: `new_lines.append(line)` then check match.
                    # So new_lines has the header.
                    # Now I need to add the *existing* content of this section to new_lines.
                    
                    # Let's iterate from i+1 up to insertion_index
                    k = i + 1
                    while k < insertion_index:
                        new_lines.append(lines[k])
                        k += 1
                    
                    # Now insert the NEW content from source map
                    if section_id in content_map:
                        # new_lines.append(f"\n<!-- Content from Exam Objectives for {section_id} -->\n")
                        new_lines.extend(content_map[section_id])
                        # new_lines.append(f"<!-- End content for {section_id} -->\n")
                    
                    # Update i to continue from insertion_index
                    # The outer loop does i+=1, so set i = insertion_index - 1
                    i = insertion_index - 1
                
                i += 1
        
        # Write back
        with open(out_path, 'w', encoding='utf-8') as f_out:
            f_out.writelines(new_lines)
            
    except FileNotFoundError:
        print(f"Error: Destination file {dest_path} not found.")

content_map = parse_source(source_file)
print(f"Parsed {len(content_map)} sections from source.")
merge_files(dest_file, content_map, output_file)
print(f"Merged content written to {output_file}")