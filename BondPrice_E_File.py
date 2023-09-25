

def getBondPrice_E(face, couponRate, m, yc):
    pvcfsum = 0
    
    cf = couponRate*face
    for t in range(1,m+1):
        pv = (1+yc[t-1]) **(-t)
        pvcf=pv*cf
        pvcfsum += pvcf
    
    bondprice = pvcfsum + pv*face
    #print(bondprice, "hello")
    return(bondprice)
    #return(2098949)
