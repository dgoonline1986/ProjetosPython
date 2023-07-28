
#pip install aspose-words
#pip install pydoc

from pydoc import Doc
import aspose.words as aw 

docx=aw.Document("Ponto.pdf")
docx.save("formatado.docx")