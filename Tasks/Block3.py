def task (period = 50):
    '''
    Программа считает
    A. Какого уровня будет игрок в конце периода				
    B. Сколько всего фруктов каждого вида будет продано				
    C. Сумма потраченных и заработанных у.е				
    D. Конечный остаток у.е.				

    Параметры
    ----------
    Период: ТИП int, по умолчанию 50.

    '''
    #Создаем необходимые счётчики
    level = 1       #уровень
    exp = 0         #опыт
    money = 0       #деньги
    day = 0         #день недели для отсчета бонуса в конце недели
    applecount = 0  #кол-во яблок
    orangecount = 0 #кол-во апельсинов
    pearcount = 0   #кол-во груш
    earned = 0      #заработанная сумма
    spent = 0       #потраченная сумма
    #Прописываем, на каких уровнях появляются какие фрукты. В обратном порядке,
    #чтобы в дальнейшем использовать метод pop(), дабы избежать повторной выдачи
    #фрукта, если игрок остался на одном уровне на несколько дней
    orange = [340, 310, 280, 250, 220, 190, 160, 130, 100, 70, 35, 30, 25, 3]
    pear = [350, 320, 290, 260, 230, 200, 170, 140, 110, 80, 60, 55, 50, 45, 40]
    apple = [330, 300, 270, 240, 210, 180, 150, 120, 90, 65, 20, 15, 10, 5, 2]

    
    for i in range (1,period+1):
        exp += 100                          #Добавляем 100 опыта каждый день
        
        if day // 7:                        #Если ВСК:
            exp += 5500                     #добавляем 5500 опыта
            day = 0                         #переходим на ПН
            
        while exp // 300 and exp > 0:       #Пока у игрока есть более 300 опыта
            exp -= 300                      #вычитаем этот опыт
            level += 1                      #прибавляем 1 к уровню
            if level in apple:              #Если на новом уровне предполагается яблоко
                money += 50                 #добавляем 50 у.е.
                earned += 50                #записываем их в заработанное
                apple.pop()                 #убираем уровень из списка, как пройденный, чтобы избежать двойного счёта            
                applecount += 1             #прибавляем к счетчику яблок
            elif level in pear:             #Аналогично повторяем для груш, если на уровне д.б. груша
                money += 130                
                earned += 130               
                pear.pop()                  
                pearcount += 1              
            elif level in orange:           #Аналогично повторяем для апельсинов, если на уровне д.б. апельсин
                money += 75                 
                earned += 75                
                orange.pop()                
                orangecount += 1            
                                            #Во время тестирования было обнаружено, что оптимальная
                                            #стратегия покупать всегда уровни за 120 у.е
                                            #В документе будут объяснения.                                 
            # if money >= 615:                
            #     money -= 615
            #     exp += (24*300)
            # elif money >= 275:
            #     money -= 275
            #     exp += (11*300)
            elif money >= 120:                #Если денег больше 120
                money -= 120                #снимаем эти деньги
                spent -= 120                #заносим в расходы
                exp += (5*300)              #прибавляем 1500 опыта
                
        day += 1                            #Завершаем текущую итерацию и переходим
                                            #на следующий день периода          
        
    print (f'Период: {i} дней. Уровень: {level}. \nПродано яблок: {applecount}, апельснов: {orangecount}, груш: {pearcount}. \nЗаработано: {earned}, потрачено: {-spent}. \nОстаток денег: {money}')
               
task()
       
