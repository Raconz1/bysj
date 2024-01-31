
# for num in range(0,6999):
#     a = df.iloc[num]
#     a = a.to_string()
#     print(a)

# print(df.iloc[2])
# for i in range(len(df)):
#    row = df[i:i + 1]
#    print(type(row))
#    print(row)
with open('holder.txt', "r") as f1:  # 设置文件对象
    with open('target.txt', "r") as f2:  # 设置文件对象
        with open('polarity.txt', "r") as f3:  # 设置文件对象
            for data in f1.readlines():
                a = data.replace("\n", "")
                b = f2.readline().replace("\n", "")
                c = int(str(f3.readline()).replace("\n", ""))


                if c == 1:
                    print(a + "对" + b + "的情感为积极\n")
                elif c == -1:
                    print(a + "对" + b + "的情感为消极\n")
                else:
                    print(a + "对" + b + "没有明显的情感倾向\n")
