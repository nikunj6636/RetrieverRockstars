## Creating virtualenv
```
conda create --name venv python=3.10 -y
conda activate
pip install -r requirements.txt
```


## How to run:
```
python3 main.py </path/to/pdf>
```


## Output Generated
- The input file is also parsed and its text file is stored in txt_papers directory.
- All the research papers are stored in the pdf format under the pdf_papers directory.
- All the pdf papers parsed using llama are stored in text format under the txt_papers directory.
