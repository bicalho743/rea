import sys,struct
def pool(b,off):
    t,hs,sz=struct.unpack_from('<HHI',b,off); n,sn,fl,so,_=struct.unpack_from('<IIIII',b,off+8)
    utf8=fl&0x100; base=off+so; out=[]
    for i in range(n):
        p=base+struct.unpack_from('<I',b,off+hs+4*i)[0]
        if utf8:
            l=b[p]; p+=2 if l&0x80 else 1; l2=b[p]
            if l2&0x80: l2=((l2&0x7f)<<8)|b[p+1]; p+=2
            else: p+=1
            out.append(b[p:p+l2].decode('utf8','replace'))
        else:
            l=struct.unpack_from('<H',b,p)[0]; p+=2
            if l&0x8000: l=((l&0x7fff)<<16)|struct.unpack_from('<H',b,p)[0]; p+=2
            out.append(b[p:p+2*l].decode('utf-16le','replace'))
    return out
b=open(sys.argv[1],'rb').read()
off=int(sys.argv[2]) if len(sys.argv)>2 else 8
for s in pool(b,off): print(repr(s))
