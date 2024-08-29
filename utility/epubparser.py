# pip install ebooklib==0.18
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re

def parse_epub(epub_file, 
               ix = 1,
               endquote = "我尊敬父亲，希望用自己的方式让他的名字继续存在。"):
    book = epub.read_epub(epub_file)
    for publisher in list(book.metadata.keys()):
        book_metadata = book.metadata[publisher]
        # print (book_metadata)

    # Extract content
    # len(book.items)
    # book.__dict__

    # Find all items with the "stylesheet" media type
    stylesheets = [item for item in book.get_items_of_type(ebooklib.ITEM_STYLE)]
    # Extract the filenames (relative paths) of the stylesheets
    # stylesheet_filenames = [item.file_name for item in stylesheets]
    css = "<style> \n"
    for stylesheet_item in stylesheets:
        css += stylesheet_item.content.decode('utf-8')
    css += "</style> \n"


    content = css + "" 
    for item in book.items[ix+1:]:
        # item.__dict__
        if item.file_name.endswith('.html'):
            pagecnt =  item.content.decode('utf-8')
            content += pagecnt
            if endquote in pagecnt :
                break
        print (ix)
        ix += 1
            
    return content,ix+1

def get_word_count(content):
    soup = BeautifulSoup(content, 'html.parser')
    section = soup.findAll('p', class_='calibre_1')
    word = ""
    for paragraph in section:
        word += paragraph.text
    return len(word)

if __name__ == "__main__":
    # Example usage
    epub_file = "../docs/ebook/你一年的8760小时.epub"
    content,endix = parse_epub(epub_file)
    # print(f"Content: {content}")
    # from IPython.core.display import HTML
    # HTML(content)
    # print(content)
    with open(f"doc_{endix}.html","w",encoding='utf-8') as f:
        f.write(content)

    get_word_count(content)