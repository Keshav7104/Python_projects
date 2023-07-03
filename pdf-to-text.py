from PyPDF2 import PdfReader
from os import listdir

files=listdir()
pdfs=[fil for fil in files if fil.endswith('.pdf')]

def read(pdf:str)->str:
    reader = PdfReader(f"{pdf}.pdf")
    t=open(f"{pdf}.txt","w")
    for i in range(len(reader.pages)):
        page=reader.pages[i]
        t.write(page.extract_text())
    t.close()


if __name__ == "__main__":
    print("Following Pdfs are available for Operation")
    print(pdfs)
    pd=input("Enter the name of pdf to convert into txt(without .pdf)\n")
    read(pd)
    print(f"Work done check {pd}.txt in folder")
