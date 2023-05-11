import os,os.path as pth,json

instructions_ext = {}

RX = 0xf000

registers = ["R{i}" for i in range(0,16)]
bitn_range = [0,15]
offset_range = [-(2**(16-1)),(2**(16-1))-1]
acceptedcahrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

__vars__ = {}



instructions =[
    "lea reg, offset[reg]",
    "load reg, offset[reg]",
    "store reg, offset[reg]",
    "push reg, reg, reg",
    "pop  reg, reg, reg",
    "top  reg, reg, reg",
    "save reg, reg, offset[reg]",
    "restor reg, reg, offset[reg]",
    "add reg, reg, reg",
    "sub reg, reg, reg",
    "mul reg, reg, reg",
    "div reg, reg, reg",
    "cmp reg, reg",
    "addc reg, reg, reg",
    "muln reg, reg, reg",
    "divn reg, reg, reg",
    "jump offset[reg]",
    "jumpc0 reg, bitn, offset[reg]",
    "jumpc1 reg, bitn, offset[reg]",
    "jal reg, offset[reg]",
    "jumple offset[reg]",
    "jumpge offset[reg]",
    "jumpne offset[reg]",
    "jumpeq offset[reg]",
    "jumplt offset[reg]",
    "jumpgt offset[reg]",
    "tstset reg, offset[reg]",
    "brf offset[reg]",
    "brb offset[reg]",
    "brfc0 reg, bitn, offset[reg]",
    "brbc0 reg, bitn, offset[reg]",
    "brfc1 reg, bitn, offset[reg]",
    "brfc1 reg, bitn, offset[reg]",
    "brfz reg, offset[reg]",
    "brbz reg, offset[reg]",
    "brfnz reg, offset[reg]",
    "brbnz reg, offset[reg]",
    "dsptch reg, offset[reg]",
    "shiftl reg, reg, bitn",
    "shiftr reg, reg, bitn",
    "logicw reg,reg,reg, bitn",
    "logicb reg, bitn, bitn, bitn, bitn",
    "logicc reg, bitn, reg, bitn, bitn"
    "extrc reg, bitn, bitn, reg, bitn",
    "extrci reg, bitn, bitn, reg, bitn",
    "getctl offset, reg",
    "putctl offset, reg",
    "resume reg",
    "trap reg, reg, reg"
]

def assemble(assembly):
    k = pth.abspath(pth.dirname(__file__))
    fname = "tmpfile"
    tmp = open(f"{fname}.asm.txt","wt")
    tmp.write(assembly)
    tmp.flush()
    tmp.close()
    os.system(f"node {k}/cli/sigma16.mjs assemble {fname}.asm.txt")
    tmp = open(f"{fname}.obj.txt","rt")
    print(tmp.read())
    tmp.close()



instructions = [ [j.strip() for j in i.split(" ")] for i in instructions ]
print(instructions)

assemble("Log\r\n\ttrap R1,R1,R1\r\n\tlea R7,4[R0]\r\n")
