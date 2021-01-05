from tkinter import *
from code_blocks import *


# class EntryWithPlaceholder(Entry):
#     def __init__(self, master=None, placeholder=None):
#         self.entry_var = StringVar()
#         super().__init__(master, textvariable=self.entry_var)
#
#         if placeholder is not None:
#             self.placeholder = placeholder
#             self.placeholder_color = 'grey'
#             self.default_fg_color = self['fg']
#             self.placeholder_on = False
#             self.put_placeholder()
#
#             self.entry_var.trace("w", self.entry_change)
#
#             self.bind("<FocusIn>", self.reset_cursor)
#             self.bind("<KeyRelease>", self.reset_cursor)
#             self.bind("<ButtonRelease>", self.reset_cursor)
#
#     def entry_change(self, *args):
#         if not self.get():
#             self.put_placeholder()
#         elif self.placeholder_on:
#             self.remove_placeholder()
#             self.entry_change()
#
#     def put_placeholder(self):
#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color
#         self.icursor(0)
#         self.placeholder_on = True
#
#     def remove_placeholder(self):
#         text = self.get()[:-len(self.placeholder)]
#         self.delete('0', 'end')
#         self['fg'] = self.default_fg_color
#         self.insert(0, text)
#         self.placeholder_on = False
#
#     def reset_cursor(self, *args):
#         if self.placeholder_on:
#             self.icursor(0)


class Constructor(Tk):
    my_list_of_entries = list()
    req = []
    res = []

    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.text = Text(self, width=50, height=10)
        self.text.pack()
        Button(self, text='Create bot', command=self.create_bot).pack(side=BOTTOM)
        Label(text='Response -> request').pack()

    def add_new_block(self):
        # for _ in range(2):
        request = StringVar()
        response = StringVar()
        self.req.append(Entry(self, textvariable=request))
        self.req[-1].pack()
        self.res.append(Entry(self, textvariable=response))
        self.res[-1].pack()
        # self.my_list_of_entries.append(Entry(self))
        # self.my_list_of_entries[-1].pack()
        Label().pack()

    def create_bot(self):
        msg = self.text.get(1.0, END)
        msg_list = msg.split('\n')
        for msg in msg_list:
            mes = msg.split('->')
            if msg != '':
                # print(mes)
                self.res.append(mes[0])
                self.req.append(mes[1])
        bot_creating(self.res, self.req)
        print(f'Responses:{self.res}\n Requests{self.req}')


if __name__ == '__main__':
    window = Constructor()
    # Button(window, text="Add new block", command=window.add_new_block).pack()
    mainloop()
