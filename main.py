from pypdf import PdfMerger, PdfWriter

pdfiles = ['1.pdf', '2.pdf']
merger = PdfWriter()
for pdf in pdfiles:
    # merger.append(pdf)
    # merger.merge(2,pdf)
    merger.append(pdf, pages=(0, 3))
merger.write('merged3.pdf')
merger.close()