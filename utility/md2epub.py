import subprocess
import os
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
