#переменая фреза ширина паза

# '''
# задачи
# 1. разбить по классам
#
#     а. добавить проходы по круговой интерполяции (горизонтальной и вертикальной расписать позиционирование инструмента)
#     б. родительски класс инициализация вводных данных
#     в. классы расчет проходов
# 2. реализовать через телеграм бот
#     инициализация запросов с телеграм бота
# 3. закинуть на сервер
# '''


#pасчет прохода гребня

    
#расчет проходов фрезы паз

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def proxod_greb(frez, shir_grebe):
    sdvig_frez= {}
    frez,shir_grebe = float(frez), float(shir_grebe)
    greb_pred_chist_pol = (frez + shir_grebe + 1) / 2
    greb_pred_chist_otr = (frez + shir_grebe + 1) / 2*-1
    greb_chist_pol = (frez + shir_grebe) / 2
    greb_chist_otr = (frez + shir_grebe) / 2*-1
    print(f"предчистовой проход если центр гребня 0 гребень {greb_pred_chist_pol}")
    print(f"чистовой проход если центр гребня 0 гребень {greb_chist_pol}")
    sdvig_frez["pred_chist_otr"] = toFixed(greb_pred_chist_otr, 3)
    sdvig_frez["pred_chist_pol"] = toFixed(greb_pred_chist_pol, 3)
    sdvig_frez["chist_otr"] = toFixed(greb_chist_otr, 3)
    sdvig_frez["chist_pol"] = toFixed(greb_chist_pol, 3)
    print(sdvig_frez)
    return sdvig_frez


def proxod_paz(frez, paz):
    frez, paz = float(frez), float(paz)
    sdvig_frez = {}
    pred_chist_pol=(paz - frez -1)/2
    pred_chist_otr=((paz - frez -1)/2)*-1
    print(f'предчистовой проход {toFixed(pred_chist_otr,3)} и {pred_chist_pol}')
    chist_pol=(paz - frez )/2
    chist_otr=(paz - frez )/2*-1
    print(f'чистовой проход {chist_otr} и {chist_pol}')
    sdvig_frez["pred_chist_otr"] = toFixed(pred_chist_otr, 3)
    sdvig_frez["pred_chist_pol"] = toFixed(pred_chist_pol, 3)
    sdvig_frez["chist_otr"] = toFixed(chist_otr,3)
    sdvig_frez["chist_pol"] = toFixed(chist_pol, 3)
    print(sdvig_frez)
    return sdvig_frez

class Result_Prohoda():
    """собираем даные для расчета прохода
    просчет берем из функций"""
    def __init__(self, otbr_func, frez, paz_greben):
        self.otbr_func = otbr_func
        self.frez = frez
        self.paz_greben = paz_greben
    """сделал паз горебень в одну для просчета"""
    def prov_vxod(self):
        if self.otbr_func == "Рассчет паза":
            if float(self.frez)+1 < float(self.paz_greben):
                return proxod_paz(
                                  self.frez,
                                  self.paz_greben)
            elif float(self.frez)+1 > float(self.paz_greben):
                return None
        elif self.otbr_func == "Рассчет гребня":
            return proxod_greb(
                              self.frez,
                              self.paz_greben)







# ResuitProhoda = Result_Prohoda(otbr_func="paz", frez=12.9, paz=34.4,  greben=23.6)
#
# # ResuitProhoda.print1()
# ResuitProhoda.proxod_paz()
# ResuitProhoda.proxod_greb()

    #расчет паза
    # if greb_paz ==1:
    #     shir_greben=float(input("Прошу ввести ширину гребня в мм: "))
    #     dopusk=float(input("Прошу ввести допуск в мм если допуска нет пиши O : "))
    #     if (shir_greben-dopusk)/2 > freza/2:
    #         proxod_greb(freza, shir_greben, dopusk)
    #     else:
    #         print ("ошибочный ввод попробуйте сначала")
    #
    # #рпсчет гребня
    # elif greb_paz ==0:
    #     shir_paza=float(input("Прошу ввести ширину паза в мм: "))
    #     dopusk=float(input("Прошу ввести допуск в мм если допуска нет пиши O : "))
    #     if shir_paza+dopusk<freza:
    #         print ('Ширина паза с допуском уже чем фреза подберите другую фрезу')
    #     elif shir_paza+dopusk>freza:
    #         smeshnie = 0
    #         proxod_paz(freza, shir_paza, dopusk, smeshnie)
    # else:
    #     print ("ошибочный ввод попробуйте сначала")
    #

# """
# def proxod_greb(frez, shir_grebe, dopus):
#     pred_chist_prox=(frez+shir_grebe-dopus+1)/2
#     chist_prox=(frez+shir_grebe-dopus)/2
#     print (f"предчистовой проход если центр гребня 0 гребень {pred_chist_prox}")
#     print (f"чистовой проход если центр гребня 0 гребень {chist_prox}")
#
#
# #расчет проходов фрезы паз
# def proxod(fez, paz, dop, sdvig):
#     sdvig = sdvig
#     pred_chist_pol=(paz + dop -fez -1)/2
#     pred_chist_otr=((paz + dop -fez -1)/2)*-1
#     print(f'предчистовой проход {pred_chist_otr} и {pred_chist_pol}')
#     chist_pol=(paz + dop -fez )/2
#     chist_otr=(paz + dop -fez )/2*-1
#     print(f'чистовой проход {chist_otr} и {chist_pol}')
#     sdvig_pre_pol = sdvig+pred_chist_pol
#     sdvig_pre_otr= sdvig+pred_chist_otr
#     sdvig_chis_pol = sdvig+chist_pol
#     sdvig_chis_otr = sdvig+chist_otr
#
#     print(f'предчистовой проход со сдвигом от 0 - {sdvig_pre_otr} и {sdvig_pre_pol}')
#
#     print(f'предчистовой проход со сдвигом от 0 - {sdvig_chis_otr} и {sdvig_chis_pol}')
#
# #расчет паза
# if greb_paz ==1:
#     shir_greben=float(input("Прошу ввести ширину гребня в мм: "))
#     dopusk=float(input("Прошу ввести допуск в мм если допуска нет пиши O : "))
#     if (shir_greben-dopusk)/2 > freza/2:
#         proxod_greb(freza, shir_greben, dopusk)
#     else:
#         print ("ошибочный ввод попробуйте сначала")
#
# #рпсчет гребня
# elif greb_paz ==0:
#     shir_paza=float(input("Прошу ввести ширину паза в мм: "))
#     dopusk=float(input("Прошу ввести допуск в мм если допуска нет пиши O : "))
#     if shir_paza+dopusk<freza:
#         print ('Ширина паза с допуском уже чем фреза подберите другую фрезу')
#     elif shir_paza+dopusk>freza:
#         smeshnie = 0
#         proxod(freza, shir_paza, dopusk, smeshnie)
# else:
#     print ("ошибочный ввод попробуйте сначала")
# """