# from PyPDF2 import PdfMerger
#
# two_pdf= ["Welcome to python pdf file.pdf","Hello.pdf"]
# MM = PdfMerger()
#
# for oky in two_pdf:
#     MM.append(oky)
#
# MM.write("sourav.pdf")
# MM.close()


from PyPDF2 import PdfMerger

Two_pdf = ["Hello.pdf","Welcome to python pdf file.pdf"]
my_merger = PdfMerger()

for file in Two_pdf:
    my_merger.append(file)

my_merger.write("sourav_1.pdf")
my_merger.close()


















