# import urllib.request
# from urllib import parse
# from html.parser import HTMLParser
# import os
# import mysql.connector

# connect = mysql.connector.connect(user = 'root', 
#                                   password = 'lucifer123#321', 
#                                   host = 'localhost', 
#                                   database = 'flaskapp')
# cursor = connect.cursor(buffered= True)

# # creating the databases




    

    
#     #print(list_of_table)


# r = open("project/queue.txt", "r")

# #capturing the content of tge file
# cont = r.read()
# r.close()
# print(cont)

# re = urllib.request.urlopen(cont)

# #checking the content-type of the page
# if re.getheader('content-type') == 'text/html' or 'text/css':
#     #print(re)
#     html = re.read()
#     #print(html)
#     strings = html.decode('utf-8')
#     #print(strings)

# #htmlpraser subclass for collecting the urls
# class finder(HTMLParser):
#     def __init__(self, base):
#         super().__init__()      #for accessing the instance-attributes of the mainclass
#         self.base = base        
#         self.links = []      

#     def handle_starttag(self, tag, attrs):
#         #checking for the 'anchor' tags and 'href' attributes
        
#         if tag == 'a':
#             print("entring the data")
#             for (attr, value) in attrs:
#                 if attr == 'href':
#                     url = urllib.parse.urljoin(self.base, value + "," + "\n") #for completing the url if any is incomplete
#                     self.links.append(url)

   
    

# fq = finder("https://automatetheboringstuff.com/") #main or homapage for the completion of any incomplete url
# fq.feed(strings)        #feeding the parser with the html/css code


# def store_links(lik):
    
#     for i, value in enumerate(lik):
#         if i == len(lik):
            
#              break
#         else:
#             tuple_list = [tuple(map(str, sub.split(', '))) for sub in lik]
#             #print(i)    
#             formula = (INSERT INTO url_links (url) VALUES (%s);)
#             #print(tuple_list)

#             cursor.executemany(formula, tuple_list)
#             connect.commit()
    
    
    
    
# store_links(fq.links)
# """
# cursor.close()
# connect.close()


# class main:
#     l = [1,3,4]
#     def __init__(self):
#         main.a()
#         #self.a = a
#     @staticmethod
#     def a():
#         print('hello')

#ab = main()
a = [i for i in range(10)]
print(a)