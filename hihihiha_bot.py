import PySimpleGUI as sg
import telegram
layoutpulsanti= [[sg.Button('invia',key="invia"), sg.FileBrowse('Immagine',target='Immagine',file_types=(("JPEG",".JPG"),("PNG",".png")),key='Immagine')]]
layoutgenerale = [  [sg.Text('Invia il messaggio')],
    [sg.Multiline(default_text='',size=(80,10),no_scrollbar=True)],
    [sg.Input('Immagine',expand_x=True,key='Immagine', enable_events=True,visible=True)],
    [sg.Column(layoutpulsanti,expand_x=True,element_justification="center")]]
 
window = sg.Window('Teleponti', layoutgenerale, location=(750, 450))
chatid= "-682438525"
token= "xxx"
bot = telegram.Bot(token=token)
while True:
    event, values = window.read()
    print (values)
    if event== "invia":
        if values[0]=="":
            sg.popup("scrivere un messaggio o selezionare una immagine")
        else:
            bot.send_message(chat_id=chatid, text=values[0])
            bot.send_message(chat_id = chatid, text = "HI HI HI HA!")
            bot.send_video(chat_id=chatid, video=open('clashroyale.mp4', 'rb'), supports_streaming=True)
    if event=="Immagine":
        try:
            bot.send_photo(chat_id=chatid, photo=open(values['Immagine'], 'rb'))
        except:
            sg.popup("scrivere un messaggio o selezionare una immagine")
    if event == sg.WIN_CLOSED or event == 'Cancel':
       break
    print('You entered ', values[0])
   
window.close()
