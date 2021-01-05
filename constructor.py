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
        self.geometry('500x600')

        # filename
        file_name = StringVar()
        self.filename = Entry(self, textvariable=file_name)
        Label(text='File name without ".py"').pack()
        self.filename.pack()

        # token
        token = StringVar()
        self.ent = Entry(self, textvariable=token)
        Label(text='token').pack()
        self.ent.pack()

        # textfield
        self.text = Text(self, width=50, height=10)
        self.text.pack()
        Label(text='Example:\nResponse -> request\ndelete: res -> req', font=("Consolas", 10)).pack()

        # script
        self.label = Label(self, text='Your script will be here')
        self.label.pack()
        self.script = ''

        Button(self, text='Create bot', command=self.create_bot).pack(side=BOTTOM)
        Button(self, text='Create script', command=self.create_script).pack(side=BOTTOM)
        Label(text='Firstly create script, \nif you sure everything is ready then click "create bot"',
              font=("Consolas", 11)).pack(side=BOTTOM)

    def delete_part(self):
        string = self.text.get(1.0, END)
        string = string.split(':')
        deleted_str = string[1].strip() + '\n'
        self.script = self.script.replace(deleted_str, '')

    def create_script(self):
        msg = self.text.get(1.0, END)
        if 'delete' in msg.lower():
            self.delete_part()
            self.label.configure(text=f'Your script:\n\nYour token: {self.ent.get()}\n\n{self.script}')
        else:
            self.script += msg
            self.label.configure(text=f'Your script:\n\nYour token: {self.ent.get()}\n\n{self.script}')
        print(self.script.split('\n'))

    def create_bot(self):
        msg_list = self.script.split('\n')
        for msg in msg_list:
            mes = msg.split('->')
            if msg != '':
                # print(mes)
                self.res.append(mes[0])
                self.req.append(mes[1])
        bot_creating(self.res, self.req, self.ent.get(), self.filename.get())
        print(f'Responses:{self.res}\n Requests{self.req}')


if __name__ == '__main__':
    window = Constructor()
    mainloop()
