from sys import implementation
import PySimpleGUI as sg
import webbrowser

image1 = b'background image.png'

sg.theme('bluemono')

layout = [
    
    
    [sg.Text('Website Opener', size=(18,1), font = 'Calibri 30', justification='c', background_color='#2f2c30', text_color='white')],

    [sg.Checkbox('Youtube', key = '-YT-', font = 'Calibri 15', background_color='Red', text_color='white', size=(8,1)), sg.Checkbox('Edge Hill Website', key = '-EHU_WEB-', font = 'Calibri 15', background_color='teal', text_color='white', size=(18,1)) ], 
    [sg.Checkbox('Google', key = '-GOOGLE-', font = 'Calibri 15', background_color='blue', text_color='white', size=(8,1)), sg.Checkbox('Edge Hill Blackboard', key = '-EHU_BB-', font = 'Calibri 15', background_color='orange', text_color='white')],

    [sg.Button('Open Selected', key = '-OPEN-', expand_x=True, expand_y= True, font = 'Calibri 18', button_color='#2f2c30')],
    [sg.Button('Exit', expand_x=True, expand_y=False, font = 'Calibri 18', button_color='#2f2c30')]

]

window = sg.Window('Url Opener', layout, size=(346, 300), no_titlebar=True, background_color='white')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        
        break


    if values['-YT-']  == True:
        get_url = webbrowser.open('https://www.youtube.com/')
        window.close()

    if values['-GOOGLE-'] == True:
        get_url = webbrowser.open('https://google.com/')
        window.close()
    
    if values['-EHU_WEB-'] == True:
        get_url = webbrowser.open('https://www.edgehill.ac.uk/')
        window.close()

    if values['-EHU_BB-'] == True:
        get_url = webbrowser.open('https://learningedge.edgehill.ac.uk/ultra/course')
        window.close()

    

    

   

    

    

        
        
        

    
window.close()



        
        
        





    

window.close()
