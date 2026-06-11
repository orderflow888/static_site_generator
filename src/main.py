from textnode import TextNode

def main():
    # Create a node with dummy data
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    
    # Print the node to see your __repr__ method in action
    print(node)

# This ensures main() only runs if the file is executed directly
if __name__ == "__main__":
    main()
