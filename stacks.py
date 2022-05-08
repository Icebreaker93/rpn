class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    # Funktion zum Hinzufügen von Inhalt auf den Stack mithilfe der List append Methode
    def push(self, inhalt):
        self.stack.append(inhalt)
    
    # Um das oberste Element vom Stack zu entfernen, nutzen wir die List pop Methode
    def pop(self):
        errorempty = ("Stapel ist leer.")
        # Wenn Stack Inhalt hat, wird die pop Methode angewendet
        # Wenn Stack leer ist, wird Fehler ausgegeben
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return errorempty

    # Gibt bei nicht leerem Stack oberstes Element zurück
    def top(self):
        errorempty = ("Stapel ist leer.")
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return errorempty
    
    # Prüft ob Stack leer ist
    def isEmpty(self):
        notempty = ("Stapel ist nicht leer")
        errorempty = ("Stapel ist leer.")
        if len(self.stack) != 0:
            return notempty
        else:
            return errorempty
    
    # Gibt die Anzahl der Stack Elemente zurück
    def size(self):
        stacksize = len(self.stack)
        return stacksize

# Klasse für die reverse polish notation
class Rpn:
    def __init__(self,):
        self.stack = Stack()
    
    # Funktion zur Berechnung des rpn, der wir eine Liste übergeben
    def calcrpn(self, term = []):
        self.term = term
        # Handelt es sich um einen numerischen Wert, wird er dem Stack hinzugefügt
        for i in term:
            if type(i) == float or type(i) == int:
                self.stack.push(i)
            # Handelt es sich nicht um einen numerischen Wert, werden die
            # ersten beiden Elemente des Stacks in Variablen gespeichert und vom Stack entfernt
            else:
                a = self.stack.top()
                self.stack.pop()
                b = self.stack.top()
                self.stack.pop()
                
                # Definition der Berechnungsoperatoren, für die jeweils beiden zwischengespeicherten
                # und entferntenStack Elemente, deren Ergebnisse dem Stack wieder zugefügt werden
                if i == "+":
                    self.stack.push(a + b)
                elif i == "-":
                    self.stack.push(b - a)
                elif i == "*":
                    self.stack.push(a * b)
                elif i == "/":
                    self.stack.push(b / a)
                    
        # Zwischenspeicherung des Ergebnisses in Variable   
        ergebnis = self.stack.top()
        # Rückgabe des Ergebnisses
        return ergebnis


# Erstellen eines leeren Stapels / Objekts der Klasse Stapel
stapel1 = Stack()

# Test ob die grundlegenden Stapelbefehle funktionieren
print(stapel1.isEmpty())
stapel1.push(2)
stapel1.push(5)
stapel1.push(7)
stapel1.pop()
stapel1.push(7)
print(stapel1.size())
print(stapel1.isEmpty())

# Aufgabe aus Vorlesung
aufgabe = [5.1, 91, 28, "+", 4.3, 6, "+", "*", 777, "+", "*"]

# Ausgabe des auf 2 Dezimalstellen gerundeten Ergebnisses
print(round(float(Rpn().calcrpn(aufgabe)),2))              




