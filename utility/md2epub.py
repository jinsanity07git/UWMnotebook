import subprocess
import os
import re

os.environ["pandoc"] = "C:\Program Files\Pandoc\pandoc.exe"
# subprocess.run([os.environ["pandoc"],"--version"], check=True)
subprocess.run(["pandoc","--version"], check=True)





def create_epub(input_folder, output_file, cover_image=None):
    
    # Construct the pandoc command
    # https://github.com/jgm/pandoc/releases/tag/3.1.13
    pandoc_command = [
        os.environ["pandoc"] ,
        '-o', output_file,
        '--metadata', f'title={os.path.splitext(output_file)[0]}',
        '--table-of-contents'
    ]

    # Optionally add a cover image
    if cover_image:
        pandoc_command.extend(['--epub-cover-image', cover_image])

    # Add all markdown files from the input folder to the pandoc command
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith('.md'):
            print (filename)
            pandoc_command.append(os.path.join(input_folder, filename))

    print(pandoc_command )

    # Run the pandoc command
    try:
        subprocess.run(pandoc_command, check=True)
        print(f'Successfully created {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred while creating the EPUB: {e}')

if __name__ == "__main__":
    # Example usage:
    input_folder = 'C:/Users/Zjin/Desktop/demo/aow'
    output_file = 'The_Art_Of_War.epub'
    cover_image = f'{input_folder}/tnc.PNG'  # Optional

    # create_epub(input_folder, output_file, cover_image)s
    index_md = "digest_The_Art_Of_War.md"
    ixf = f"{input_folder}/{index_md}"
    with open(ixf,"r",encoding="utf8") as f:
        lines = f.readlines()

  
    
    def parse_outlinks(markdown_link = "* [始计第一](01_LayingPlans.md)"):
        
        # using re.search if the pattern does not start at the very beginning of the string
        match = re.search(r"\*\s+\[(.*?)\]\((.*?)\)", markdown_link)
        
        if match:
            text_inside_brackets, markdown_link_inside_parentheses = match.groups()
            result = (text_inside_brackets, markdown_link_inside_parentheses)
        else:
            result = "No match found"
        return result

    charpters = []
    for i,line in enumerate(lines):
        if "TOC\n" in line:
            print (i, line)
            for j,subl in enumerate(lines[i:]):
                if  "  * ["  in subl:
                    charpters.append(parse_outlinks( subl.strip("\n") ) )

    singlebody = lines.copy()
    cpf = f"{input_folder}/{charpters[0][1]}"
    with open(cpf,"r",encoding="utf8") as f:
        lines = f.readlines()
    headings = f"# {charpters[0][0]}"
    singlebody =  singlebody + [headings] +  lines

    with open("output_file.md","w",encoding="utf8") as f:
        f.writelines(singlebody)