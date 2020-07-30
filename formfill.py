import pyautogui, time, webbrowser, csv, datetime

def getDateSeq(date_time):
    values = date_time.split('/')
    subdate = datetime.date(int(values[0]),int(values[1]),int(values[2]))
    today = datetime.date.today()
    presses = (today - subdate).days
    seq = []
    for i in range(presses):
        seq.append('left')
    seq.append('enter')
    return seq

def getHourSeq(date_time):
    hour_seq = []
    mins_seq = []
    values = date_time.split('/')
    now = datetime.datetime.now()
    dif_hours = now.hour - int(values[3])
    dif_mins = (now.minute - int(values[4]))//5

    if dif_hours > 0:   move = 'left'
    else: move = 'right'
    for i in range(abs(dif_hours)):
        hour_seq.append(move)
    hour_seq.append('enter')
        
    if dif_mins > 0:   move = 'left'
    else: move = 'right'  
    for i in range(abs(dif_mins)):
        mins_seq.append(move)
    mins_seq.append('enter')

    return hour_seq, mins_seq

def run(row):
    webbrowser.open('https://makaut1.ucanapply.com/smartexam/public/')

    time.sleep(2)
    smalldelay = 0.05
    longdelay = 0.2
    #navigating
    try:
        pyautogui.click('student.png')
        time.sleep(2)
        pyautogui.click('submit.png')
        time.sleep(2)
        pyautogui.click('activity2.png')
        time.sleep(2)
    except:
        print('image cannot be located')

    #filling
    dataFile = open('data.csv')
    dataReader = csv.reader(dataFile)
    data = list(dataReader)
    #week
    info0 = open('mouseInfoLog0.txt','r')
    info1 = open('mouseInfoLog1.txt','r')
    time.sleep(2)
    week = int(data[row][0])
    week_points=[]
    for coord in info0:
        values = coord.split(',')
        temp = [int(values[0]),int(values[1])]
        week_points.append(temp)

    pyautogui.click(week_points[0])
    pyautogui.click(week_points[week])
    for coord in info1:
        values = coord.split(',')
        pyautogui.click(int(values[0]),int(values[1]))
        time.sleep(0.2)

    time.sleep(0.5)
    #subject
    pyautogui.click(159,494); pyautogui.write(data[row][3],longdelay); pyautogui.click(140,580)
    #topic
    pyautogui.click(730,500); pyautogui.write(data[row][4],smalldelay)
    #platform
    pyautogui.click(1288,501); pyautogui.write(data[row][5],smalldelay)
    #teacher
    pyautogui.click(116,601); pyautogui.write(data[row][6],longdelay); pyautogui.click(129,689)
    #date
    date_seq = getDateSeq(data[row][7])
    seq = getHourSeq(data[row][7])

    pyautogui.click(588,605)
    pyautogui.write(date_seq)
    pyautogui.write(seq[0])
    pyautogui.write(seq[1])

    info2 = open('mouseInfoLog2.txt', 'r')
    column = 8
    time.sleep(1)
    for coord in info2:
        values = coord.split(',')
        pyautogui.click(int(values[0]),int(values[1])); pyautogui.write(data[row][column],smalldelay)
        column+=1
        time.sleep(0.2)
    
    pyautogui.click('add_details.png')
    time.sleep(1)

def launch(begin_row, end_row):
    for row in range(begin_row, end_row+1):
        run(row)
#launch takes parameters (begin_row-1, end_row) according to data.csv file
launch(0,54)

