import pyautogui
import time as tm
from data import datas
import keyboard as key

dt = datas()
pyautogui.press('win')
tm.sleep(2)
pyautogui.write('chrome')
pyautogui.press('enter')
tm.sleep(2)
pyautogui.write('https://plataforma.ubots.com.br/?next=https%3A%2F%2Fplataforma.ubots.com.br%2Fv1%2Fdesk%2F%23%2Fconversation-new')
pyautogui.press('enter')
tm.sleep(8)
pyautogui.press('tab')
pyautogui.press('tab')
tm.sleep(2)
pyautogui.write('USER')
pyautogui.press('tab')
tm.sleep(2)
pyautogui.write('PASSWORD')
pyautogui.press('enter')
tm.sleep(6)
pyautogui.click(x=1417,y=121)                               
tm.sleep(1.5)
pyautogui.click(x=1396, y=205)
tm.sleep(2)
pyautogui.click(x=1405, y=253)
tm.sleep(2)
pyautogui.click(x=27, y=705)        
tm.sleep(2)
pyautogui.click(x=27, y=705)        
tm.sleep(2)
pyautogui.click(x=72, y=614)
tm.sleep(3)
for i in range(13):
    pyautogui.press('tab')
pyautogui.press('enter')
tm.sleep(1.5)
pyautogui.click(x=1588, y=277)
tm.sleep(1.5)
for i in range(10):
    pyautogui.press('backspace')
tm.sleep(2)
pyautogui.doubleClick(x=1512, y=277)
tm.sleep(2)
pyautogui.write(dt.formatar_passado_inicio())
tm.sleep(1)
pyautogui.press('enter')
tm.sleep(1.5)
pyautogui.click(x=1795, y=278)
tm.sleep(2)
for i in range(10):
    pyautogui.press('backspace')
tm.sleep(2)
pyautogui.click(x=1707, y=223)
tm.sleep(1)
pyautogui.click(x=1732, y=276)
tm.sleep(1.5)
pyautogui.write(dt.formatar_passado_fim())
tm.sleep(1.5)
pyautogui.press('enter')
tm.sleep(1.5)
pyautogui.click(x=1446, y=901)
tm.sleep(2)
pyautogui.scroll(-500)
tm.sleep(1.5)
pyautogui.click(x=1445, y=459)
pyautogui.click(x=1447, y=543)
pyautogui.click(x=1445, y=586)
pyautogui.click(x=1448, y=678)
pyautogui.click(x=1445, y=730)
pyautogui.click(x=1445, y=781)
pyautogui.click(x=1448, y=835)
pyautogui.click(x=1647, y=504)
pyautogui.click(x=1642, y=546)
pyautogui.click(x=1647, y=587)
pyautogui.click(x=1646, y=678)
pyautogui.click(x=1647, y=731)
tm.sleep(1.5)
pyautogui.scroll(-400)
tm.sleep(1.5)
pyautogui.click(x=1445, y=685)
pyautogui.click(x=1447, y=727)
pyautogui.click(x=1443, y=767)
pyautogui.click(x=1447, y=804)
pyautogui.click(x=1445, y=849)
pyautogui.click(x=1444, y=929)
pyautogui.click(x=1445, y=888)
pyautogui.click(x=1646, y=686)
pyautogui.click(x=1644, y=727)
pyautogui.click(x=1646, y=765)
pyautogui.click(x=1647, y=807)
pyautogui.click(x=1645, y=849)
pyautogui.click(x=1647, y=888)
tm.sleep(1.5)
pyautogui.click(x=1662, y=999)
tm.sleep(2)
pyautogui.click(x=1498, y=981)
tm.sleep(2)
pyautogui.click(x=849, y=565)
tm.sleep(1.5)
pyautogui.write('controller2@levnegocios.com.br')
tm.sleep(2)
pyautogui.click(x=1109, y=659)
tm.sleep(2)
pyautogui.click(x=1109, y=659)
tm.sleep(2)
pyautogui.click(x=1670, y=984)
tm.sleep(1.5)
pyautogui.moveTo(x=1702, y=938)
tm.sleep(1.5)
pyautogui.scroll(850)
tm.sleep(1.5)
pyautogui.click(x=1588, y=277)
tm.sleep(1.5)
for i in range(10):
    pyautogui.press('backspace')
tm.sleep(2)
pyautogui.doubleClick(x=1512, y=277)
tm.sleep(2)
pyautogui.write(dt.formatar_hoje_inicio())
tm.sleep(1)
pyautogui.press('enter')
tm.sleep(1.5)
pyautogui.click(x=1795, y=278)
tm.sleep(2)
for i in range(10):
    pyautogui.press('backspace')
tm.sleep(2)
pyautogui.click(x=1707, y=223)
tm.sleep(1)
pyautogui.click(x=1732, y=276)
tm.sleep(1.5)
pyautogui.write(dt.formatar_hoje())
tm.sleep(1.5)
pyautogui.press('enter')
tm.sleep(1)
pyautogui.click(x=1674, y=998)
tm.sleep(1.5)
pyautogui.click(x=1498, y=981)
tm.sleep(2)
pyautogui.click(x=849, y=565)
tm.sleep(1.5)
pyautogui.write('controller2@levnegocios.com.br')
tm.sleep(2)
pyautogui.click(x=1109, y=659)
tm.sleep(2)
pyautogui.click(x=1109, y=659)
tm.sleep(2)
pyautogui.hotkey('ctrl','t')
tm.sleep(1.5)
pyautogui.write('https://outlook.office.com/mail/')
pyautogui.press('enter')
tm.sleep(120)
pyautogui.click(x=494, y=397)
tm.sleep(1.5)
pyautogui.click(x=1359, y=614)
tm.sleep(8)
pyautogui.click(x=481, y=499)
tm.sleep(8)
pyautogui.click(x=1359, y=614)
tm.sleep(15)
pyautogui.click(x=438, y=986)
tm.sleep(10)
pyautogui.click(x=-909, y=116)
tm.sleep(6)
pyautogui.click(x=-2379, y=286)
tm.sleep(1.5)
pyautogui.doubleClick(x=-2290, y=286)
tm.sleep(15)
pyautogui.click(x=144, y=985)
tm.sleep(18)
pyautogui.click(x=-909, y=116)
tm.sleep(8)
pyautogui.click(x=-2337, y=306)
tm.sleep(2)
pyautogui.hotkey('ctrl','*')
tm.sleep(2)
pyautogui.hotkey('ctrl','c')
tm.sleep(2)
pyautogui.hotkey('ctrl','tab')
tm.sleep(2)
pyautogui.click(x=-2339, y=306)
tm.sleep(2)
pyautogui.hotkey('ctrl','down')
tm.sleep(1)
pyautogui.press('down')
tm.sleep(1)
pyautogui.hotkey('ctrl','v')
tm.sleep(1)
pyautogui.press('left')
tm.sleep(1)
pyautogui.hotkey('ctrl','-')
tm.sleep(1)
pyautogui.press('up')
tm.sleep(1)
pyautogui.press('up')
tm.sleep(1)
pyautogui.press('enter')
tm.sleep(1)
pyautogui.hotkey('ctrl','up')
tm.sleep(1)
pyautogui.click(x=-536, y=286)
tm.sleep(1)
pyautogui.hotkey('ctrl','+')
tm.sleep(1.5)
pyautogui.doubleClick(x=-671, y=306)
pyautogui.write('ID')
tm.sleep(1)
pyautogui.press('enter')
tm.sleep(1)
pyautogui.hotkey('ctrl','tab')
tm.sleep(1)
pyautogui.click(x=-32, y=33)
tm.sleep(1)
pyautogui.click(x=-1862, y=1321)
tm.sleep(1)
pyautogui.click(x=474, y=242)
tm.sleep(1)
pyautogui.write('Z:\COMPARTILHADOS\BI\PLANILHAS\Rel_atendimento.xlsx')
tm.sleep(1)
pyautogui.press('enter')
tm.sleep(15)
pyautogui.click(x=-915, y=114)
tm.sleep(8)
pyautogui.hotkey('ctrl','tab')
tm.sleep(1)
pyautogui.doubleClick(x=-696, y=334)
tm.sleep(1)
key.write("=PROCV(F2;'[Rel_atendimento.xlsx]Relatório de Protocolos'!$F:$G;2;0)")
tm.sleep(1)
pyautogui.press('enter')
tm.sleep(1)
pyautogui.hotkey('ctrl','tab')

