import mysql.connector



connect = mysql.connector.connect(user='root',
                                  password='lucifer123#321',
                                  host='localhost',
                                  database='flaskapp')
cursor = connect.cursor(buffered=True)



def storing(table,links):
    name_table = tuple(map(str, table.split(' ')))
    cursor.execute("SELECT id FROM %s" % (table))
    r = cursor.fetchall()
    old_index = r[-1]
    new_index = int(' '.join(map(str, old_index))) + 1
    #print(links)
    index = []
    for u in range(new_index, len(links)):
        index.append(u)
    # merging two lists into one lint of tuples
    print(index)
    merged_list = [(index[i], links[i]) for i in range(0, len(index))]
    print(table)

    # inserting into the table
    cursor.execute("SHOW TABLES")
    row = cursor.fetchall()

    for i in row:

        if name_table == i:
            print('yes')

            for _ in links:
                if links.index == range(len(links)):
                    print(links.index)
                    break

                else: 
                    print(links)

                    formula_queue = (
                        "INSERT INTO {0} (id, queue) VALUES (%s,%s);" .format(table))
                    cursor.executemany(formula_queue, merged_list)

                    
                    



# l = ['a','b','c']
# # for i in range(100):
# #     l.append(i)
# print(l)

#storing('table1', l)

connect.commit()
cursor.close()
connect.close()
