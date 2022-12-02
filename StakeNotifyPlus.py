import requests
from bs4 import BeautifulSoup
import os
import ctypes
import lxml
import time
import threading
import unicodedata
from datetime import datetime
import webbrowser
import pyperclip
from plyer import notification


kernel32 = ctypes.windll.kernel32
handle = kernel32.GetStdHandle(-11)
kernel32.SetConsoleMode(handle, 0x0001 + 0x0002 + 0x0004)
os.system("title Auto Bonus❤ made by moku")

class C:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

class StakeBonusCodeScraper():
    def __init__(self):
        self.AutoOpenBrowser = False
        self.AutoCopy = False
        self.Notify = False
        self.language = "en"

        self.update_interval = 10
        self.now_code = (None, "null", None)
        self.is_new_code = False
        self.Custome_Browser = None

        self.texts = {
            "Settings": {
                "Question_Auto_Open_Browser": {
                    "ja": "ボーナスコードを受信したときに、自動でサイトを開きますか？(y/n)",
                    "en": "Do you want your browser to open automatically when you receive a bonus code?(y/n)"
                },
                "Question_Auto_Copy_Code": {
                    "ja": "ボーナスコードを受信したときに、自動でコードをコピーしますか？これを有効にしておくとブラウザを開いた後スムーズにコードを入力できます(y/n)",
                    "en": "Do you want to automatically copy the code when you receive a bonus code? If you enable this, you can enter the code smoothly after opening the browser(y/n)"
                },
                "Question_Custome_Browser": {
                    "ja": "ブラウザの指定をしますか?(y/n)",
                    "en": "Would you like to specify a browser?(y/n)"
                },
                "Question_Custome_Browser_Path": {
                    "ja": "ブラウザのパスを入力してください(ex: C:\Program Files\Google\Chrome\Application\chrome.exe)",
                    "en": "Please enter the browser path(ex: C:\Program Files\Google\Chrome\Application\chrome.exe)"
                },
                "Question_Notify": {
                    "ja": "ボーナスコードを受信したときに、トースト通知を出しますか?(y/n)",
                    "en": "Do you want a toast notification when you receive a bonus code?(y/n)"
                },
                "SetupComplete": {
                    "ja": "セットアップが完了しました。",
                    "en": "Setup is complete."
                }
            },
            "Notify": {
                "Title": {
                    "ja": "ボーナスコードを検出しました!!",
                    "en": "Bonus code detected!!"
                },
                "Message": {
                    "ja": "ボーナスコード: ",
                    "en": "Bonus Code: "
                }

            }
        }

    def Check_Telegram(self):
        telegram = requests.get("https://t.me/s/StakeCasino")

        codes = []

        html = BeautifulSoup(telegram.text, "lxml")
        for element in html.find_all("div", class_="tgme_widget_message_text"):
            if "25 Days of Christmas" in element.get_text() and "Monthly Bonus" not in element.get_text():
                code = None
                prefix = None
                try:
                    code = element.get_text().split("claim,")[1].split("-")[0]
                except: None
                try:
                    prefix = element.get_text().split("you must add ")[1].split(" ")[0]
                except: None
                try:
                    amount = element.get_text().split("- Value: ")[1].split("-")[0]
                except: None
                try:
                    position = "end" if "onto the end" in element.get_text() else "start"
                except: None
                codes.append((prefix, code, amount, position))

        if self.now_code[1] == codes[-1][1]:
            self.is_new_code = True
        else:
            self.now_code = codes[-1]
            self.is_new_code = False

    def mainloop(self):
        try:
            while True:
                time.sleep(self.update_interval)
                ldng = loading(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]Checking Telegram")
                threading.Thread(target=ldng.execute).start()

                self.Check_Telegram()
                if self.is_new_code:
                    ldng.text = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]No Code found>>^end"
                    time.sleep(0.5)
                    ldng.exit = True
                    print("")
                else:
                    ldng.text = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]Code Found>>^end"
                    time.sleep(0.5)
                    ldng.exit = True
                    if self.now_code[0] or self.now_code[1] or self.now_code[2]:
                        info_aa = f"{C.MAGENTA}=============== Info ===============\n"

                        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        timelength = util.precisionlen("Time: "+now)
                        leftspace = (34 - timelength) // 2
                        if timelength % 2 == 1:
                            rightspace = leftspace + 1
                        else:
                            rightspace = leftspace
                        info_aa += f"={' '*leftspace}Time: {now}{' '*rightspace}=\n"

                        if self.now_code[0]:
                            prefixlength = util.precisionlen("Prefix: "+self.now_code[0])
                            leftspace = (34 - prefixlength) // 2
                            if prefixlength % 2 == 1:
                                rightspace = leftspace + 1
                            else:
                                rightspace = leftspace
                            info_aa += f"={' '*leftspace}Prefix: {self.now_code[0]}{' '*rightspace}=\n"

                        if self.now_code[1]:
                            codelength = util.precisionlen("Code: "+self.now_code[1])
                            leftspace = (34 - codelength) // 2
                            if codelength % 2 == 1:
                                rightspace = leftspace + 1
                            else:
                                rightspace = leftspace
                            info_aa += f"={' '*leftspace}Code: {self.now_code[1]}{' '*rightspace}=\n"

                        if self.now_code[1] and self.now_code[0]:
                            codelength = util.precisionlen("All: "+self.now_code[0]+self.now_code[1])
                            leftspace = (34 - codelength) // 2
                            if codelength % 2 == 1:
                                rightspace = leftspace + 1
                            else:
                                rightspace = leftspace
                            if self.now_code[3] == "end":
                                info_aa += f"={' '*leftspace}All: {self.now_code[1]+self.now_code[0]}{' '*rightspace}=\n"
                            else:
                                info_aa += f"={' '*leftspace}All: {self.now_code[0]+self.now_code[1]}{' '*rightspace}=\n"

                        if self.now_code[2]:
                            valuelength = util.precisionlen("Value: "+self.now_code[2])
                            leftspace = (34 - valuelength) // 2
                            if valuelength % 2 == 1:
                                rightspace = leftspace + 1
                            else:
                                rightspace = leftspace
                            info_aa += f"={' '*leftspace}Value: {self.now_code[2]}{' '*rightspace}=\n"

                        info_aa += "="*36+C.RESET

                        print(info_aa+"\n\n")
                        if self.now_code[3] == "end":
                            Allcode = self.now_code[1]+self.now_code[0]
                        else:
                            Allcode = self.now_code[0]+self.now_code[1]

                        if self.Notify:
                            notification.notify(title=self.texts["Notify"]["Title"][self.language], message=self.texts["Notify"]["Message"][self.language]+Allcode, app_name="Stake Bonus Notify", app_icon="stakeicon.ico", timeout=5)

                        if self.AutoCopy:
                            pyperclip.copy(Allcode)

                        if self.AutoOpenBrowser:
                            if self.Custome_Browser:
                                browser = webbrowser.get(f'"{self.Custome_Browser}" %s')
                                browser.open(f"https://stake.com/settings/offers?type=drop&code={Allcode}&currency=ltc&modal=redeemBonus")
                            else:
                                webbrowser.open_new(f"https://stake.com/settings/offers?type=drop&code={Allcode}&currency=ltc&modal=redeemBonus")
        except: self.mainloop()

    def setconfig(self):
        print("🌎Language(en/ja):")
        language = util.limited_input(["en", "ja"])
        self.language = language
        print(self.texts["Settings"]["Question_Auto_Open_Browser"][self.language])
        Question_Auto_Open_Browser = util.limited_input(["y", "n"])
        if Question_Auto_Open_Browser == "y":
            self.AutoOpenBrowser = True
        print(self.texts["Settings"]["Question_Auto_Copy_Code"][self.language])
        Question_Auto_Copy_Code = util.limited_input(["y", "n"])
        if Question_Auto_Copy_Code == "y":
            self.AutoCopy = True
        if self.AutoOpenBrowser:
            print(self.texts["Settings"]["Question_Custome_Browser"][self.language])
            Question_Custome_Browser = util.limited_input(["y", "n"])
            if Question_Custome_Browser == "y":
                print(self.texts["Settings"]["Question_Custome_Browser_Path"][self.language])
                while True:
                    path = input(">>")
                    if os.path.isfile(path):
                        self.Custome_Browser = path
                        break
                    else:
                        print(f"{C.RED}Invalid input{C.RESET}")
                        time.sleep(1)
                        print("\033[A                                                                             \033[A")
                        print("\033[A                                                                             \033[A")
        if not self.AutoOpenBrowser:
            print(self.texts["Settings"]["Question_Notify"][self.language])
            Question_Notify = util.limited_input(["y", "n"])
            if Question_Notify == "y":
                self.Notify = True
        print(self.texts["Settings"]["SetupComplete"][self.language])
        time.sleep(2)
        os.system("cls")

class loading():
    def __init__(self, text):
        self.text = text

    def execute(self):
        i = 0
        while True:
            i += 1
            if len(self.text.split(">>^")) == 2:
                print("                                                                             ", end="\r")
                return print(self.text.split(">>^")[0])
            b = self.text + "." * i
            print(b, end="\r")
            time.sleep(0.5)

class util():
    @staticmethod
    def limited_input(limit):
        while True:
            user_input = input(">>")
            if type(limit) == list:
                if user_input in limit:
                    return user_input
                else:
                    print(f"{C.RED}Invalid input{C.RESET}")
                    time.sleep(1)
                    print("\033[A                                                                             \033[A")
                    print("\033[A                                                                             \033[A")
            elif type(limit) == int:
                if user_input.isdigit():
                    return user_input
                else:
                    print(f"{C.RED}Invalid input{C.RESET}")
                    time.sleep(1)
                    print("\033[A                                                                             \033[A")
                    print("\033[A                                                                             \033[A")
            else:
                if limit(user_input):
                    return user_input
                else:
                    print(f"{C.RED}Invalid input{C.RESET}")
                    time.sleep(1)
                    print("\033[A                                                                             \033[A")
                    print("\033[A                                                                             \033[A")

    @staticmethod
    def precisionlen(text):
        length = 0
        for c in text:
            if unicodedata.east_asian_width(c) in "FWA":
                length += 2
            else:
                length += 1
        return length

if __name__ == "__main__":
    client = StakeBonusCodeScraper()
    client.setconfig()
    client.mainloop()
