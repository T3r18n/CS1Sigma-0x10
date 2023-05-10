import st

class AsmInfo :
    def __init__ (this):
        this.modName = "anonymous"     # default
        this.text = ""                 # raw source text
        this.asmSrcLines = []          # list of lines of source text
        this.asmStmt = []              # corresponds to source lines
        this.symbols = []              # symbols used in the source
        this.symbolTable = {}          # symbol table
        this.locationCounter = 0       #  next code address
        this.objectCode = []           # string hex representation
        this.objectText = ""           # object code as single string
        this.metadata = st.Metadata() # address-source map
        this.imports = []              # imported module/identifier
        this.exports = []              # exported identifiers
        this.nAsmErrors = 0            # errors in assembly source code
        this.executable = st.emptyExe  # {object code, maybe metadata}
        this.objMd = None
