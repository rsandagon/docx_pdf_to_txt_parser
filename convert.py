############################################  NOTE  ########################################################
#
#           Reads a folder and outputs a txt equivalent of docs
#
############################################################################################################

import glob
import codecs
from converter import convert_pdf_to_text
from converter import convert_docx_to_text

class ConvertToTxt():

    def __init__(self):
        # Glob module matches certain patterns
        docx_files = glob.glob("docs/*.docx")
        pdf_files = glob.glob("docs/*.pdf")

        files = set(docx_files + pdf_files)
        files = list(files)

        for f in files:
            # info is a dictionary that stores all the data obtained from parsing
            info = {}
            print('write at', f.split(".")[0])
            self.inputString, info['extension'] = self.readFile(f)
            info['fileName'] = f
            ftxtName = f.split(".")[0] + ".txt"
            ftxt = codecs.open(ftxtName, 'w+', "utf-8")
            trimmed_string = " ".join(self.inputString.split())
            ftxt.write(trimmed_string)
            ftxt.close()

    def readFile(self, fileName):
        extension = fileName.split(".")[-1]
        if extension == "txt":
            f = open(fileName, 'r')
            string = f.read()
            f.close()
            return string, extension
        elif extension == "docx":
            try:
                return convert_docx_to_text(fileName), extension
            except:
                return ''
                pass
        elif extension == "pdf":
            try:
                return convert_pdf_to_text(fileName), extension
            except:
                return ''
                pass
        else:
            print
            'Unsupported format'
            return '', ''


if __name__ == "__main__":
    ConvertToTxt()