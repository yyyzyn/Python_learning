#使用制表符或换行符添加空白
#\t添加制表符
#\n添加换行符
#print("\tPython")
#print("Languages:\nPython\nC\nJava")
#print("Languages:\n\tPython\n\tC\n\tJava")

#删除空白
#字符串末尾没有空白，方法rstrip()
#favourite_language="python "
#print(favourite_language)
#favourite_language=favourite_language.rstrip()
#print(favourite_language)
favourite_language=" python "
print(favourite_language)
favourite_language=favourite_language.strip()#同时消除字符串两端空白
print(favourite_language)

#函数str()将非字符串转换为字符串
age=24
message="Happy " +str(age)+"rd Birthday"+"to you"
print(message)


