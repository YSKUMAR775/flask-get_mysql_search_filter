import pymysql


def search(data):
    a = '%' + data + '%'

    mydb = pymysql.connect(host='database.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                           user='root',
                           password='yskumar775',
                           db='sql_flask_excel',
                           )
    cur = mydb.cursor()
    query = " select * from sql_flask_excel_table where address like '" + str(a) + "' "

    cur.execute(query)
    s = cur.fetchall()
    # print(s)

    total_list = []
    for i in s:
        all_dict = {'id': i[0], 'name_info': i[1], 'contact': i[2], 'mail': i[3], 'address': i[4]}
        total_list.append(all_dict)

    return total_list
