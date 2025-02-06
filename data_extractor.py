from langchain.document_loaders import WebBaseLoader

url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
documents = loader.load()

# Save the documents for later use
with open('extracted_data.txt', 'w') as f:
    for doc in documents:
        f.write(doc.page_content + "\n")