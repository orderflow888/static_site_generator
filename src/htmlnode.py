
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop, prop_value in self.props.items():
            props_html += f' {prop}="{prop_value}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"