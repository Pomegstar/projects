from PyPDF2 import PdfMerger
x = ["5cv.pdf","NID.pdf"]
y = PdfMerger()
for i in x:
    y.append(i)
y.write("new.pdf")
y.close()
