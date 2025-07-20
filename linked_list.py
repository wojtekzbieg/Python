
class wezel:
    def __init__(self, data):
        self.data = data
        self.next = None

class lista:
    def __init__(self):
        self.head = None


    def dodaj_element_na_poczatku(self, data):
        nowy_wezel = wezel(data)
        nowy_wezel.next = self.head
        self.head = nowy_wezel


    def dodaj_element_gdziekolwiek(self, data, index):
        if index == 1:
            self.dodaj_element_na_poczatku(data)
            return
        elif index == 0:
            print("indeksy zaczynaja sie od 1")
            return

        current_wezel = self.head
        pozycja = 0
        while pozycja != index-2:

            current_wezel = current_wezel.next
            pozycja += 1

            if current_wezel is None:
                print("index out of range")

        nowy_wezel = wezel(data)
        nowy_wezel.next = current_wezel.next
        current_wezel.next = nowy_wezel


    def dodaj_element_na_koncu(self, data):
        nowy_wezel = wezel(data)
        if self.head is None:
            self.head = nowy_wezel
            return

        current_wezel = self.head
        while current_wezel.next:
            current_wezel = current_wezel.next


        current_wezel.next = nowy_wezel


    def zmien_wartosc_elementu(self, value, index):
        current_wezel = self.head
        pozycja = 0

        while current_wezel is not None and pozycja != index-1:
            current_wezel = current_wezel.next
            pozycja += 1

        if current_wezel is None:
            print("index out of range")
            return

        current_wezel.data = value


    def wyswietl_liste(self):
        if self.head is None:
            print("lista jest pusta")

        else:
            current_wezel = self.head
            while current_wezel:
                print(f"['{current_wezel.data}']", end=" ")
                current_wezel = current_wezel.next





lista = lista()
lista.dodaj_element_na_poczatku(5)
lista.dodaj_element_gdziekolwiek(10,2)
lista.dodaj_element_na_koncu(10)
lista.zmien_wartosc_elementu(15,3)

lista.wyswietl_liste()