class Nachalniki: #Класс
    prizv = ""
    name = ""
    po_batkovi = ""
    posada = ""

    def __init__(self, prizv, name, po_batkovi, posada): #Коноструктор с параметром
        self.prizv = prizv
        self.name = name
        self.po_batkovi = po_batkovi
        self.posada = posada

class Others(Nachalniki): #Наследование
    Moz_ker_insh_nach = ""
    def __init__(self, prizv, name, po_batkovi, posada, Moz_ker_insh_nach): #Перегрузка методов
        self.prizv = prizv
        self.name = name
        self.po_batkovi = po_batkovi
        self.posada = posada
        self.Moz_ker_insh_nach = Moz_ker_insh_nach

Zamistnik = Others("Косенко ", "Дмитро", " Сергійович", "Замістник директора", True)
Director = Others("Майстренко", " Наталія ", "Миколаївна", "Директор", True)



class Zav(Nachalniki): #Наследование
    __kurs = "" #Инкапсуляция


Sovgir = Zav("Совгир ", "Людмила", " Миколаївна", "Завідуюча відділенням")
Sovgir.kurs = "другий, третій, четвертий"

Vasiletc = Zav("Василець", " Тетяна ", "Олександрівна", "Завідуюча відділенням")
Vasiletc.kurs = "перший"

Zhmud = Zav("Жмуд", " Надія ", " Олександрівна", "Завідуюча відділенням")
Zhmud.kurs = "другий, третій, четвертий (Професійна освіта)"
