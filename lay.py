from time import sleep as wait
import PySimpleGUI as sg
import back

class Login:
    def main(self):
        sg.theme('reddit')
        layout = [
            [sg.Text('Type in the login password:')],
            [sg.Input(key='pss', password_char='•')],
            [sg.Button('Login')],
            [sg.Text('Incorrect password. Try again.', visible=False, key='incorrect')]
        ]
        window = sg.Window('Accounts Manager', layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Login':
                pss = values['pss']
                ver = back.compare(pss)
                if pss:
                    menu = Menu()
                    menu.main()
                else:
                    window['incorrect'].update(visible=True)


class Menu:
    def main(self):
        sg.theme('reddit')
        layout = [
            [sg.Text('Select what you want to do.')],
            [sg.Button('Register Account'), sg.Button('Remove Account')],
            [sg.Button('Consult DB (Platform)'), sg.Button('Consult DB (Email)')],
            [sg.Button('Consult DB (Password)')]
        ]
        window = sg.Window('Accounts Manager (Menu)', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Register Account':
                register = Register()
                register.main()
            if event == 'Remove Account':
                remove = Remove()
                remove.main()
            if event == 'Consult DB (Platform)':
                verPlat = VerPlat()
                verPlat.main()
            if event == 'Consult DB (Email)':
                verEmail = VerEmail()
                verEmail.main()
            if event == 'Consult DB (Password)':
                verPass = VerPass()
                verPass.main()


class Register:
    def main(self):
        sg.theme('reddit')
        lay = [
            [sg.Text("Fill the spaces with the accounts' informations.")],
            [sg.Text('Platform:'), sg.Input(key='plat')],
            [sg.Text('Email/Login:'), sg.Input(key='email')],
            [sg.Text('Password:'), sg.Input(key='pss', password_char='•')],
            [sg.Button('Register')],
            [sg.Text('Account registered successfully!', visible=False, key='success')],
            [sg.Text('An error ocurred, try again later...', visible=False, key='error')]
        ]
        window = sg.Window('Accounts Manager', lay)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Register':
                plat = values['plat']
                email = values['email']
                psswrd = values['pss']
                register = back.registerAccount(plat, email, psswrd)
                if register:
                    window['success'].update(visible=True)
                    wait(1.5)
                    window.Close()
                else:
                    window['error'].update(visible=True)


class VerPlat:
    def main(self):
        rows = []
        sg.theme('reddit')
        lay = [
            [sg.Text('Type in the platform you want to look for:')],
            [sg.Input(key='plat')],
            [sg.Button('Search')]
        ]
        window = sg.Window('Accounts Manager', lay)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Search':
                plat = values['plat']
                rows = back.consultAccounts('platform', str(plat))
                showResult = ShowResult(rows)
                showResult.main()


class VerEmail:
    def main(self):
        rows = []
        sg.theme('reddit')
        lay = [
            [sg.Text('Type in the email/login you want to look for:')],
            [sg.Input(key='email')],
            [sg.Button('Search')]
        ]
        window = sg.Window('Accounts Manager', lay)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Search':
                email = values['email']
                rows = back.consultAccounts('email', str(email))
                showResult = ShowResult(rows)
                showResult.main()


class VerPass:
    def main(self):
        rows = []
        sg.theme('reddit')
        lay = [
            [sg.Text('Type in the password you want to look for:')],
            [sg.Input(key='pss')],
            [sg.Button('Search')]
        ]
        window = sg.Window('Accounts Manager', lay)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Search':
                pss = values['pss']
                rows = back.consultAccounts('password', str(pss))
                showResult = ShowResult(rows)
                showResult.main


class ShowResult:
    def __init__(self, rows):
        self.rows = rows
    def main(self):
        sg.theme('reddit')
        lay = [
            [sg.Text('Results are:')],
            [sg.Text(text=str(self.rows), visible=True, key='account')]
        ]
        window = sg.Window('Accounts Manager', lay)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break

class Remove:
    def main(self):
        sg.theme('reddit')
        lay = [
            [sg.Text("Type in the account's informations to be deleted")],
            [sg.Text('Platform:'), sg.Input(key='plat')],
            [sg.Text('Email/Login:'), sg.Input(key='email')],
            [sg.Text('Password:'), sg.Input(key='pss', password_char='•')],
            [sg.Button('Delete')],
            [sg.Text('Account deleted successfully!', visible=False, key='success')],
            [sg.Text('An error ocurred, try again later...', visible=False, key='error')]
        ]
        window = sg.Window('Accounts Manager', lay)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Delete':
                plat = values['plat']
                pss = values['pss']
                email = values['email']
                delete = back.removeAccount(plat, email, pss)
                if delete:
                    window['success'].update(visible=True)
                    wait(2)
                    window.Close()
                else:
                    window['error'].update(visible=True)