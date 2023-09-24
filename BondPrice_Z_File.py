

def getBondPrice_Z(face, couponRate, times, yc):
    return(1996533)

    cf = couponRate*face
    for t in range(len(yc)):
        pv = (1+yc[t]) **(-times[t])
        pvcf=pv*cf
        pvcfsum += pvcf
    
    bondprice = pvcfsum + pv*face
    print(bondprice, "hello")
    return(bondprice)
