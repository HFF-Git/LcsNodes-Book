
import re
import sys

def markdown_to_latex(markdown_text):
    latex_text = markdown_text

    # Convert headers
    latex_text = re.sub(r'#### (.*)', r'\\subsection{\1}', latex_text)
    latex_text = re.sub(r'### (.*)', r'\\section{\1}', latex_text)
    latex_text = re.sub(r'## (.*)', r'\\chapterr{\1}', latex_text)

    # Convert bold and italics
    latex_text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', latex_text)
    latex_text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', latex_text)

    # Convert lists
    latex_text = re.sub(r'^\s*-\s+(.*)', r'\\item \1', latex_text, flags=re.MULTILINE)
    latex_text = re.sub(r'((\\item .*\n)+)', r'\\begin{itemize}\n\1\\end{itemize}\n', latex_text, flags=re.MULTILINE)

    # Convert links
    latex_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\\href{\2}{\1}', latex_text)

    # Convert images
    latex_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'''
    \\begin{figure}[h]
    \\includegraphics[width=\\linewidth]{\2}
    \\caption{\1}
    \\end{figure}
    ''', latex_text)

    # Convert inline code
    latex_text = re.sub(r'`([^`]*)`', r'\\texttt{\1}', latex_text)

    # Convert code blocks
    latex_text = re.sub(r'```(.*?)\n(.*?)\n```', r'\\begin{verbatim}\2\\end{verbatim}', latex_text, flags=re.DOTALL)

    return latex_text

# Check if the file name is provided
if len(sys.argv) < 2:
    print("Usage: python script_name.py <file_name>")
    sys.exit(1)

file_path = sys.argv[1]

# Read the file
try:
    with open(file_path, 'r') as file:
        markdown_text = file.read()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

# Convert Markdown to LaTeX
latex_text = markdown_to_latex(markdown_text)

# Overwrite the file with the converted text
with open(file_path, 'w') as file:
    file.write(latex_text)

print(f"Conversion complete! Changes saved in {file_path}")