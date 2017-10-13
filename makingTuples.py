
def tupleOut(myDict):
    newarr=[]
    for key in myDict:
        temptuple=(key, myDict[key])
        newarr.append(temptuple)
        

    print newarr



info = {
    "Speros":"(555)-555-5555",
    "Michael":"(999)-999-9999",
    "Jay":"(777)-777-7777"
}
tupleOut(info)