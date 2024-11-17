import os
import re
import sys
import time
import requests

import nest_asyncio
from llama_parse import LlamaParse
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

nest_asyncio.apply()

class counter():
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        if (self.count >= 4):
            self.count = 0
            time.sleep(60)


def preprocess_text_list(text_list):
        return "\n\n".join(doc.text for doc in text_list if hasattr(doc, 'text'))


def extract_references(text):
    references = []
    match = re.search(r'(References|Bibliography)(.*)', text, re.IGNORECASE | re.DOTALL)
    if match:
        ref_section = match.group(2)
        refs = ref_section.split("\n")
        references.extend([ref.strip() for ref in refs if ref.strip()])
    return references


def get_papers(queries):
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', google_api_key=os.environ['GOOGLE_API_KEY'])
    calls_track = counter()

    urls = []
    for i, query in enumerate(queries):
        calls_track.increment()
        messages = [(
                "system",
                "Give me the link for this paper so that using wget for the link gets the pdf on my local system. Just give me the link of the paper.",
            ),
            ("human", query),
        ]

        response = llm.invoke(messages)
        print(response.content)
        urls.append(response.content)
        if i==1: break
    return [url.replace('\n', '') for url in urls]


def download_papers(urls):
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                name = url.split('/')[-1]
                with open(f"pdf_papers/{name}", "wb") as f:
                    f.write(response.content)
                print(f"Downloaded paper: {name}")
            else:
                print(f"Failed to download from {url}")
        except:
            print(f"Failed for {url}")

    
def parse_papers(parser):
    dir_path = './pdf_papers'
    output_dir = './txt_papers'
    for filename in os.listdir(dir_path):
        if filename.endswith('.pdf'):
            infile_path = os.path.join(dir_path, filename)
            outfile_path = os.path.join(output_dir, filename)
            output_file = os.path.splitext(outfile_path)[0] + '.txt'
            text = parser.load_data(infile_path)
            combined_text = "\n\n".join(doc.text for doc in text)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(combined_text)


def main(file):
    os.makedirs("pdf_papers", exist_ok=True)
    os.makedirs("txt_papers", exist_ok=True)
    parser = LlamaParse(api_key=os.environ['LLAMAINDEX_API_KEY'], result_type="markdown")

    text = parser.load_data(file)
    output_file = os.path.splitext(file)[0] + '.txt'
    output_path = os.path.join('./txt_papers', output_file)
    combined_text = "\n\n".join(doc.text for doc in text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(combined_text)

    text = preprocess_text_list(text)
    references = extract_references(text)
    queries = [s for s in references if re.match(r'^\d+\.\s', s)]

    urls = get_papers(queries)
    download_papers(urls)
    parse_papers(parser)
    


if __name__ == "__main__":
    n = len(sys.argv)
    if n < 2:
        print('Provide file name!')
    else:
        file = sys.argv[1]
        main(file)