from textnode import TextNode, TextType

def main():
    tn = TextNode("This is some anchor text", TextType.BOLD , "https://www.google.com")
    print(tn)

if __name__ == "__main__":
    main()
