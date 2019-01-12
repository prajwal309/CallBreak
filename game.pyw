from tkinter import *
from math import sin, cos, pi
from random import randrange
from time import time, sleep
#from winsound import Beep

master= Tk()
master.title("Call Break")
#master.wm_iconbitmap('Icon.ico')
master.geometry("700x600")
master.resizable(width=False, height=False)

def animation(text_entry):
  global screen
  screen=Canvas(master, width=800, height=800)
  screen.pack()
  big_rad = 250
  x_cen = 350
  y_cen = 300
  counter = 0
  counter1 = 0
  initial_time = time()
  color = ["#ff3433","#223433","#1dfd3f","#4f93fc","#f456f7","#31ff33"]
  screen.create_text(350,300,text=text_entry,font=('Helvetica',30), fill="red")

  for small_rad in range(50,175,25):
    while counter<2*pi:
      current_time = time()
      time_diff = current_time-initial_time
      if time_diff>0.0005:
        master.update()
        xpos1 = x_cen+big_rad*cos(counter)+ small_rad*sin(counter1)
        ypos1 = y_cen+big_rad*sin(counter)+small_rad*cos(counter1)
        xpos2 = x_cen+big_rad*cos(counter+0.001)+small_rad*sin(counter1+0.01)
        ypos2 = y_cen+big_rad*sin(counter+0.001)+small_rad*cos(counter1+.01)

        screen.create_line(xpos1,ypos1,xpos2,ypos2,fill=color[randrange(0,len(color)-1)],width=randrange(1,6))
        counter+=0.001
        counter1+=0.01
    counter = 0
    counter1 = 0
############################################animation

def credit():
    credit_win = Toplevel(master)
    #credit_win.wm_iconbitmap('Icon.ico')
    credit_win.geometry("200x70")
    credit_win.resizable(width=False, height=False)
    credit_win.title("Credit")

    creator = "Prajwal Niraula \n Saint Peter's University \n Jersey City, NJ \n prajwalniraula@gmail.com"
    Label(credit_win, text=creator).pack()

def confirmation():
  confirm_win = Toplevel(master)
  #confirm_win.wm_iconbitmap('Icon.ico')
  confirm_win.title("Confirming")
  confirm_win.resizable(width=False, height=False)

  f1 = Frame(confirm_win, borderwidth = 2, width=300, height = 200)
  Label(f1,text="Do you want to quit?").pack(pady=8)
  Button(f1,borderwidth = 2, text="Yes", command=master.destroy).pack(side=LEFT,padx=15,pady=8)
  Button(f1,borderwidth = 2, text="No", command=confirm_win.destroy).pack(side=LEFT,padx=15,pady=8)
  f1.pack(padx=50, pady=10)


def name_entry():
  gamemenu.entryconfig("New Game", state=DISABLED)
  global name_entry_win,user_name, placement#, name_entry_
  name_entry_win = Toplevel(master)
  #name_entry_win.wm_iconbitmap('Icon.ico')
  name_entry_win.resizable(width=False, height=False)
  frame = Frame(name_entry_win, width=300, height=200)
  frame.pack()
  user_name_entry= Entry(frame)
  Label(frame, text="Name:").grid(row=0,column=0,padx=10, pady=10)
  user_name_entry.grid(padx=20, pady=10,row=0,column=1)
  user_name_entry.focus_set()
  user_name_entry.insert(0,"Player1")
  proceed_button = Button(frame,text="Proceed",command=lambda:placement_player(user_name_entry.get()))
  proceed_button.grid(row=2,column=2,padx=10,pady=10)

def instruct():
   try:
      instruct_win=Toplevel(master)
      #instruct_win.wm_iconbitmap('Icon.ico')
      instruct_win.resizable(width=False, height=False)
      instruct_win.title("Instruction")
      Label(instruct_win,text="Instructions",font=("Arial", 15), justify = CENTER).pack()
      instruct_file= open("Instruction.txt", 'r')
      instruct_read = instruct_file.read()
      Label(instruct_win, text=instruct_read, justify=LEFT, wraplength = 350).pack()
      instruct_file.close()
   except IOError:
      pass

def how_to_play():
  try:
     how_to_play_win=Toplevel(master)
     #how_to_play_win.wm_iconbitmap('Icon.ico')
     how_to_play_win.resizable(width=False, height=False)
     how_to_play_win.title("Instruction")
     Label(how_to_play_win,text="How to Play",font=("Arial", 15), justify = CENTER).pack()
     how_to_play= open("help.txt", 'r')
     how_to_play_read = how_to_play.read()
     Label(how_to_play_win, text=how_to_play_read, justify=LEFT, wraplength = 350).pack()
     how_to_play.close()
  except IOError:
      pass

def card_value(card):
  card_reading_front = card[:-1]
  try:
      card_local_value = int(card_reading_front)
  except:
      if card_reading_front == "J":
        card_local_value = 11
      if card_reading_front == "Q":
        card_local_value = 12
      if card_reading_front == "K":
        card_local_value = 13
      if card_reading_front == "A":
        card_local_value = 14
  return card_local_value

def rearrange_subset(player_cards):
  try:
    card_first = player_cards[0]
    card_type = card_first[len(card_first)-1:len(card_first)]
    new_subset_temp = []
    initial_counter=0
    length = len(player_cards)

    for card in player_cards:
      card_reading_front = card[:-1]
      value = card_value(card)
      new_subset_temp.append(value)
    new_subset_temp.sort()
    new_subset_temp.reverse()
    new_arrangedlist = []
    for num in new_subset_temp:
      if num==14:
        new_arrangedlist.append("A"+card_type)
      if num==13:
        new_arrangedlist.append("K"+card_type)
      if num==12:
        new_arrangedlist.append("Q"+card_type)
      if num==11:
        new_arrangedlist.append("J"+card_type)
      if num<11:
        new_arrangedlist.append(str(num)+card_type)
    return new_arrangedlist
  except:
    return []

def arrange_cards(player_cards):
  cardsinlist=[]
  spade=[]
  diamond = []
  heart = []
  club = []
  for card in player_cards:
    card_reading_back = int(card[len(card)-1:len(card)])
    if card_reading_back ==1:
      spade.append(card)
    if card_reading_back ==2:
      diamond.append(card)
    if card_reading_back ==3:
      club.append(card)
    if card_reading_back ==4:
      heart.append(card)
  spade = rearrange_subset(spade)
  diamond = rearrange_subset(diamond)
  heart = rearrange_subset(heart)
  club = rearrange_subset(club)
  cardsinlist = spade+diamond+club+heart
  return cardsinlist


def check_player(player_cards):
  spade_card = 0
  major_card = 0
  for card in player_cards:
    card_reading_front = card[:-1]
    card_reading_back = card[len(card)-1:len(card)]
    if (card_reading_front == "J" or card_reading_front =="Q" or card_reading_front == "K" or card_reading_front == "A"):
      major_card+=1
    if (card_reading_back == "1"):
      spade_card+=1
  if spade_card>0 and major_card>0:
    return 1
  else:
    return 0

def card_distribution():
  global player_1, player_2, player_3, player_4
  player_1 =[]
  player_2 = []
  player_3 = []
  player_4 = []

  deck_temp_distribution = deck[:]
  counter = 0
  while len(deck_temp_distribution)>0:
    card_number = randrange(len(deck_temp_distribution))
    temp_card_holder = deck_temp_distribution.pop(card_number)
    if counter%4==0:
      player_1.append(temp_card_holder)
    if counter%4==1:
      player_2.append(temp_card_holder)
    if counter%4==2:
      player_3.append(temp_card_holder)
    if counter%4==3:
      player_4.append(temp_card_holder)
    counter+=1


def draw_player1_cards():
  global player1_card_picture
  counter = 0
  player1_card_picture = []

  for cards in player_1:
    master.update()
    player1_card_picture.append(PhotoImage(file = "Pictures/%s.gif" %cards))
    card_player_1.create_image(70+counter*25,90,image = player1_card_picture[counter]) #card pictures
    counter+=1

def number_hands(card_list): #to be made more expansive to include more cases
  number_of_hands = 0
  spade = 0
  heart = 0
  diamond = 0
  club = 0
  big_spade = 0
  for card in card_list:
    card_reading_front = card[:-1]
    card_reading_back = card[len(card)-1:len(card)]
    if card_reading_back != "1":
      if card_reading_front == "A":
        number_of_hands+=1
      if card_reading_front == "K":
        number_of_hands+=0.8
      if card_reading_front == "Q":
        number_of_hands+=0.5
      if card_reading_front == "J":
        number_of_hands+=0.2
    else:
      spade +=1
      if card_reading_front == "A":
        number_of_hands+=1
      if card_reading_front == "K":
        number_of_hands+=0.8
      if card_reading_front == "Q":
        number_of_hands+=0.6
      if card_reading_front == "J":
        number_of_hands+=0.3
  if spade>3:
    number_of_hands+=(spade-3)*0.8
  if number_of_hands<1:
    number_of_hands=1
  return int(number_of_hands)

def winner(card_list):
  max_value = 0
  card_value_type = 0
  temp_first_card = card_list[0]
  card_type = temp_first_card[len(temp_first_card)-1:len(temp_first_card)]
  spade_use = 0
  for card in card_list:
    card_reading_back = card[len(card)-1:len(card)]
    if card_reading_back=="1":
      spade_use=1
      card_type="1"

  for card in card_list:
    card_reading_back = card[len(card)-1:len(card)]
    temp_value= card_value(card)
    if card_reading_back==card_type and max_value<temp_value:
        max_value = temp_value

  if max_value==14:
       winning_card ="A"+card_type
  if max_value==13:
       winning_card ="K"+card_type
  if max_value==12:
       winning_card ="Q"+card_type
  if max_value==11:
       winning_card ="J"+card_type
  if max_value<11:
       winning_card =str(max_value)+card_type
  return winning_card

def first_card_choice(card_list):
  if randrange(20)!= 5: #to introduce some uncertainty
    temp_card_list = []
    for card in played_card_list:
        card_type = card[len(card)-1:len(card)]
        if card_type == "1":
           try:
             spade_card_list.remove(card)
           except:
             pass
           temp_card_list = spade_card_list
        if card_type == "2":
          try:
            diamond_card_list.remove(card)
          except:
            pass
          temp_card_list = diamond_card_list
        if card_type == "3":
          try:
            club_card_list.remove(card)
          except:
            pass
          temp_card_list = club_card_list
        if card_type == "4":
          try:
            heart_card_list.remove(card)
          except:
            pass
          temp_card_list = heart_card_list
    if len(temp_card_list)==0:
          temp_card_list = ["12"]
    get_pass_through = 0
    while (get_pass_through == 0 and randrange(30)!= 9) :#introducing more uncertainty
      random_choice=randrange(len(card_list))
      card_selected = card_list[random_choice]
      type_card_selected = card_selected[len(card_selected)-1:len(card_selected)]
      two_card_selection = [card_selected, temp_card_list[0]]

      if winner(two_card_selection) == card_selected:
        return(card_selected)
      else:
        setting_randomness=3
        if type_card_selected!="1":
          setting_randomness+=2
        if card_value(card_selected)>8 and card_value(card_selected)<12 and randrange(setting_randomness)==1:
          #restriction to play the highest number of the
          return(card_selected)

        elif card_value(card_selected)<9:
          return(card_selected)

        if card_value(card_selected)>11 and randrange(10)==9:
          #restriction to play the highest number of the
          return(card_selected)
  random_choice=randrange(len(card_list))
  return (card_list[random_choice])

def not_first_card_choice(card_list):
  if randrange(10)!= 3 or len(four_card_list)==3: #introducing some uncertainty
    winning_card = winner(four_card_list)
    type_winning_card = winning_card[len(winning_card)-1:len(winning_card)]
    type_first_card = first_card[len(first_card)-1:len(first_card)]



    possible_play_list_same_type = []
    for card in card_list:
      if card[len(card)-1:len(card)]== type_first_card:
        possible_play_list_same_type.append(card)


    temporary_card_list = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
  #Having the same type to cards:
    if possible_play_list_same_type:
      Big2small = 1
      if type_winning_card != type_first_card:
        Big2small = 0
      else:

        for count in range(len(temporary_card_list)):
          temporary_card_list[count]=temporary_card_list[count]+type_first_card

        for card in played_card_list+possible_play_list_same_type:
          for count in range(len(temporary_card_list)-1):
            if card==temporary_card_list[count%13]:
              del temporary_card_list[count]

        cards_remaining_with_other = temporary_card_list

        three_card_list = [winning_card,cards_remaining_with_other[0],possible_play_list_same_type[0]]

        if winner(three_card_list)!= possible_play_list_same_type[0]:
          Big2small = 0



        #if fourth turn to play and has a winning card:

        if len(four_card_list)== 3:
      #play the smallest card
          Big2small = 0
      if Big2small == 0:
        possible_play_list_same_type.reverse()
      for card in possible_play_list_same_type: #starts from small to big
        if check_correct_play(card_list,card)==1: #one of this is going to be right
          return card

    #to use the spade
    else:
      player_spade_cards = []
      for card in card_list:
         if card[len(card)-1:len(card)]=="1":
           player_spade_cards.append(card)
      #if player has to a spade card that can win
      if player_spade_cards:
        two_card_list =  [player_spade_cards[0],winning_card]
        if winner(two_card_list)== player_spade_cards[len(player_spade_cards)-1]:
          player_spade_cards.reverse()
          for card in possible_play_list_same_type: #starts from small to big
            if check_correct_play(card_list,card)==1: #one of this is going to be right
              return card
      #no cards of no winning spade cards
      random_choice = randrange(len(card_list))
      if card_value(card_list[random_choice])<10:
        return card_list[random_choice]
  random_choice = randrange(len(card_list))
  return (card_list[random_choice])



def write_number_hands(canvas_name,pl1_hands,pl2_hands,pl3_hands,pl4_hands,number_game):

  global text_pl1, text_pl2, text_pl3, text_pl4
  text_pl1=canvas_name.create_text(25,50+number_game*20, text = str(pl1_hands))
  text_pl2=canvas_name.create_text(75,50+number_game*20, text = str(pl2_hands))
  text_pl3=canvas_name.create_text(125,50+number_game*20, text = str(pl3_hands))
  text_pl4=canvas_name.create_text(175,50+number_game*20, text = str(pl4_hands))



#card selection event for player 1
def player_1_card_selection(event):
  global temp_card_pict, player_1_clicked, right_choice
  xpos = event.x
  ypos = event.y
  number_of_cards = len(player_1)
  card_selection=0
  if xpos>34 and xpos<(34+(len(player_1)-1)*25) and ypos>45 and ypos<135:
    card_selection = int((xpos-34)/25)+1
  if xpos>(34+(len(player_1)-1)*25)and xpos<(108+(len(player_1)-1)*25) and ypos>45 and ypos<135 :
    card_selection = len(player_1)

  if card_selection>0:
    player_1_clicked = 1
    master.update()
    temp_card_name = player_1[card_selection-1]
    global first_card_play_status
    ##if wrong_choice then first card defining will be a problem
    if first_card_play_status==0:
      global first_card
      first_card = temp_card_name
      right_choice=1
    player_1_selection = player_1[card_selection-1]
    go_forward_draw = 0
    if first_card_play_status==0:
      go_forward_draw = 1
    else:
      try:
        if check_correct_play(player_1,player_1_selection) == 1:
          go_forward_draw = 1
          right_choice = 1
      except:
        print("SOMETHING WRONG WITH CHECK_CORRECT_PLAY" )
        #Beep(1000,1000)
        pass

    if go_forward_draw == 1:
      temp_card_pict = PhotoImage(file = "Pictures/%s.gif" %temp_card_name)
      x_y_pos = all_position_collection[4-position]
      x_position = x_y_pos[2]
      y_position = x_y_pos[3]
      game_play_window.create_image(x_position,y_position,image = temp_card_pict)
      current_card_player1 = player_1[card_selection-1]
      player_1_card_selected_verified = player_1.pop(card_selection-1)
      four_card_list.append(player_1_card_selected_verified)
      played_card_list.append(player_1_card_selected_verified)
      card_player_1.delete(ALL)
      draw_player1_cards()
    else:
      information_win.delete(ALL)
      information_win.create_text(100,20, text="Illegal Choice")
      #Beep(1000,1000)


 #check for player_1, player_2, player_3, player_4
def write_player1_declaration():
  global clicked, player_1_clicked
  clicked = 1
  player_1_clicked = 1


def clear_screen():
  try:
    player_placement_win.pack_forget()
  except:
    pass

  try:
    player_placement_cards_display.pack_forget()
  except:
    pass

  try:
    window_number_hands.pack_forget()
  except:
    pass

  try:
    card_player_1.pack_forget()
  except:
    pass

  try:
    game_play_window.place_forget()
  except:
    pass

  try:
    information_win.place_forget()
  except:
    pass

  try:
    declare_number_hands_canvas.place_forget()
  except:
    pass

def new_game_start():
  try:
    master.update()
    sleep(3)
    clear_screen()
  except:
    pass

  #reference


  global card_player_1, game_play_window, window_number_hands, information_win, declare_number_hands_canvas
  card_player_1 = Canvas(height=150,width=420,bg="white",bd=5,relief=GROOVE)
  card_player_1.pack(side=BOTTOM, anchor=SW, padx=5, pady=5)

  window_number_hands = Canvas(height=200, width=200,bd=5,relief=GROOVE)
  window_number_hands.pack(anchor=NE,padx=5,pady=5)
  window_number_hands.create_text(100,15,text="Number of Hands",font=("Arial",15))
  window_number_hands.create_line(0,30,200,30)
  window_number_hands.create_line(0,50,200,50)

  game_play_window = Canvas(height=400, width=450, bg="white",bd=1,relief=GROOVE)
  game_play_window.place(relx=0.005, rely=0.005)

  declare_number_hands_canvas = Canvas()
  declare_number_hands_canvas.place(relx=0.685,rely=0.4)

  information_win = Canvas(height=150, width=220,bd=5,relief=GROOVE)
  information_win.place(relx=0.65,rely=0.718)


  for count in range(4):
    window_number_hands.create_line(count*50,30,count*50,200)

  temp_player_name = player_name[:]
  global current_player_list
  current_player_list= []
  for count in range(4):
      if (count+1)== (5-position):
        current_player_list.append(player_1_name)
        window_number_hands.create_text(25+50*(count),42,text=player_1_name[:8],font=("Arial",8))
      else:
        random_number = randrange(len(temp_player_name))
        player_name_single = temp_player_name.pop(random_number)
        current_player_list.append(player_name_single)
        window_number_hands.create_text(25+50*(count),42,text=player_name_single,font=("Arial",8))

  game_play()

def number_hands_writing(number_game):
  #writing number of hands to the canvas
  global clicked,number_of_hands_collection
  temp_position = 5-position
  number_of_hands_collection = [0,0,0,0]

  counter=1
  clicked = 0
  information_win.delete(ALL)
  #for count in range(0,4):

  for count in range(number_game-1,number_game+3):
    master.update()
    if (count%4+1)==temp_position:
      number_hands_option = StringVar()
      number_hands_option.set("1")
      global declare_button
      try:
        declare_button.ungrid()
        OptionMenu.ungrid()
      except:
        pass
      declare_button = Button(declare_number_hands_canvas,text="Declare", command=write_player1_declaration)
      information_win.create_text(100,20*counter,text="Your turn!")
      #Beep(800,800)
      OptionMenu(declare_number_hands_canvas, number_hands_option, "1", "2", "3", "4", "5", "6", "7", "8").grid(row = 0, column = 0, padx=10,pady=5)
      declare_button.grid(row = 0, column = 1, padx=10,pady=5)
      while clicked == 0:
        master.update()

      master.update()
      declare_button.config(state=DISABLED)
      counter+=1
      number_of_hands_collection[count%4]=int(number_hands_option.get())
    else:
      number_of_hands_collection[count%4]=number_hands(all_card_collection[count%4])
      information_win.create_text(100,20*counter,text="%s has declared %d hands." %(current_player_list[count%4],number_hands(all_card_collection[count%4])))
      counter+=1
      master.update()
    sleep(1)
  total_hands = sum(number_of_hands_collection)
  if total_hands<8:
    #no game can continue with total number hands less than eight
    master.update()
    information_win.create_text(100,120,text="Reshuffling the deck!")
    master.update()
    information_win.create_text(125,140,text="Discontination on less than 8 hands!!!")

    #Beep(1000,1000)
    master.update()
    sleep(2)
    return 0
  else:
    write_number_hands(window_number_hands,number_of_hands_collection[0],number_of_hands_collection[1],number_of_hands_collection[2],number_of_hands_collection[3],number_game)
    return 1

def game_play():
  #code for the game play
  global temp_card_image_nonplayer1, all_position_collection
  temp_card_image_nonplayer1 = []
  temp_position_player1 = 5-position
  all_position_collection = [[225,290,225,350],[400,130,400,190],[225,30,225,90],[50,130,50,190]] #first for text second for picture

  game_play_window.create_text(225,290,text=current_player_list[0])
  game_play_window.create_text(400,130,text=current_player_list[1])
  game_play_window.create_text(225,30,text=current_player_list[2])
  game_play_window.create_text(50,130,text=current_player_list[3])

  played_cards_list = []
  global first_card_play_status, first_card, four_card_list

  information_win.delete(ALL)
  total_player_1_hands_taken = total_player_2_hands_taken = total_player_3_hands_taken = total_player_4_hands_taken = 0

  #Loop for a single complete game


  for number_game in range(1,6):#to be changed to five for five rounds
    testing_par_less_8 = 0
    global player_1, player_2, player_3, player_4

    while testing_par_less_8 == 0:
      check_for_game = 0
      while True:
        card_distribution()
        check_for_game = check_player(player_1)+check_player(player_2)+check_player(player_3)+check_player(player_4)
        if check_for_game == 4:
          break

      player_1 = arrange_cards(player_1)
      player_2 = arrange_cards(player_2)
      player_3 = arrange_cards(player_3)
      player_4 = arrange_cards(player_4)


      draw_reference = number_game
      if number_game==5: #draw a straight line and saying total
        draw_reference=6
        master.update()
        write_number_hands(window_number_hands,total_player_1_hands_taken,total_player_2_hands_taken,total_player_3_hands_taken,total_player_4_hands_taken,5)
        master.update()
        information_win.delete(ALL)
        information_win.create_text(100,20,text="Addition Performed after 4 rounds")
        window_number_hands.create_line(0,140,200,140)
        master.update()
        #Beep(800,1000)
        sleep(2)

      global all_card_collection
      all_card_collection = [player_2,player_3,player_4]
      all_card_collection.insert(4-position,player_1)
      draw_player1_cards()

      testing_par_less_8 = number_hands_writing(draw_reference)

    global played_card_list, spade_card_list, diamond_card_list, club_card_list, heart_card_list

    played_card_list = []
    temporary_card_list = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    spade_card_list = []
    diamond_card_list = []
    club_card_list = []
    heart_card_list = []

    for card in temporary_card_list:
      spade_card_list.append(card+"1")
      diamond_card_list.append(card+"2")
      club_card_list.append(card+"3")
      heart_card_list.append(card+"4")

    information_win.delete(ALL)
    player_1_hands_taken = player_2_hands_taken = player_3_hands_taken = player_4_hands_taken = 0
    start_position = number_game
    temp_current_player=1

    while len(player_1)>0:
      four_card_list = []
      first_card_play_status=0
      player_1_played=0
      for count in range(start_position,start_position+4):
        master.update()
        if (temp_position_player1)%4 == (count%4):
          global player_1_clicked, right_choice
          right_choice = 0
          player_1_clicked = 0

          information_win.create_text(100,20, text="Your turn!!!")
          card_player_1.bind("<Double-Button-1>",player_1_card_selection)
          while right_choice == 0:
            master.update()
          card_player_1.unbind("<Double-Button-1>",funcid=None)
          player_1_played = 1
        else:
          x_y_pos = all_position_collection[(count-1)%4]
          x_position = x_y_pos[2]
          y_position = x_y_pos[3]

          current_player_card_list = all_card_collection[(count-1)%4]
          #other players card drawing
          master.update()
          draw_non_player_1(current_player_card_list, x_position, y_position)
          master.update()
        first_card_play_status = 1
        sleep(1)

  #aftermath of the play
  #Declaration of who wins with a Beep sound
      winning_card = winner(four_card_list)
      information_win.delete(ALL)
      check_winner_name = 0
      winner_player_name = ""

      while True:

        if four_card_list[check_winner_name]==winning_card:
          break

        check_winner_name+=1
        check_winner_name=check_winner_name%4

      start_position = (start_position+check_winner_name-1)%4+1

      if start_position==1:
          player_1_hands_taken+=1
      elif start_position==2:
          player_2_hands_taken+=1
      elif start_position==3:
          player_3_hands_taken+=1
      elif start_position==4:
          player_4_hands_taken+=1
      winner_player_name = current_player_list[start_position-1]
      information_win.create_text(100,40, text=winner_player_name+" wins!")
      information_win.create_text(100,60, text="Number of Hands by "+current_player_list[0]+": "+str(player_1_hands_taken))
      information_win.create_text(100,80, text="Number of Hands by "+current_player_list[1]+": "+str(player_2_hands_taken))
      information_win.create_text(100,100, text="Number of Hands by "+current_player_list[2]+": "+str(player_3_hands_taken))
      information_win.create_text(100,120, text="Number of Hands by "+current_player_list[3]+": "+str(player_4_hands_taken))
      #sleep(1)
      #Beep(800,800)
      master.update()
      temp_card_image_nonplayer1 = []#delete the picture from the previous play
      global temp_card_pict
      temp_card_pict = []

    #start
    #testing if successful



    actual_number_hands = [player_1_hands_taken,player_2_hands_taken,player_3_hands_taken,player_4_hands_taken]
    for count in range(4):
      if number_of_hands_collection[count]>actual_number_hands[count]:
        number_of_hands_collection[count] = -number_of_hands_collection[count]
      else:
        number_of_hands_collection[count] = number_of_hands_collection[count]+(actual_number_hands[count]-number_of_hands_collection[count])/10
    global text_pl1,text_pl2,text_pl3,text_pl4
    window_number_hands.delete(text_pl1,text_pl2,text_pl3,text_pl4)
    draw_reference=number_game
    if number_game==5:
      draw_reference+=1

    write_number_hands(window_number_hands,number_of_hands_collection[0],number_of_hands_collection[1],number_of_hands_collection[2],number_of_hands_collection[3],draw_reference)

    total_player_1_hands_taken += number_of_hands_collection[0]
    total_player_2_hands_taken += number_of_hands_collection[1]
    total_player_3_hands_taken += number_of_hands_collection[2]
    total_player_4_hands_taken += number_of_hands_collection[3]
    total_player_1_hands_taken = round(total_player_1_hands_taken,1)
    total_player_2_hands_taken = round(total_player_2_hands_taken,1)
    total_player_3_hands_taken = round(total_player_3_hands_taken,1)
    total_player_4_hands_taken = round(total_player_4_hands_taken,1)
    #in the aftermath of a game
    #check if the number of hands were eaten
    #and restart another
    #addition after a fourth game and another is saving the game if possible
  total_hand_collection = [total_player_1_hands_taken,total_player_2_hands_taken,total_player_3_hands_taken,total_player_4_hands_taken]
  who_wins = max(total_hand_collection)
  #two with same number:
  #if not
  num = 0
  while True:
    if who_wins == total_hand_collection[num]:
      break
    num+=1
  draw_checking_final = 0
  for count in range(0,4):
    if total_hand_collection[count]== max(total_hand_collection):
      draw_checking_final+=1

  if draw_checking_final == 1:
    winner_name=current_player_list[num]+ " Wins"
  else:
    winner_name = "Draw"
  master.update()
  clear_screen()
  sleep(3)

  animation(winner_name)


def draw_non_player_1(current_player_card_list,x, y):
  #reference1
  global temp_card_image_nonplayer1, first_card

  if first_card_play_status == 0:
    first_card = non_player1_card = first_card_choice(current_player_card_list)

  else:
    non_player1_card = not_first_card_choice(current_player_card_list)
    while check_correct_play(current_player_card_list,non_player1_card)==0: #come_back
      non_player1_card = not_first_card_choice(current_player_card_list)
  four_card_list.append(non_player1_card)
  played_card_list.append(non_player1_card)
  current_player_card_list.remove(non_player1_card)
  temp_card_image_nonplayer1.append(PhotoImage(file = "Pictures/%s.gif" %non_player1_card))
  game_play_window.create_image(x,y,image = temp_card_image_nonplayer1[len(temp_card_image_nonplayer1)-1])


def placement_draw(count):
  master.update()
  card_selection_placement = randrange(len(placement_deck))
  placement_card_player = placement_deck.pop(card_selection_placement)
  card_placement_selected.append(placement_card_player)
  temp_card_pict_placement.append(PhotoImage(file = "Pictures/%s.gif" %placement_card_player))
  player_placement_cards_display.create_image(80+150*count,90,image = temp_card_pict_placement[count])
  player_placement_win.delete(ALL)
  player_placement_win.create_text(350,50,text="Choose a card",font=('Helvetica',30), fill="red")
  player_placement_cards_display.create_text(80,15,text="Your Card",font=('Helvetica',12), fill="#67f353")
  for count in range(len(placement_deck)):
     player_placement_win.create_image(80+10*count,220,image = card_back)
  sleep(1)

def card_placement_evaluation():
  player_1_selection_value = card_value(card_placement_selected[0])
  #all four are equally placed at first
  global position, draw_selection
  for card in (card_placement_selected[1:len(card_placement_selected)]):
    temp_value = int(card_value(card))
    if temp_value<player_1_selection_value:
      position-=1
    if temp_value!=player_1_selection_value:
      draw_selection-=1


def placement_card_selection(event):
  xpos = event.x
  ypos = event.y
  initial_time = time()
  global temp_card_pict_placement, card_placement_selected
  temp_card_pict_placement = []
  card_placement_selected = []
  count_times = 0
  if ypos>123 and ypos<319 and xpos>13 and xpos<657:
    player_placement_win.unbind("<Double-Button-1>",funcid=None)
    placement_draw(0)
    for count in range(1,draw_selection):
      placement_draw(count)
    card_placement_evaluation()
    if draw_selection == 1:
      master.update()
      player_placement_win.create_text(95,330,text="Your position is %s" %str(position), font=('Helvetica',15))
      new_game_start()#
    else:
      master.update()
      sleep(1)
      #Beep(600,500)
      player_placement_win.create_text(50,330,text="Rechoose", font=('Helvetica',15))
      player_placement_cards_display.delete(ALL)
      player_placement_win.bind("<Double-Button-1>",placement_card_selection)
      #clear


def placement_player(user_name_entry):
  try:
    name_entry_win.destroy() #to destroy the name entry box
    screen.pack_forget() #to destroy the initial animation screen
  except:
    pass
  global clicked
  clicked = 1 #to take out of the loop in the game
  clear_screen()

  global placement_deck, player_placement_cards_display, player_placement_win, player_1_name, draw_selection, position
  position = 4 #initially position is fourth
  draw_selection = 4 #initially all four players are at same standing
  placement_deck = deck[:]
  player_1_name = user_name_entry

  gamemenu.entryconfig("New Game", state=NORMAL)
  player_placement_win = Canvas(width=680, height=350, bg="#458940")
  player_placement_win.pack(padx=10, pady=10)

  player_placement_cards_display = Canvas(width=680, height=180, bg="#3c45d8")
  player_placement_cards_display.pack(padx=10, pady=10)

  player_placement_win.create_text(350,50,text="Choose a card",font=('Helvetica',30), fill="red")

  #draw 52 cards
  global card_back
  card_back = PhotoImage(file = "Pictures/back.gif")
  for count in range(52):
    player_placement_win.create_image(80+10*count,220,image = card_back)
  player_placement_win.bind("<Double-Button-1>",placement_card_selection)

def check_correct_play(card_list,card_chose):
  right_card_status = 0#come back
  winning_card = winner(four_card_list)
  type_winning_card = winning_card[len(winning_card)-1:len(winning_card)]
  type_first_card = first_card[len(first_card)-1:len(first_card)]
  type_card_chose = card_chose[len(card_chose)-1:len(card_chose)]
  if type_first_card == type_card_chose:
    #if played winning card
    if card_value(card_chose)>card_value(winning_card):
      right_card_status = 1
    else:
      check_for_right_choice=1
      if type_first_card != "1" and type_winning_card=="1":
        pass
      else:
        for card in card_list:
          temp_holder_card_type=card[len(card)-1:len(card)]
          if temp_holder_card_type == type_first_card:
            if card_value(card)>card_value(winning_card):
               check_for_right_choice=0
      right_card_status=check_for_right_choice

  else:
    #different types of card used check if the same type of card is present

    check_for_right_choice=1
    for card in card_list:
      temp_holder_card_type=card[len(card)-1:len(card)]
      if temp_holder_card_type == type_first_card:
         check_for_right_choice=0

    #first card is spade and user has run out of spade
    if check_for_right_choice==1:

      if type_card_chose != "1":#not a spade
        for card in card_list:
          temp_holder_card_type=card[len(card)-1:len(card)]
          if type_winning_card!="1" and temp_holder_card_type == "1":
            check_for_right_choice = 0
          if temp_holder_card_type == "1" and card_value(card)>card_value(winning_card) and type_winning_card=="1":
            check_for_right_choice=0

      else:

      #if the player plays spade #already checked

        #if already wins the game
        if card_value(card_chose)>card_value(winning_card):
          pass
        else:
          for card in card_list:
            temp_holder_card_type=card[len(card)-1:len(card)]
            if temp_holder_card_type == "1":
              if card_value(card)>card_value(winning_card) and type_winning_card=="1":
                check_for_right_choice=0

    right_card_status=check_for_right_choice
  return right_card_status #returns 0 if the player is wrong and 1 if the player is right





#menu of the game
menubar = Menu(master)
gamemenu = Menu(menubar, tearoff = 0)
gamemenu.add_command(label="New Game", command=name_entry)
gamemenu.add_separator()
gamemenu.add_command(label="Credit", command = credit)
gamemenu.add_command(label="Quit", command=confirmation)

menubar.add_cascade(label="Game", menu=gamemenu )


helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="How to Play", command=how_to_play)
helpmenu.add_command(label="Instruction", command=instruct)

menubar.add_cascade(label="Help", menu=helpmenu)
master.config(menu=menubar) # display the menu

card_types = ["1","2","3","4"] #1 = spade, 2 = diamond, 3 = club, 4 = heart
card_numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
player_name =["Shubham", "Prajjwol", "Gagan","Pramit", "Kapil", "Andrew"]

deck=[]
for card_type in card_types:
  for card_number in card_numbers:
     deck.append(card_number+card_type)

animation("Call Break")

mainloop()
