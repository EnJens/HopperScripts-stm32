def analyzeVectors(doc, seq, adr):
    if adr % 0x100 != 0:
        doc.log("Possibly invalid start address 0x%X!? Aborting!" % adr)
        return
    seg.setTypeAtAddress(adr, 4, Segment.TYPE_INT)
    for offset in range(adr + 4, adr + 0x180, 4):
        value = seg.readByte(offset+3) << 24 | seg.readByte(offset+2) << 16 | seg.readByte(offset+1) <<8 | seg.readByte(offset)
        doc.log("0x%X = 0x%X" % (offset, value))
        seg.setTypeAtAddress(offset, 4, Segment.TYPE_INT)
        if value != 0:
            doc.log("Marking 0x%X as code" % value)
            seg.markAsCode(value)
    


doc = Document.getCurrentDocument()
seg = doc.getCurrentSegment()
adr = doc.getCurrentAddress()

analyzeVectors(doc, seg, adr)

