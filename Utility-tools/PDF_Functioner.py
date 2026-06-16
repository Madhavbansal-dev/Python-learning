from pypdf import PdfWriter,PdfReader
class PDF:
    def __init__(self,path):
        self.path=path
    def merge(self,pdfs=[],name="Default.pdf"):
        merger=PdfWriter()
        for pdf in pdfs:
            merger.append(f"{self.path}\\{pdf}")
        merger.write(f"{self.path}\\{name}")
        merger.close()
        print("DONE")
    def reduce_size(self,pdf,name="Default.pdf"):
        writer=PdfWriter(clone_from=f"{self.path}\\{pdf}")
        for page in writer.pages:
            page.compress_content_streams() 
            for img in page.images:
                img.replace(img.image, quality=30)
        writer.write(f"{self.path}\\{name}")
        print("DONE")
    def show_metadata(self,pdfs=[]):
        for pdf in pdfs:
            reader = PdfReader(f"{self.path}\\{pdf}")
            meta=reader.metadata
            meta_XMP = reader.xmp_metadata
            print(pdf)
            print("It's Regular Metadata---")
            if meta:
                print("Title=",meta.title)
                print("Author=",meta.author)
                print("Subject=",meta.subject)
                print("Creator=",meta.creator)
                print("Producer=",meta.producer)
                print("Creation Date=",meta.creation_date)
                print("Modification Date=",meta.modification_date)
                print("It's XMP Metadata---")
            else:
                print("It has no Regular Metadata")
            if meta_XMP:
                print("DC Title=",meta_XMP.dc_title)
                print("DC Description=",meta_XMP.dc_description)
                print("XMP Creation Date=",meta_XMP.xmp_create_date)
            else:
                print("It has no XMP Metadata")
        print("DONE")
    def encrypt(self,pdf,password="0000",name="Default.pdf"):
        reader = PdfReader(f"{self.path}\\{pdf}")
        writer = PdfWriter(clone_from=reader)
        writer.encrypt(password, algorithm="AES-256")
        writer.write(f"{self.path}\\{name}")
        print("DONE")
    def decrypt(self,pdf,password="0000",name="Default.pdf"):
        reader = PdfReader(f"{self.path}\\{pdf}")
        if reader.is_encrypted:
            reader.decrypt(password)
        writer = PdfWriter(clone_from=reader)
        writer.write(f"{self.path}\\{name}")
        print("DONE")
try:
    pdfs=[]
    path=input(r"ENTER THE EXACT PATH OF YOUR PDF FILES: ")
    hmp=int(input("\nHOW MANY PDF's YOU HAVE: "))
    for i in range(hmp):
        pdf=str(input("\nENTER THE EXACT NAME OF PDF WITH .pdf: "))
        pdfs.append(pdf)
    wdyw=int(input("\nWHAT DO YOU WANT TO THESE PDF FILE\n1) MERGE IT\t\t\t(Enter 1)\n2) REDUCE ITS SIZE\t\t(Enter 2)\n3) WANT TO SEE ITS METADATA\t(Enter 3)\n4) PUT A PASSWORD ON IT\t\t(Enter 4)\n5) REMOVE THE PASSWORD ON IT\t(Enter 5)\nENTER: "))
    if wdyw==1:
        name=input("ENTER THE NAME YOU WANT TO PUT ON YOUR MERGED PDF FILE WITH AT LAST .pdf: ")
        obj=PDF(path)
        obj.merge(pdfs,name)
    elif wdyw==2:
        for pdf in pdfs:
            name=input(f"ENTER THE NAME YOU WANT TO PUT AFTER REDUCING {pdf} FILE SIZE WITH AT LAST .pdf: ")
            obj=PDF(path)
            obj.reduce_size(pdf,name=name)
    elif wdyw==3:
        obj=PDF(path)
        obj.show_metadata(pdfs)
    elif wdyw==4:
        for pdf in pdfs:
            password=input(f"ENTER THE PASSWORD YOU WANT TO PUT ON {pdf} FILE: ")
            name=input(f"ENTER THE NAME YOU WANT TO PUT AFTER ENCRYPTING YOUR {pdf} FILE WITH AT LAST .pdf: ")
            obj=PDF(path)
            obj.encrypt(pdf,password=password,name=name)
    elif wdyw==5:
        for pdf in pdfs:
            password=input(f"ENTER THE PASSWORD OF {pdf} FILE: ")
            name=input(f"ENTER THE NAME YOU WANT TO PUT AFTER DECRYPTING YOUR {pdf} FILE WITH AT LAST .pdf: ")
            obj=PDF(path)
            obj.decrypt(pdf,password=password,name=name)
    else:
        print("ENTER ONLY VALID NUMBER")
except Exception as e:
  print(e)
