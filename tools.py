from main import header

def dataformat(data):
    if data == header:
        return data
    formateddata = data.pop(0).split("-")
    formateddata = formateddata[2]+"-"+formateddata[1]+"-"+formateddata[0]

    data.insert(0, formateddata)

    return data

