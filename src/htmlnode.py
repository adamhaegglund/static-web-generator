
class HTMLNode:
    def __init__(self, tag : str | None = None, value : str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("not yet implemented")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        
        result_string = ""
        for k,v in self.props.items():
           tmp_string=f' {k}="{v}"'
           result_string += tmp_string

        return result_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("All leafs must have a value")
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("A parent node needs a tag")
        if self.children is None:
            raise ValueError("A parent node needs children")
        
        result_string = ""
        for child in self.children:
            result_string += child.to_html()

        return f"<{self.tag}>{result_string}</{self.tag}>"
