from tkinter import *
from tkinter import ttk, messagebox
from settings import *
from logics import CDA

db = CDA()

class Main(Tk):

    def __init__(self):
        Tk.__init__(self)

        app = Frame(self, bg=PURPLE)
        app.pack(side=TOP, fill=BOTH, expand=True)
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (Home,Dashboard ):
            frame = f(app, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame(Home)

    # create a function to raise frame
    def show_frame(self, control):
        frame = self.frames[control]
        frame.tkraise()


class Home(Frame):

    def __init__(self, master, controller):
        super(Home, self).__init__(master)
        self.controller = controller

        self.wind_packer = Frame(self, bg=LIGHT_PURPLE)
        self.wind_packer.pack(fill=BOTH, expand=True)

        Label(self.wind_packer, text=APP_NAME, bg=PURPLE, fg=YELLOW, font=BIG_FONT).pack(fill=X, ipadx=15, ipady=5)
        self.disp = Frame(self.wind_packer, bg=PURPLE)
        self.disp.pack(pady=20, padx=20)

        Button(self.disp, text="REGISTER LANDLORD", bg=YELLOW, font=BTN_FONT, command=self.reg_landlord_wid).grid(row=0, column=0, sticky=W)
        Button(self.disp, text="LOGIN LANDLORD", bg=YELLOW, font=BTN_FONT, command=self.login_landlord_wid).grid(row=0, column=1, sticky=W)
        Button(self.disp, text="VERIFY TENANT", bg=YELLOW, font=BTN_FONT).grid(row=1, column=0, columnspan=2, sticky='news')

#this function handles registration of landlords
    def reg_landlord_wid(self):
        self.reg_landlord = Toplevel()
        self.reg_landlord.config(bg=LIGHT_PURPLE)
        self.reg_landlord.grab_set()

        self.wid_frm = Frame(self.reg_landlord, bg=YELLOW)
        self.wid_frm.pack(padx=20, pady=20)

        Label(self.wid_frm, text='Register Landlord', bg=PURPLE, fg=YELLOW).pack()

        self.packer = Frame(self.wid_frm)
        self.packer.pack(padx=5, pady=5)

        Label(self.packer, text='Name: ').grid(row=0, column=0, sticky=W)
        self.land_name = ttk.Entry(self.packer)
        self.land_name.grid(row=0, column=1, sticky=W)

        Label(self.packer, text='Mobile: ').grid(row=1, column=0, sticky=W)
        self.mobile = ttk.Entry(self.packer)
        self.mobile.grid(row=1, column=1, sticky=W)

        Label(self.packer, text='Password: ').grid(row=2, column=0, sticky=W)
        self.land_pass = ttk.Entry(self.packer, show='*')
        self.land_pass.grid(row=2, column=1, sticky=W)

        ttk.Button(self.packer, text='Register', command=self.reg_landlord_func).grid(row=3, column=1, sticky='news', pady=5)

    def reg_landlord_func(self):
        name = self.land_name.get().upper()
        mobile = self.mobile.get()
        pasw = self.land_pass.get()
        self.wid_frm.destroy()
        self.reg_landlord.destroy()
        self.packer.destroy()


        id = db.register_landLord(name, mobile, pasw)

        messagebox.showinfo(APP_NAME, f'Landlord ID: {id}')

#End of landlord registration

#Login landlord functions
    def login_landlord_wid(self):
        self.login_landlord = Toplevel()
        self.login_landlord.config(bg=LIGHT_PURPLE)
        self.login_landlord.grab_set()

        self.wid_frmm = Frame(self.login_landlord, bg=YELLOW)
        self.wid_frmm.pack(padx=20, pady=20)

        Label(self.wid_frmm, text='Login Landlord', bg=PURPLE, fg=YELLOW).pack()

        self.packerrr = Frame(self.wid_frmm)
        self.packerrr.pack(padx=5, pady=5)

        Label(self.packerrr, text='Landlord ID: ').grid(row=0, column=0, sticky=W)
        self.land_id = ttk.Entry(self.packerrr)
        self.land_id.grid(row=0, column=1, sticky=W)

        Label(self.packerrr, text='Password: ').grid(row=2, column=0, sticky=W)
        self.land_pass = ttk.Entry(self.packerrr, show='*')
        self.land_pass.grid(row=2, column=1, sticky=W)

        ttk.Button(self.packerrr, text='Login', command=self.login_landlord_func).grid(row=3, column=1, sticky='news', pady=5)

    def login_landlord_func(self):
        id = self.land_id.get().upper()
        pasw = self.land_pass.get()
        self.login_landlord.destroy()
        self.wid_frmm.destroy()
        self.packerrr.destroy()

        resp = db.login_landlord(id, pasw)
        if resp['msg'] == 'Successful':
            messagebox.showinfo(APP_NAME, f'Welcome! {resp["info"]["Name"]}')
            self.controller.show_frame(Dashboard)

        else:
            messagebox.showerror(APP_NAME, f'{resp["msg"]}')



#End of login function



class Dashboard(Frame):

    def __init__(self, master, controller,):
        super(Dashboard, self).__init__(master)
        self.controller = controller

        self.windows = Frame(self, bg=LIGHT_PURPLE)
        self.windows.pack(fill=BOTH, expand=True)

        Label(self.windows, text="Landlord Dashboard", bg=PURPLE, fg=YELLOW, font=BIG_FONT).pack(fill=X, ipadx=15, ipady=5)
        self.dispp = Frame(self.windows, bg=PURPLE)
        self.dispp.pack(pady=20, padx=20)

        Button(self.dispp, text="REGISTER Tenant", bg=YELLOW, font=BTN_FONT,command=self.reg_tenant_wid).grid(row=0, column=0, sticky=W) #c)
        Button(self.dispp, text="DELETE Tenant", bg=YELLOW, font=BTN_FONT,).grid(row=0, column=1, sticky=W)# command=self.del_tenant_wid)
        Button(self.dispp, text="VERIFY TENANT", bg=YELLOW, font=BTN_FONT).grid(row=1, column=0, columnspan=2, sticky='news')

    # this function handles registration of tenants
    def reg_tenant_wid(self):
        self.reg_tenant = Toplevel()
        self.reg_tenant.config(bg=LIGHT_PURPLE)
        self.reg_tenant.grab_set()

        wid_frame = Frame(self.reg_tenant, bg=YELLOW)
        wid_frame.pack(padx=20, pady=20)

        Label(wid_frame, text='Register Tenant', bg=PURPLE, fg=YELLOW).pack()

        packerr = Frame(wid_frame)
        packerr.pack(padx=5, pady=5)

        Label(packerr, text='Name: ').grid(row=0, column=0, sticky=W)
        self.tenant_name = ttk.Entry(packerr)
        self.tenant_name.grid(row=0, column=1, sticky=W)

        Label(packerr, text='Mobile: ').grid(row=1, column=0, sticky=W)
        self.ten_mobile = ttk.Entry(packerr)
        self.ten_mobile.grid(row=1, column=1, sticky=W)

        ttk.Button(packerr, text='Register', command=self.reg_tenant_func).grid(row=3, column=1, sticky='news',
                                                                                 pady=5)

    def reg_tenant_func(self):
        name = self.tenant_name.get().upper()
        mobile = self.ten_mobile.get()

        id = db.register_tenant(name, mobile,)

        messagebox.showinfo(APP_NAME, f'Tenant ID: {id}')

# End of tenant registration