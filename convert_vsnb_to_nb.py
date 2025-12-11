#!/usr/bin/env python3
"""Convert VS Code Notebook (.vsnb) to Mathematica Notebook (.nb)"""

import json
import re

def escape_mathematica_string(s):
    """Escape special characters for Mathematica strings."""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '')
    s = s.replace('\t', '    ')  # Replace tabs with spaces
    return s

def determine_cell_style(md_content):
    """Determine the appropriate cell style based on markdown content."""
    stripped = md_content.strip()
    
    if stripped.startswith('---'):
        return "Text"
    elif stripped.startswith('#### '):
        return "Subsubsection"
    elif stripped.startswith('### '):
        return "Subsection"
    elif stripped.startswith('## '):
        return "Section"
    elif stripped.startswith('# '):
        return "Title"
    else:
        return "Text"

def clean_markdown_for_style(content, style):
    """Clean markdown headers based on cell style."""
    lines = content.split('\n')
    result_lines = []
    first_content_line = True
    
    for line in lines:
        clean_line = line
        if first_content_line and line.strip():
            first_content_line = False
            if style == "Title" and line.strip().startswith('# ') and not line.strip().startswith('## '):
                clean_line = re.sub(r'^#\s*', '', line.strip())
            elif style == "Section" and line.strip().startswith('## ') and not line.strip().startswith('### '):
                clean_line = re.sub(r'^##\s*', '', line.strip())
            elif style == "Subsection" and line.strip().startswith('### ') and not line.strip().startswith('#### '):
                clean_line = re.sub(r'^###\s*', '', line.strip())
            elif style == "Subsubsection" and line.strip().startswith('#### '):
                clean_line = re.sub(r'^####\s*', '', line.strip())
        result_lines.append(clean_line)
    
    return '\n'.join(result_lines)

def create_text_cell(content, style="Text"):
    """Create a Mathematica text cell from content."""
    clean_content = clean_markdown_for_style(content, style)
    escaped = escape_mathematica_string(clean_content)
    return f'Cell["{escaped}", "{style}"]'

def create_code_cell(code):
    """Create a Mathematica input cell from code."""
    escaped = escape_mathematica_string(code)
    # Use simple string format - Mathematica will parse it as input
    return f'Cell["{escaped}", "Input", CellLabel->""]'

def convert_vsnb_to_nb(input_path, output_path):
    """Convert a .vsnb file to a .nb file."""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        vsnb_data = json.load(f)
    
    cells = vsnb_data.get('cells', [])
    nb_cells = []
    
    for cell in cells:
        kind = cell.get('kind')
        value = cell.get('value', '')
        
        if kind == 1:  # Markdown cell
            style = determine_cell_style(value)
            nb_cell = create_text_cell(value, style)
            nb_cells.append(nb_cell)
            
        elif kind == 2:  # Code cell (wolfram)
            nb_cell = create_code_cell(value)
            nb_cells.append(nb_cell)
    
    cells_str = ",\n".join(nb_cells)
    
    notebook_content = f'''Notebook[{{
{cells_str}
}},
WindowSize->{{1200, 800}},
WindowMargins->{{Automatic, Automatic}},
FrontEndVersion->"14.0 for Mac OS X ARM (64-bit)",
StyleDefinitions->"Default.nb",
CellGrouping->Automatic
]'''
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(notebook_content)
    
    print(f"Converted {input_path} to {output_path}")
    print(f"Total cells converted: {len(nb_cells)}")

if __name__ == "__main__":
    input_file = "/Users/shlinky/Documents/MSBA/Storytelling/!!BDI_FINAL/Mag7_Spending.vsnb"
    output_file = "/Users/shlinky/Documents/MSBA/Storytelling/!!BDI_FINAL/Mag7_Spending.nb"
    convert_vsnb_to_nb(input_file, output_file)
