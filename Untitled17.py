#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import tkinter
import numpy as np
import random
import tkinter as tk
import platform
from PIL import Image, ImageTk
from pygame import mixer
from itertools import combinations
import os
import pygame
#exe化する際に使用する外部ファイルをまとめる。
if getattr(sys, 'frozen', False):
    # 実行ファイルが存在する場合
    current_dir = sys._MEIPASS
else:
    # スクリプトが実行されているディレクトリ
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
image_path1 = os.path.join(current_dir, "onpu__test.png")
image_path2 = os.path.join(current_dir, "アオバズクの鳴き声.mp3")
image_path3 = os.path.join(current_dir, "ライオンの鳴き声3.mp3")
image_path4 = os.path.join(current_dir, "猫の鳴き声1.mp3")
image_path5 = os.path.join(current_dir, "馬の鳴き声2.mp3")
image_path6 = os.path.join(current_dir, "ヤギの鳴き声.mp3")
image_path7 = os.path.join(current_dir, "ゾウの鳴き声1.mp3")
image_path8 = os.path.join(current_dir, "イノシシの鳴き声.mp3")
image_path9 = os.path.join(current_dir, "牛の鳴き声.mp3")
image_path10 = os.path.join(current_dir, "オオカミの遠吠え.mp3")
image_path11 = os.path.join(current_dir, "カリフォルニアアシカ1.mp3")
image_path12 = os.path.join(current_dir, "ドバトの鳴き声.mp3")
image_path13 = os.path.join(current_dir, "ニワトリの鳴き声3.mp3")
image_path14= os.path.join(current_dir, "ヒヨコの鳴き声.mp3")
image_path15 = os.path.join(current_dir, "カラスが鳴く夕方.mp3")
image_path16 = os.path.join(current_dir, "エンマコオロギの鳴き声.mp3")
image_path17 = os.path.join(current_dir, "ヒグラシの鳴き声.mp3")
image_path18 = os.path.join(current_dir, "ヒヨドリの鳴き声2.mp3")
image_path19 = os.path.join(current_dir, "トンビの鳴き声.mp3")
image_path20 = os.path.join(current_dir, "インドクジャクの鳴き声.mp3")
image_path21 = os.path.join(current_dir, "usigaeru.mp3")
image_path22 = os.path.join(current_dir, "3940.mp3")
image_path23 = os.path.join(current_dir, "ani_fa_doragon03.mp3")
image_path24 = os.path.join(current_dir, "ani_ge_kujira01.mp3")
image_path25 = os.path.join(current_dir, "onpu2__test.png")
image_path26 = os.path.join(current_dir, "hukidasix.png")
image_path27 = os.path.join(current_dir, "player.png")
image_path28 = os.path.join(current_dir, "text_versus_vs.png")
image_path29 = os.path.join(current_dir, "tukue.png")
image_path30 = os.path.join(current_dir, "white_tree.png")
image_path31 = os.path.join(current_dir, "charactor.png")
image_path32 = os.path.join(current_dir, "charactor1.png")
image_path33 = os.path.join(current_dir, "918950.png")
image_path34 = os.path.join(current_dir, "ボタン.png")
image_path35 = os.path.join(current_dir, "ボタン1.png")
image_path36 = os.path.join(current_dir, "ボタン２.png")
image_path37 = os.path.join(current_dir, "ボタン３.png")
image_path38 = os.path.join(current_dir, "ボタン4.png")
image_path39 = os.path.join(current_dir, "ボタン5.png")
image_path40 = os.path.join(current_dir, "ボタン6.png")
image_path41 = os.path.join(current_dir, "choice_button.png")
image_path42 = os.path.join(current_dir, "choice_button1.png")
image_path43 = os.path.join(current_dir, "charactor2.png")
image_path44 = os.path.join(current_dir, "charactor3.png")
image_path45 = os.path.join(current_dir, "ボタン_target.png")
image_path46 = os.path.join(current_dir, "ボタン1_target.png")
image_path47 = os.path.join(current_dir, "ボタン２_target.png")
image_path48 = os.path.join(current_dir, "ボタン３_target.png")
image_path49 = os.path.join(current_dir, "ボタン4_target.png")
image_path50 = os.path.join(current_dir, "ボタン5_target.png")
image_path51 = os.path.join(current_dir, "ボタン6_target.png")
image_path52 = os.path.join(current_dir, "choice_button_target.png")
image_path53 = os.path.join(current_dir, "choice_button1_target.png")
image_path54 = os.path.join(current_dir, "onpu__test_target.png")
image_path55 = os.path.join(current_dir, "onpu2__test_target.png")
image_path56 = os.path.join(current_dir, "button04.mp3")
image_path57 = os.path.join(current_dir, "button12.mp3")
image_path58 = os.path.join(current_dir, "button40.mp3")
image_path59 = os.path.join(current_dir, "button45.mp3")
image_path60 = os.path.join(current_dir, "button55.mp3")
image_path61 = os.path.join(current_dir, "playericon.ico")
game_mode=['モ','ー','ド','を','選','ん','で','ね']
game_VS=['対','戦','す','る','相','手','を','選','ん','で','ね']
coin=list(range(4))#カードを並べるときに4分の一の確率で一度置いた同じ数字(music)のカードを再度置く。
root = tkinter.Tk()
root.geometry("1100x800")
root.title(u"音感衰弱")

root.configure(background="#006400")
current_width = root.winfo_width()
current_height = root.winfo_height()
canvas = tk.Canvas(root,width=156, height=250,bg="#006400",highlightthickness=0)#試合中の左上に配置されているプレイヤー１のスコアと画像を表示
canvas1 = tk.Canvas(root,width=156, height=250,bg="#006400",highlightthickness=0)#試合中の左上に配置されているプレイヤー２のスコアと画像を表示
canvas2 = tk.Canvas(root,width=400, height=185,bg="#006400",highlightthickness=0)#試合中の真上に配置されているVS画像のスコアとされのターンかを表示

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
haikei = tk.Canvas(root, width=screen_width, height=screen_height)#モード選びおよび対戦相手選びの画面全体
haikei_clear = tk.Canvas(root, width=screen_width, height=screen_height,bg="#006400")#対戦結果の時の画面全体

frame = tk.Canvas(root,width=800, height=600,bg="#006400",highlightthickness=0)#カードを表示する画面
canvas_frame=tk.Canvas(frame,width=600, height=395,bg="#333333",highlightthickness=1)#試合中にタイトル画面(haikei)に戻るかの選択画面
image_test = Image.open(image_path1)
photo_test = ImageTk.PhotoImage(image_test)
image = Image.open(image_path1)
photo = ImageTk.PhotoImage(image)
image = Image.open(image_path25)
photo1 = ImageTk.PhotoImage(image)
image = Image.open(image_path26)
photo2 = ImageTk.PhotoImage(image)
image = Image.open(image_path27)
photo3 = ImageTk.PhotoImage(image)
image = Image.open(image_path28)
photo4 = ImageTk.PhotoImage(image)
image =Image.open(image_path29)
photo5 = ImageTk.PhotoImage(image)
image = Image.open(image_path30)
photo6 = ImageTk.PhotoImage(image)
image = Image.open(image_path31)
photo7 = ImageTk.PhotoImage(image)
image = Image.open(image_path32)
photo8 = ImageTk.PhotoImage(image)
image9 =Image.open(image_path33)
resized_image = image9.resize((screen_width, screen_height), Image.ANTIALIAS)
photo9= ImageTk.PhotoImage(resized_image)
image = Image.open(image_path34)
photo10 = ImageTk.PhotoImage(image)
image = Image.open(image_path35)
photo11 = ImageTk.PhotoImage(image)
image = Image.open(image_path36)
photo12 = ImageTk.PhotoImage(image)
image = Image.open(image_path37)
photo13 = ImageTk.PhotoImage(image)
image = Image.open(image_path38)
photo14 = ImageTk.PhotoImage(image)
image = Image.open(image_path39)
photo15 = ImageTk.PhotoImage(image)
image = Image.open(image_path40)
photo16 = ImageTk.PhotoImage(image)
image = Image.open(image_path41)
photo17 = ImageTk.PhotoImage(image)
image = Image.open(image_path42)
photo18 = ImageTk.PhotoImage(image)
image = Image.open(image_path43)
photo19 = ImageTk.PhotoImage(image)
image = Image.open(image_path44)
photo20 = ImageTk.PhotoImage(image)
image = Image.open(image_path45)
photo21 = ImageTk.PhotoImage(image)
image = Image.open(image_path46)
photo22 = ImageTk.PhotoImage(image)
image = Image.open(image_path47)
photo23 = ImageTk.PhotoImage(image)
image = Image.open(image_path48)
photo24 = ImageTk.PhotoImage(image)
image = Image.open(image_path49)
photo25 = ImageTk.PhotoImage(image)
image = Image.open(image_path50)
photo26 = ImageTk.PhotoImage(image)
image = Image.open(image_path51)
photo27 = ImageTk.PhotoImage(image)
image = Image.open(image_path52)
photo28 = ImageTk.PhotoImage(image)
image = Image.open(image_path53)
photo29 = ImageTk.PhotoImage(image)
image = Image.open(image_path54)
photo30 = ImageTk.PhotoImage(image)
image = Image.open(image_path55)
photo31 = ImageTk.PhotoImage(image)
class GAME():
    def __init__(self):
        self.click=0 #CPUまたはプレイヤーの2進数上のボタンのクリック回数
        self.CPU_choice_list=[] #プレイヤーまたはCPUがめくったカードの情報を記録するリスト
        self.level=0 #self.CPU_choice_listが記憶できる量の値を調整する変数
        self.mode=0.0 #選んだモードによるカードの全体の枚数とself.levelの値を調整してself.CPU_choice_listに記憶できる量を調整
        self.choice_tup=[] #CPUのターンでクリック数がself.click%2=0回の時にCPU_choice_list内で同じカード(music)が２つ以上あるとそのカードのうちの一つを格納する。
        self.tapul=(0,0,None) #CPU_choice_listに含まれるカード情報
        self.text_id=[]#
        self.sqr=0 #タイトル画面、ゲーム画面、リザルト画面等を選別して使う変数
        self.count=0 #タイトル画面において吹き出しの中のテキストを１文字事読み込むのに使う。
        self.player1=0 #プレイヤー１のスコア
        self.player2=0 #プレイヤー2またはCPUのスコア
        self.music1=0 #self.clickが０のときのカードのmusic情報を保存するための変数
        self.card=0 #カードの横並びの変数
        self.card1=0 #カードの縦並びの変数
        self.pt=0 #何枚モードが選んだ際に
        self.trash=-1 #self.tapul内におけるmusicの値を変更し、邪魔な情報にするための変数
        self.button1=None #self.clickが０のときのカードのbutton情報を保存するための変数
        self.all_buttons=[] #カードが生成されるたびにそのカードのbutton情報を格納する
        self.music_box=[] #musicの値を格納する
        self.music_sort=[] #そのカードのmusic情報を番号順に格納する
        self.id=[] #CPUがランダムで選ぶカードを格納する
        self.id_count=0 #カードを並べる際に何番目のカードなのかを追加情報として与える。
        self.id_count1=0 #self.clickが０のときのカードのid情報を保存するための変数
        self.pt=0 #何枚モードを選んだあとの場合分けの変数
        self.turn=1 #相手ターンか自分ターンかを区別する変数
        self.choice1=-1 #CPUが何番目のカードかを表す変数
        self.current_image =None #タイトル画面の切り替え画像に使う初期値
        self.tup_choiced=None #self.clickが０回の時にどのタプル(カード)を選んだかを示す変数
        self.after_id=None #画像を切り替える関数を呼び出す
        self.after_id1=None #一文字づつ出力する関数を呼び出す
    def button_click(self,button,music,photo,this_id):#カードをクリックした際に
        if music==0:
            audio_path = image_path2
        if music==1:
            audio_path = image_path3
        if music==2:
            audio_path = image_path4
        if music==3:
            audio_path = image_path5
        if music==4:
            audio_path = image_path6
        if music==5:
            audio_path = image_path7
        if music==6:
            audio_path = image_path8
        if music==7:
            audio_path = image_path9
        if music==8:
            audio_path = image_path10
        if music==9:
            audio_path = image_path11
        if music==10:
            audio_path = image_path12
        if music==11:
            audio_path = image_path13
        if music==12:
            audio_path = image_path14
        if music==13:
            audio_path = image_path15
        if music==14:
            audio_path = image_path16
        if music==15:
            audio_path = image_path17
        if music==16:
            audio_path = image_path18
        if music==17:
            audio_path = image_path19
        if music==18:
            audio_path = image_path20
        if music==19:
            audio_path = image_path21
        if music==20:
            audio_path = image_path22
        if music==21:
            audio_path = image_path23
        if music==22:
            audio_path = image_path24
        #musicの値によってaudio_pathに含まれる音声データを決定し、読み込む
        mixer.init()
        mixer.music.load(audio_path)
        mixer.music.play()
        
        self.tapul=(music,this_id,button)
        #self.CPU_choice_list内にself.tapulが含まれているかどうかを判定する変数
        contains_target_button = any((music, this_id, button) == tup for tup in self.CPU_choice_list)
        
        if self.click==0:
            self.music1=music
            self.button1=button
            frame.itemconfig(button, image=photo1) #その押したボタンの画像を切り替える
            frame.tag_bind(button, '<Enter>',lambda event: on_enter_button(button,frame,photo31))
            frame.tag_bind(button, '<Leave>', lambda event: on_leave_button(button,frame,photo1))
            self.music_exe() #audio_pathの音声ファイルを出力する
            self.click=1
            self.id_count1=this_id                        
            if contains_target_button==False: #self.CPU_choice_list内にself.tapulが含まれていなければそのタプルを追加
                self.CPU_choice_list.append(self.tapul) 
            #CPUが同じmusicを持ったタプルを二つ選ぶ際に、self.click=0のときに選んだself.tapulを次のクリックの時に除外するために行う
            self.choice_tup.append(self.tapul)            
            game.tup_choiced=self.tapul
            deleate_label()
        elif self.click==1: #self.click=0の時に選んだbuttonと同じボタンではないときは処理を進める
            if self.button1!=button:
                frame.itemconfig(button, image=photo1)
                frame.tag_bind(button, '<Enter>',lambda event: on_enter_button(button,frame,photo31))
                frame.tag_bind(button, '<Leave>', lambda event: on_leave_button(button,frame,photo1))
                self.music_exe()
            else:
                return
            self.choice_tup.clear() #ここで選んだカード２枚が確定するのでchoice_tupの中身を削除する
            self.click=0
            if self.music1==music: #選んだカードのmusic値がself.click=0の時に選んだカードのmusic値と同じなら以下の処理を進める
                frame.delete(button) #今回選んだカードを盤面から削除
                frame.delete(self.button1) #self.click=0の時に選んだカードを盤面から削除
                self.id.remove(this_id) #今回選んだカードのID情報を盤面から削除
                self.id.remove(self.id_count1) #self.click=0の時に選んだカードのID情報を盤面から削除
                self.point_player() #player1 or player2のどちらかにスコアを加算する
                if contains_target_button==False:
                    self.CPU_choice_list.append(self.tapul)
                for tup in game.CPU_choice_list:
                    #tup[0]はCPU_choice_list内のタプルにおけるmusicの値を表しており、今回選んだmusic値と同じmusic値を持っているタプルに対して以下の処理をする
                    if tup[0]==music:
                        game.CPU_choice_list.remove(tup) #そのタプルの要素をCPU_choice_listから削除する
                        tup3=(self.trash,-1,None) #邪魔な要素
                        game.CPU_choice_list.append(tup3) #先ほど削除したタプルの代わりに邪魔な要素をリストに追加
                        self.trash-=1 #数字を更新していくことでCPU関数内で同じmusic値として邪魔な要素が反映されないようにする
                deleate_label()
            
            else: #選んだカードのmusic値がself.click=0の時に選んだカードのmusic値と違う場合
                button_before=self.button1 #これを宣言せずにself.button1でtag_bindを行うと次に更新されるself.button1にもtag_bindが反映されるのを防ぐため
                #このターン中に押されたbuttonの画像情報を押される前に戻す
                frame.itemconfig(button, image=photo)
                frame.tag_bind(button, '<Enter>',lambda event: on_enter_button(button,frame,photo30))
                frame.tag_bind(button, '<Leave>', lambda event: on_leave_button(button,frame,photo))
                frame.itemconfig(self.button1, image=photo)
                frame.tag_bind(button_before, '<Enter>',lambda event: on_enter_button(button_before,frame,photo30))
                frame.tag_bind(button_before, '<Leave>', lambda event: on_leave_button(button_before,frame,photo))
                #ターンを変える
                if self.turn==1:
                    self.turn=2
                else:
                    self.turn=1
                if contains_target_button==False:
                    self.CPU_choice_list.append(self.tapul)
                deleate_label()
    def point_player(self):
        if self.turn==1:
            self.player1+=1
        else:
            self.player2+=1
            
    def music_box1_choice(self): #music_box1からカードを取り出す
        x=random.choice(self.music_box1)
        self.music_box1.remove(x)
        return x
    
    #盤面のカードで同じmusic値を持つカード２枚を生成するためにmusic_boxから値を取り出したらその値と同じ値をmusic_box1に格納する
    def music_box_choice(self): 
        x=random.choice(self.music_box)
        self.music_box.remove(x)
        self.music_box1.append(x)
        return x
    #music_box1の中身が何もない場合はそのままmusic_boxから値を取り出す。そうでなけばcoinリストから4分の１の確率でmusic_box1から値を取り出す
    def music_choice1(self):
        if len(self.music_box1)==0:
            x=self.music_box_choice()
        else:
            hantei=random.choice(coin)
            if hantei==0:
                x=self.music_box1_choice()
            else:
                x=self.music_box_choice()
            
        return x
    #モードの枚数とmusic_boxの要素数に応じてmusic_boxから値を取り出すかmusic_box1から取り出すかを決める
    def music_choice(self):
        if self.pt==1:
            if len(self.music_box)>3:
                x=self.music_choice1()
            else:
                x=self.music_box1_choice()
        elif self.pt==2:
            if len(self.music_box)>7:
                x=self.music_choice1()
            else:
                x=self.music_box1_choice()
        elif self.pt==3:
            if len(self.music_box)>11:
                x=self.music_choice1()
            else:
                x=self.music_box1_choice()
        return x
    def music_exe(self):
        if root.winfo_exists():  # ウィンドウがまだ存在しているか確認
            for button in self.all_buttons: #all_buttons内に入っているbuttonはこのmusic_exe関数の音が流れている間は押すことが出来ないようにする
                frame.itemconfig(button, state=tk.DISABLED)
            while mixer.music.get_busy():
                root.update()
            for button in self.all_buttons:
                frame.itemconfig(button, state=tk.NORMAL)
    def create_button(self,row,column): #１枚１枚のカードを生成する
        x=self.music_choice()
        self.music_sort.append(x)
        count_id=self.id_count
        button = frame.create_image(column * 75+105, row * 75+125, anchor=tk.NW, image=photo, tags=f"button_{row}_{column}")
        frame.tag_bind(button, '<Enter>',lambda event: on_enter_button(button,frame,photo30))
        frame.tag_bind(button, '<Leave>', lambda event: on_leave_button(button,frame,photo))
        frame.tag_bind(button, '<Button-1>', lambda event, r=row, c=column: self.button_click(button, x, photo,count_id))
        self.id_count+=1
        return button
    def display(self): #生成したカードをframe内に並べる
        for i in range(self.card1):
            for j in range(self.card):
                button = self.create_button(i, j)
                self.all_buttons.append(button)

game=GAME()
def play_sound(audio_this):#audio_thisに代入されている音声のファイルパスを実行する
    pygame.mixer.init()
    pygame.mixer.music.load(audio_this)  
    pygame.mixer.music.play()
def switch_image1():
        # 現在の画像を判別し、次の画像に切り替える
    if game.current_image == photo20:
        game.current_image = photo19
    else:
        game.current_image = photo20
        # 画像を切り替え
    haikei_clear.itemconfig(image_id1, image=game.current_image)
    game.after_id=root.after(500, switch_image1)
def reset(): #試合画面またはゲーム結果の盤面からタイトル画面(main関数)に遷移するときに使う
    root.after_cancel(game.after_id)
    root.after_cancel(game.after_id1)
    frame.delete("all")
    frame.pack_forget()
    canvas.delete("all")
    canvas.pack_forget()
    canvas1.delete("all")
    canvas1.pack_forget()
    canvas2.delete("all")
    canvas2.pack_forget()
def switch_text(): #吹き出し内に書かれている一文字一文字を出力するために使う
    global mode_text
    global mode_VS
    game.count+=1
    if game.sqr==0 and game.count<=7:
        mode_text=haikei.create_text(130+game.count*37,screen_height-550,text="{}".format(game_mode[game.count]),anchor=tk.SW,font=("Helvetica",30))
        game.text_id.append(mode_text)
    elif game.sqr==1 and game.count<=10:
        if game.count<8:
            mode_VS=haikei.create_text(150+game.count*37,screen_height-550,text="{}".format(game_VS[game.count]),anchor=tk.SW,font=("Helvetica",30))
            game.text_id.append(mode_VS)
        else:
            mode_VS=haikei.create_text(150+(game.count-8)*37,screen_height-500,text="{}".format(game_VS[game.count]),anchor=tk.SW,font=("Helvetica",30))
            game.text_id.append(mode_VS)
    game.after_id1=root.after(300, switch_text)
def switch_image():
        # 現在の画像を判別し、次の画像に切り替える
    if game.current_image == photo7:
        game.current_image = photo8
    else:
        game.current_image = photo7
        # 画像を切り替え
    haikei.itemconfig(image_id, image=game.current_image)
    game.after_id=root.after(500, switch_image)
#ゲームリザルト画面でどちらが勝利したのかを表示するときのテキストの大きさを取得するため
def game_over_text(text_this):
    global text_bbox #これがそのテキストの大きさを表す変数
    global text_game_end
    
    text_game_end=haikei_clear.create_text(0,0,text=text_this,anchor=tk.SW,font=("Helvetica",30),fill="black")
    text_bbox = haikei_clear.bbox(text_game_end)
    haikei_clear.delete(text_game_end)
#ゲームリザルト画面でプレイヤー1とプレイヤー2(またはCPU)のスコアを表示するときのテキストの大きさを取得するため
def game_over_text1(text_this1):
    global text_bbox1 #これがそのテキストの大きさを表す変数
    global text_game_end1
    text_game_end1=haikei_clear.create_text(0,0,text=text_this1,anchor=tk.SW,font=("Helvetica",30),fill="black")
    text_bbox1 = haikei_clear.bbox(text_game_end1)
    haikei_clear.delete(text_game_end1)
def game_over(): #ゲームリザルト画面
    global image_id1
    global text_bbox
    global text_game_end
    global text_bbox1
    global text_game_end1
    global return_gameover_button
    reset()    
    game.current_image = photo20
    haikei_clear.pack(fill=tk.BOTH, expand=True)    
    image_id1=haikei_clear.create_image((root.winfo_width()-photo20.width()) // 2, (root.winfo_height()-photo20.height()) // 2,anchor=tk.NW, image=photo20)   
    if game.sqr==3:
        game_over_text1(text_this1="プレイヤー１：{}               プレイヤー２：{}".format(game.player1,game.player2))
        text_game_end1=haikei_clear.create_text((root.winfo_width()- text_bbox1[2]) // 2, (root.winfo_height()- text_bbox1[3])// 2-400,text="プレイヤー１：{}               プレイヤー２：{}".format(game.player1,game.player2),anchor=tk.SW,font=("Helvetica",30),fill="black")
    else:
        game_over_text1(text_this1="プレイヤー１：{}                        CPU：{}".format(game.player1,game.player2))
        text_game_end1=haikei_clear.create_text((root.winfo_width()- text_bbox1[2]) // 2, (root.winfo_height()- text_bbox1[3])// 2-400,text="プレイヤー１：{}              CPU：{}".format(game.player1,game.player2),anchor=tk.SW,font=("Helvetica",30),fill="black")
    
    if game.player1>game.player2: 
        game_over_text(text_this="プレイヤー１の勝利")
        text_game_end=haikei_clear.create_text((root.winfo_width()- text_bbox[2]) // 2, (root.winfo_height()- text_bbox[3])// 2-200,text="プレイヤー１の勝利",anchor=tk.SW,font=("Helvetica",30),fill="black")
    elif game.player1==game.player2:
        game_over_text(text_this="引き分け")
        text_game_end=haikei_clear.create_text((root.winfo_width()- text_bbox[2]) // 2, (root.winfo_height()- text_bbox[3])// 2-200,text="引き分け",anchor=tk.SW,font=("Helvetica",30),fill="black")
    else:
        if game.sqr==3:
            game_over_text("プレイヤー２の勝利")
            text_game_end=haikei_clear.create_text((root.winfo_width()- text_bbox[2]) // 2, (root.winfo_height()- text_bbox[3])// 2-200,text="プレイヤー２の勝利",anchor=tk.SW,font=("Helvetica",30),fill="black")
        else:
            game_over_text("CPUの勝利")
            text_game_end=haikei_clear.create_text((root.winfo_width()- text_bbox[2]) // 2, (root.winfo_height()- text_bbox[3])// 2-200,text="CPUの勝利",anchor=tk.SW,font=("Helvetica",30),fill="black")
    return_gameover_button=haikei_clear.create_image((root.winfo_width()-photo11.width()) // 2, (root.winfo_height()-photo11.height()) // 2-100,anchor=tk.NW, image=photo11)
    canvas_UI(haikei_clear,return_gameover_button,photo22,photo11,return_4)
    game.sqr=5
    on_resize()
    game.after_id=root.after(500, switch_image1)

def return_4(event): #ゲームリザルト画面からゲームタイトル画面に戻る際の関数
    play_sound(image_path58)
    root.after_cancel(game.after_id)
    haikei_clear.delete("all")
    haikei_clear.pack_forget()
    game.__init__()
    haikei_main=haikei.create_image(0, 0,anchor=tk.NW,image=photo9)
    main()
def return_3(event):#試合中にタイトル画面に戻りたいかどうかのキャンバスを生成するための関数
    play_sound(image_path58)
    frame.delete(return_title_button)
    canvas_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    game.all_buttons.pop(len(game.all_buttons)-1)
    canvas_frame.create_text(90,150,text="タイトルに戻りますか？",anchor=tk.SW,font=("Helvetica",30),fill="white")
    yes=canvas_frame.create_text(150,300,text="はい",anchor=tk.SW,font=("Helvetica",30),fill="white")
    canvas_frame.tag_bind(yes, '<Enter>',lambda event: on_enter_yes(yes,canvas_frame))
    canvas_frame.tag_bind(yes, '<Leave>', lambda event: on_leave_yes(yes,canvas_frame))
    canvas_frame.tag_bind(yes, '<Button-1>', lambda event: click_yes(canvas_frame))
    no=canvas_frame.create_text(350,300,text="いいえ",anchor=tk.SW,font=("Helvetica",30),fill="white")
    canvas_frame.tag_bind(no, '<Enter>',lambda event: on_enter_no(no,canvas_frame))
    canvas_frame.tag_bind(no, '<Leave>', lambda event: on_leave_no(no,canvas_frame))
    canvas_frame.tag_bind(no, '<Button-1>', lambda event: click_no(canvas_frame))
def return_2(event): #CPUのレベルを決める画面から戻る際の関数
    global button_24
    play_sound(image_path58)
    game.level=0
    new_canvas.delete("all")
    new_canvas.place_forget()
    button_24=haikei.create_image(root.winfo_width() // 2+300, root.winfo_height() // 2+300, image=photo11, anchor=tk.NW)
    canvas_UI(haikei,button_24,photo22,photo11,return_1)
def return_1(event): #対戦相手を決める画面からモードの枚数を決める画面に戻るさいの関数
    play_sound(image_path58)
    root.after_cancel(game.after_id)
    root.after_cancel(game.after_id1)
    game.__init__()
    haikei.delete(hukidasi)
    haikei.delete(button_24)
    haikei.delete(button_32)
    haikei.delete(button_40)
    haikei.delete(image_id)
    main()
def on_enter_button(object1,new_canvas,photo_main):
    new_canvas.itemconfig(object1, image=photo_main)
def on_leave_button(object1,new_canvas,photo_main2):
    new_canvas.itemconfig(object1, image=photo_main2)
def on_enter_no(no,canvas_frame):
    canvas_frame.itemconfig(no, fill="red")
def on_leave_no(no,canvas_frame):
    canvas_frame.itemconfig(no, fill="white")
def on_enter_yes(yes,canvas_frame):
    canvas_frame.itemconfig(yes, fill="red")
def on_leave_yes(yes,canvas_frame):
    canvas_frame.itemconfig(yes, fill="white")
    
def click_no(canvas_frame): #試合中からタイトル画面に戻るのを拒否し、試合を続行する際の関数
    global return_title_button
    play_sound(image_path59)
    canvas_frame.delete("all")
    canvas_frame.place_forget()
    return_title_button=frame.create_image(700,550,image=photo11)
    canvas_UI(frame,return_title_button,photo22,photo11,return_3)
    game.all_buttons.append(return_title_button)
def click_yes(canvas_frame): #試合中からタイトル画面に戻りたいときの関数
    play_sound(image_path57)
    canvas_frame.delete("all")
    canvas_frame.place_forget()
    reset()
    game.__init__()
    haikei_main=haikei.create_image(0, 0,anchor=tk.NW,image=photo9)
    main()
def game_lets_play(): #試合を始める際にやらなければいけないこと試合画面の設定を行う関数
    global label
    global label_turn
    global return_title_button
    play_sound(image_path56)
    game.id=list(range(game.card*game.card1))
    for i in range(len(game.text_id)):
        haikei.delete(game.text_id[i])
    game.text_id=[]
    game.count=0
    haikei.delete("all")
    haikei.pack_forget()
    canvas.pack(side="left", anchor="n")
    canvas1.pack(side="right", anchor="n")
    canvas2.pack(anchor="n")
    VS=canvas2.create_image(100,0,anchor=tk.NW,image=photo4)
    label_turn=canvas2.create_text(200,170,text="プレイヤー{}のターン".format(game.turn),font=("Helvetica",25))
    canvas1.create_image(0,0,anchor=tk.NW,image=photo3)
    canvas.create_image(0,0,anchor=tk.NW,image=photo3)
    label=canvas.create_text(70,190,text="プレイヤー１\nスコア:{}".format(game.player1),font=("Helvetica",15))
    frame.pack(anchor="n")
    frame.create_image(400,300,image=photo5)
    return_title_button=frame.create_image(700,550,image=photo11)
    canvas_UI(frame,return_title_button,photo22,photo11,return_3)
    game.display()
    game.all_buttons.append(return_title_button)  
def game_mode_(): #モードの枚数を選んだあとに誰と対戦するかを決める画面に設定する際の関数
    global button_40
    global button_32
    global button_24
    global mode_VS
    play_sound(image_path60)
    current_width = root.winfo_width()
    current_height = root.winfo_height()
    game.music_box=[]
    game.music_box1=[]
    game.music_box=list(range(23))
    game.turn=1
    game.sqr=1
    for i in range(len(game.text_id)):
        haikei.delete(game.text_id[i])
    game.text_id=[]
    game.count=0
    haikei.delete(button_40)
    haikei.delete(button_32)
    haikei.delete(button_24)
    
    button_40=haikei.create_image(current_width // 2+100, current_height // 2-300, image=photo14, anchor=tk.NW)
    canvas_UI(haikei,button_40,photo25,photo14,game_play)
    button_32=haikei.create_image(current_width // 2+100, current_height // 2-100, image=photo15, anchor=tk.NW)
    canvas_UI(haikei,button_32,photo26,photo15,open_new_window)
    button_24=haikei.create_image(current_width // 2+300, current_height // 2+300, image=photo11, anchor=tk.NW)
    canvas_UI(haikei,button_24,photo22,photo11,return_1)
    mode_VS=haikei.create_text(150,screen_height-550,text="{}".format(game_VS[game.count]),anchor=tk.SW,font=("Helvetica",30))
    game.text_id.append(mode_VS)
    
def game_play(event): #プレイヤー同士と戦う際のラベルとsqrの設定
    global label1    
    game.sqr=3    
    game_lets_play()
    label1=canvas1.create_text(60,190,text="プレイヤー2\nスコア:{}".format(game.player2),font=("Helvetica",15))
    deleate_label()
def game＿CPU(event): #CPUと戦う際のラベルとsqrの設定
    global label1
    game.sqr=4
    new_canvas.delete("all")
    new_canvas.place_forget()
    new_frame.delete("all")
    new_frame.place_forget()
    game_lets_play()
    label1=canvas1.create_text(60,190,text="CPUレベル{}\nスコア:{}".format(game.level,game.player2),font=("Helvetica",15))
    deleate_label()
def game1_1(event): #40枚モードを選んだ際に設定する関数
    game.card=8
    game.card1=5
    game.pt=1
    game.mode=4.0
    game_mode_()
def game2_2(event): #32枚モードを選んだ際に設定する関数
    game.card=8
    game.card1=4
    game.pt=2
    game.mode=3.2
    game_mode_()
def game3_3(event): #24枚モードを選んだ際に設定する関数
    game.card=8
    game.card1=3
    game.pt=3
    game.mode=2.4
    game_mode_()
def main(): #モードを選ぶ最初の関数、タイトル画面
    global image_id
    global button_40
    global button_32
    global button_24
    global mode_text
    global hukidasi
    haikei.pack(fill=tk.BOTH, expand=True)
    game.current_image = photo7
    image_id = haikei.create_image(100, screen_height-150,anchor=tk.SW, image=photo7)
    hukidasi=haikei.create_image(100, screen_height-450,anchor=tk.SW, image=photo2)
    button_40=haikei.create_image(current_width // 2+100, current_height // 2-300, image=photo12, anchor=tk.NW)
    canvas_UI(haikei,button_40,photo23,photo12,game1_1)
    button_32=haikei.create_image(current_width // 2+100, current_height // 2-100, image=photo13, anchor=tk.NW)
    canvas_UI(haikei,button_32,photo24,photo13,game2_2)
    button_24=haikei.create_image(current_width // 2+100, current_height // 2+100, image=photo10, anchor=tk.NW)
    canvas_UI(haikei,button_24,photo21,photo10,game3_3)
    mode_text=haikei.create_text(130,screen_height-550,text="{}".format(game_mode[game.count]),anchor=tk.SW,font=("Helvetica",30))
    game.text_id.append(mode_text)
    root.after(500, switch_image)
    game.after_id1=root.after(300, switch_text)
    on_resize()
#お互いのスコアまた誰のターンなのかを更新するためにラベルを削除する関数。また、ゲームが終了したかどうかを判定する関数。
def deleate_label():
    canvas.delete(label)
    canvas1.delete(label1)
    canvas2.delete(label_turn)
    if (game.player1+game.player2)==(game.card*game.card1)/2:
        game_over()
    main1_pt()
#新たに互いのスコアまた誰のターンなのかを更新するためにラベルを生成する関数。また、戦っている相手によって遷移する関数を決める。
def main1_pt():
    global label
    global label1
    global label_turn
    if game.sqr==3:
        label=canvas.create_text(80,190,text="プレイヤー１\nスコア:{}".format(game.player1),font=("Helvetica",15))
        label1=canvas1.create_text(60,190,text="プレイヤー2\nスコア:{}".format(game.player2),font=("Helvetica",15))
        label_turn=canvas2.create_text(200,170,text="プレイヤー{}のターン".format(game.turn),font=("Helvetica",25))
    elif game.sqr==4:
        label=canvas.create_text(80,190,text="プレイヤー１\nスコア:{}".format(game.player1),font=("Helvetica",15))
        label1=canvas1.create_text(60,190,text="CPUレベル{}\nスコア:{}".format(game.level,game.player2),font=("Helvetica",15))
        if game.turn==1:
            label_turn=canvas2.create_text(200,170,text="プレイヤー1のターン",font=("Helvetica",25))
        else:
            label_turn=canvas2.create_text(200,170,text="CPUのターン",font=("Helvetica",25))  
    if game.sqr==3:
        main1()
    if game.sqr==4:
        CPU()
    
def main1(): #プレイヤー２と戦っているときの最終関数。特に何もしない。
    return

def CPU(): #CPUと戦っているときの最終関数
    #CPU_choice_listをCPUのレベルとモードの枚数によって記憶できる領域を決め、それを超えたらCPU_choice_listの先頭を削除
    if float(game.level*game.mode)<float(len(game.CPU_choice_list)):
        game.CPU_choice_list.pop(0)
    if game.turn==2: #CPUのターンのとき
        hantei=False
        for tup in game.CPU_choice_list: #まず、CPU_choice_list内のタプルの情報を確認する。
            #そこでtup[0]というmusic値において同じ値が2つあるときにTrueを代入する。
            if sum(1 for t in game.CPU_choice_list if t[0] == tup[0]) == 2:               
                hantei=True
        
        if hantei==True:
            #CPU_choice_list内の全てのタプルの要素において二つのタプルの組み合わせを全て網羅する
            for tup1, tup2 in combinations(game.CPU_choice_list, 2):
                
                if tup1[0] == tup2[0]: #1番目の要素(music)が同じ場合
                    if game.click==0: #現在のクリック回数が0回ならどちらかのタプルを決めて、そのタプルの情報を元にbuttonをクリックする
                        game.choice_tup.append(tup1)
                        game.choice_tup.append(tup2)
                        game.tup_choiced=random.choice(game.choice_tup)
                        game.choice_tup.clear()
                        game.button_click(game.tup_choiced[2],game.tup_choiced[0],photo_test,game.tup_choiced[1])
                        break
                        
                    else: #現在のクリック回数が1回なら0回の時にクリックしたタプルとは別のもう一つのタプルの情報を元にbuttonをクリックする
                        if any(game.tup_choiced == tup1 for tup in game.choice_tup):
                            game.button_click(tup2[2],tup2[0],photo_test,tup2[1])
                            break
                        else:
                            game.button_click(tup1[2],tup1[0],photo_test,tup1[1])
                            break
        else: #CPU_choice_list内に同じmusic値を持ったタプルが存在しないとき
            choice=game.choice1 #クリック数が0回の時に選んだカードを保存
            #何番目のカード(タプル)を指定するか決めるときにクリック数が0回の時のカードと同じカードを指定したら再度別のカードを指定するまで続ける
            while choice==game.choice1:           
                choice=random.choice(game.id)
            #以下は指定した番号をそれぞれの情報更新してボタンをクリックする
            game.choice1=choice
            music_choice=game.music_sort[choice]
            button_choice=game.all_buttons[choice]
            game.button_click(button_choice,music_choice,photo_test,choice)
                
                
                
def level_down_(event): #CPUのレベルを一つ下げる関数
    global level
    global new_frame
    global level_up
    play_sound(image_path59)
    if game.level==10:
        level_up=new_canvas.create_image(377,205,anchor=tk.W,image=photo17)
        canvas_UI(new_canvas,level_up,photo28,photo17,level_up_)
    game.level-=1
    new_frame.delete(level)
    level=new_frame.create_text(50,50,text="{}".format(game.level),font=("Helvetica",50))
    if game.level==0:
        new_canvas.delete(level_down)
def level_up_(event): #CPUのレベルを一つ上げる関数
    global level
    global new_frame
    global level_down
    play_sound(image_path59)
    if game.level==0:
        level_down=new_canvas.create_image(150,205,image=photo18)
        canvas_UI(new_canvas,level_down,photo29,photo18,level_down_)
    game.level+=1
    new_frame.delete(level)
    level=new_frame.create_text(50,50,text="{}".format(game.level),font=("Helvetica",50))
    if game.level==10:
        new_canvas.delete(level_up)
def open_new_window(event): #対戦を相手をCPUにする際にCPUのレベルを設定する際の関数
    global level
    global new_frame
    global level_up
    global new_canvas
    play_sound(image_path59)
    haikei.delete(button_24)
    new_canvas = tk.Canvas(haikei, width=550, height=400, bg="#006400")
    new_canvas.place(relx=0.5, rely=0.4, anchor=tk.W)
    return_button=new_canvas.create_image(185,370,anchor=tk.W,image=photo11)
    canvas_UI(new_canvas,return_button,photo22,photo11,return_2)
    new_frame=tk.Canvas(new_canvas, width=100, height=100, bg="white")
    new_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    level=new_frame.create_text(50,50,text="{}".format(game.level),font=("Helvetica",50))
    level_up=new_canvas.create_image(377,205,anchor=tk.W,image=photo17)
    canvas_UI(new_canvas,level_up,photo28,photo17,level_up_)
    start=new_canvas.create_image(150,300,anchor=tk.W,image=photo16)
    canvas_UI(new_canvas,start,photo27,photo16,game＿CPU)
    CPUlevel=new_canvas.create_text(290,100,text="CPUのレベルを選んでください。",font=("Helvetica",20))    
    on_resize()
def canvas_UI(new_canvas,object1,photo_main,photo_main2,func):# マウスがUIに対して行った操作に対するコールバック関数を返す
    new_canvas.tag_bind(object1, '<Enter>',lambda event: on_enter_button(object1,new_canvas,photo_main))# マウスがボタン上に乗ったときに対するコールバック関数を設定
    new_canvas.tag_bind(object1, '<Leave>', lambda event: on_leave_button(object1,new_canvas,photo_main2))# マウスがボタン上から離れたときに対するコールバック関数を設定
    new_canvas.tag_bind(object1, '<Button-1>', func)# マウスがボタンをクリックしたときに対するコールバック関数を設定
def on_resize(): #それぞれ画像の配置をウィンドウのサイズに合わせて自動的に調整する関数
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    
    # ウィンドウサイズに合わせて画像を再設定
    resized_image = image9.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(resized_image)

    # キャンバスの背景画像を更新
    if game.sqr==5:
        haikei_clear.coords(image_id1, (new_width-game.current_image.width()) // 2, (new_height-game.current_image.height()) // 2)
        haikei_clear.coords(text_game_end, (new_width- text_bbox[2]) // 2, (new_height- text_bbox[3]) // 2-200)
        haikei_clear.coords(return_gameover_button, (new_width-photo11.width()) // 2, (new_height-photo11.height()) // 2+200)
        haikei_clear.coords(text_game_end1, (new_width- text_bbox1[2]) // 2, (new_height- text_bbox1[3]) // 2-300)
    haikei.itemconfig(haikei_main, image=photo)
    haikei.image = photo
    haikei.config(width=new_width, height=new_height)
    haikei.coords(button_40, new_width // 2+100, new_height // 2-300)
    haikei.coords(button_32, new_width // 2+100, new_height // 2-100)
    
    # ガベージコレクションの防止
    if game.sqr==0:                
        haikei.coords(button_24, new_width // 2+100, new_height // 2+100)
    elif game.sqr==1:
        haikei.coords(button_24, new_width // 2+300, new_height // 2+300)

def on_closing():
    root.destroy()

haikei_main=haikei.create_image(0, 0,anchor=tk.NW,image=photo9)
root.bind("<Configure>", lambda event: root.after(1, on_resize)) #ウィンドウのサイズが変更されたときに呼び出す
root.protocol("WM_DELETE_WINDOW", on_closing) #ウィンドウを閉じたときに呼び出す
main()
root.iconbitmap(image_path61) #アイコン画像設定
root.mainloop()


# In[ ]:





# In[ ]:




