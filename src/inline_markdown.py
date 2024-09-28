import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    regex = r'!\[(.*?)\]\((.*?)\)'
    return re.findall(regex, text)

def extract_markdown_links(text):
    regex = r"(?<!!)\[(.*?)\]\((.*?)\)"
    return re.findall(regex, text)


def split_nodes_images(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        regex_matches = extract_markdown_images(node.text)
        if len(regex_matches) == 0:
            continue
        split_nodes = []
        text = node.text
        for match in regex_matches:
            alt = match[0]
            link = match[1]
            
            sections = text.split(f"![{alt}]({link})", 1)
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], text_type_text))
            split_nodes.append(TextNode(alt, text_type_image, link))
            text = sections[1]
        if len(text) > 0:
            split_nodes.append(TextNode(text, text_type_text))
        new_nodes.extend(split_nodes)
    return new_nodes




def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        regex_matches = extract_markdown_links(node.text)
        if len(regex_matches) == 0:
            continue
        split_nodes = []
        text = node.text
        for match in regex_matches:
            alt = match[0]
            link = match[1]
            
            sections = text.split(f"[{alt}]({link})", 1)
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], text_type_text))
            split_nodes.append(TextNode(alt, text_type_link, link))
            text = sections[1]
        if len(text) > 0:
            split_nodes.append(TextNode(text, text_type_text))
        new_nodes.extend(split_nodes)
    return new_nodes

