# LESSON 44 - Reading and Editing PDF files
# Note: some files might simply not work.


import PyPDF2 (third-party module, download with pip)

PyPDF has a function called: .PdfFileReader(filename) to read pdf files
This is the order:

    first: open the PDF file in a variable:
        >>> pdfFile = open('FILE PATH', 'rb') # 'rb' stands for "read-binary.
    Then, aff the pdf file into a readable object (reader):
        >>> reader = PyPDF2.PdfFileReader(pdfFile)
        >>> reaer.numPages # stores the number of pages of the pdf
        >>> reader.getPage(int) #gets the page I want
    For example, if I want to deal with the first page of a pdf file:
        >>> pagezero = reader.getPage(0) #pagezero is the first page.
    I can extract the text (sorta) of a page by using:
        >>> page.extractText()

    #
    To extract ALL text from a PDF file:
        for pageNum in range(reader.numPages):
            print(reader.getPage(pageNum).extractText())
    #
PyPDF is very limited in dealing with PDF files.
Cannot change font size, text or anything like that.
It basically handles pages.


# ------------------

TO COMBINE 2 or more PDF files into a new PDF file:
    EXAMPLE:
    >>> pdf1File = open('meetingminutes1.pdf', 'rb')
    # open file 1
    >>> pdf2File = open('meetingminutes2.pdf', 'rb')
    # open file 2
    >>> reader1 = PyPDF2.PdfFileReader(pdf1File)
    # put file 1 in a reader object (variable)
    >>> reader2= PyPDF2.PdfFileReader(pdf2File)
    # do the same here
    >>> writer = PyPDF2.PdfFileWriter() # this file only exists here, right now
    # open a new PDF in a writer object (variable)

# TO ADD all pages in a pdf file into the writer object:
    # file 1:
    >>> for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

    # file 2:	
    >>> for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

# TO SAVE THE WRITER OBJECT AS A FILE:
    >>> outputFile = open('combinedminutes.pdf', 'wb') # 'wb' is writing in binary
    # this is the name of the output file.
    >>> writer.write(outputFile)
    # imma write the outoputfile the contents of "WRITER"
    >>> outputFile.close()
    # close it.
    >>> pdf1File.close()
    >>> pdf2File.close()
    # and close both pdfs too.	
    
