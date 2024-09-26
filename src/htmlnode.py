

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return None
        st = ""
        for key, value in self.props.items():
            st += f' {key}={value}'
        return st

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.props_to_html()})"
    

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        props = self.props_to_html()
        if not props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError()
        if not self.children:
            raise ValueError("Expecting children")
        props = self.props_to_html()
        if not props:
            val = f"<{self.tag}>"
        else:
            val = f"<{self.tag}{props}>"
        for child in self.children:
            val += child.to_html()
        val += f"</{self.tag}>"
        return val
        