import requests, json
from tkinter import messagebox,Tk,StringVar,Entry,END,NSEW,Button,Text


def translator():
    query = entry.get()
    if query == '':
        messagebox.showinfo('提示', '您输入的内容为空！')
        return
    else:
        if check(query):
            eng = 0
        else:
            eng = 1
        url = 'http://fanyi.so.com/index/search'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Cookie': 'Q_UDID=f3797e68-bc5e-2403-8ad0-bbb6cf98f289; __guid=144965027.2578340336991455700.1604373195726.7173; count=1; __huid=11E9i8kKBTI6hHfObrogibNbIJKEXY9NFGKLLuSKegRPw%3D; gtHuid=1',
            'Host': 'fanyi.so.com',
            'Origin': 'http://fanyi.so.com',
            'pro': 'fanyi',
            'Referer': 'http://fanyi.so.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }

        data = {
            'eng': eng,
            'validate': '',
            'ignore_trans': 0,
            'query': query
        }
        response = requests.post(url, headers=headers, data=data)
        response = json.loads(response.text)
        if eng == 0:
            trans(response)
            translation(response)
        else:
            trans(response)
            translation(response)


def trans(response):
    text.delete(1.0, END)
    text.insert(1.0, response['data']['fanyi'] + '\n')


def translation(response):
    try:
        if response['data']['explain']['translation'] is not None:
            for i in response['data']['explain']['translation']:
                text.insert(2.0, i + '\n')
    except:
        return


def check(query):
    for ch in query:
        if u'\u4e00' <= ch <= '\u9fff':
            return True
    return False


if __name__ == '__main__':
    # trans = translator()
    # print(trans)
    root = Tk()
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()
    root.geometry('385x220+' + str(int(win_width / 2 - 192)) + '+' + str(int(win_height / 2 - 110)))
    root.title('360翻译-农耀扫地僧')

    query = StringVar()
    query.set('请输入需要翻译的内容')
    entry = Entry(root, width=20, font=('华为行楷', 16), textvariable=query)
    entry.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

    button = Button(root, text='翻译', command=translator)
    button.grid(row=0, column=1, pady=10, padx=10, sticky=NSEW)

    text = Text(root, width=30, height=6, font=('华为行楷', 16))
    text.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky=NSEW)

    root.mainloop()
