def fact(SQL):
    line=SQL.split(" ")
    str = " "
    for i in line:
        if  i!="DELIMITER" and i!="delimiter" and i!="$$" and i!="DELIMITER;" and i!="delimiter;":
            str=str+" "+i

    line1=str.split(" ")
    str1=" "
    for i in line1:
        if i!="END$$":
            str1=str1+" "+i
        if i=="END$$":
            str1=str1+" "+"END"


    return str1