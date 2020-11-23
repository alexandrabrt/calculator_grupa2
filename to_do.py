import datetime

class Todolist:

    def __init__(self):
        self.task = input('Introduceti task-ul: ')
        self.list_task = []
        self.choice = 'D'
        self.data = input('Introduceti data dupa urmatorul format zz.ll.aaaa ')
        try:
            datetime.datetime.strptime(self.data, '%D.%M.%Y')
        except Exception:
            pass
        self.persoana_responsabila = input('Introduceti persoana responsabila: ')
        #while self.persoana_responsabila not in self.list_task
        self.categorie


    def metoda_aduagare_taskuri(self):

        while self.choice == 'D':
            self.tasks = input("Introduceti in lista task urile")
            self.list_task.append(self.task)
            self.choice = input("Doriti sa introduceti un alt task de la tastatura D/N: ")

        return self.list_task

    def