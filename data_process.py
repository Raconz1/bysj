import csv

# 打开txt文件
with open('D:\毕业设计\datasets\红楼梦\红楼梦训练集.txt', 'rb') as file:
    for data in file.readlines():
        data = data.decode().strip('\n')  # 去掉列表中每一个元素的换行符
        # 使用split()方法分割数据
        fields = data.split('_!_')

        # 将各个字段存储到不同变量中
        sentence = fields[0]
        holder = fields[1]
        target = fields[2]
        # polarity = int(fields[3])
        polarity = fields[3]
        with open('sentence.txt', 'a+') as f:  # 设置文件对象
            f.write(sentence)  # 将字符串写入文件中
            f.write("\n")

        with open('holder.txt', 'a+') as f:  # 设置文件对象
            f.write(holder)  # 将字符串写入文件中
            f.write("\n")
        with open('target.txt', 'a+') as f:  # 设置文件对象
            f.write(target)  # 将字符串写入文件中
            f.write("\n")
        with open('polarity.txt', 'a+') as f:  # 设置文件对象
            f.write(polarity)  # 将字符串写入文件中

        # with open('hlm_sentence.csv', 'a+', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow([sentence])
        #
        # with open('hlm_holder.csv', 'a+', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow([holder])
        #
        # with open('hlm_target.csv', 'a+', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow([target])
        #
        # with open('hlm_polarity.csv', 'a+', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow([polarity])
        if sentence == '晴雯严肃地对黛玉说：“黛玉，人生充满了艰辛，但只要我们坚守初心，一切都值得。”':
            break

print("数据处理结束")
