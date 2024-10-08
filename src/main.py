import os
import shutil
import pathlib
from block_markdown import markdown_to_html_node


def copy_r(source, dest):
    shutil.rmtree(dest, ignore_errors=True)
    os.mkdir(dest)
    print(f"Deleted Content in Directory: {dest}")
    copy_r_helper(source, dest)

def copy_r_helper(source, dest):
    for d in os.listdir(source):
        if os.path.isfile(f"{source}/{d}"):
            shutil.copy(f"{source}/{d}", dest)
            print(f"Copied {d} to {dest}")
        else:
            os.mkdir(f"{dest}/{d}")
            copy_r_helper(f"{source}/{d}", f"{dest}/{d}")


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[0: 2] == "# ":
            title = line[2:]
            title = title.strip()
            return title
    raise Exception("No Title Found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = None
    template_content = None
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        template_content = f.read()
    
    if not markdown_content or not template_content:
        raise Exception("File reading Error")

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    page = template_content.replace('{{ Title }}', title)
    page = page.replace('{{ Content }}', html_content)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    with open(dest_path, 'w') as f:
        f.write(page)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for d in os.listdir(dir_path_content):
        if d[-2:] == 'md':
            source_file_path = pathlib.Path(f"{dir_path_content}/{d}")
            dest_file_path = pathlib.Path(f"{dest_dir_path}/{d[:-2]}html")
            generate_page(source_file_path, template_path, dest_file_path)
        else:
            generate_pages_recursive(f"{dir_path_content}/{d}", template_path, f"{dest_dir_path}/{d}")


def main():
	copy_r("/home/ron/workspace/github.com/Ron5474/siteGen2/static", "/home/ron/workspace/github.com/Ron5474/siteGen2/public")
	generate_pages_recursive("/home/ron/workspace/github.com/Ron5474/siteGen2/content", "/home/ron/workspace/github.com/Ron5474/siteGen2/template.html", "/home/ron/workspace/github.com/Ron5474/siteGen2/public")




if __name__ == "__main__":
    main()
