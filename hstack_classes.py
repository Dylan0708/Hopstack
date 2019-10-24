from modules import format_methods as form
import decimal, mysql.connector
from decimal import Decimal
class Hop:
    def __init__(self, name = 'NULL', origin = 'NULL', h_type = 'NULL', alpha = 'NULL', beta = 'NULL', price = 0, qty = 0, notes = 'NULL'):
        self.name = name
        self.origin = origin
        self.h_type = h_type
        self.alpha = alpha
        self.beta = beta
        self.price = price
        self.qty = qty
        self.notes = notes
        self.body = [(None, 'Name'), (None, 'Origin'), (None, 'Type (Bittering, Aroma, or Both)'), (None, 'Alpha Acid Content (%)'), (None, 'Beta Acid Content (%)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save'), (None, 'Exit Without Saving')]
    # Saves the user provided name formatted for mysql, and a tuple for screen formatting
    def get_name(self):
        temp_name = input("Name: ")
        self.body[0] = (None, ('Name: ' + temp_name))
        self.name = form.quote_str(temp_name)
    # Saves the user provided origin formatted for mysql, and a tuple for screen formatting
    def get_origin(self):
        temp_origin = input("Origin: ")
        self.body[1] = (None, ('Origin: ' + temp_origin))
        self.origin = form.quote_str(temp_origin)
    # Saves the user provided type formatted for mysql, and a tuple for screen formatting
    def get_type(self):
        self.h_type = None
        while self.h_type is None:
            hop_temp = input("Type: ")
            if 'bo' in hop_temp.lower():
                self.h_type = "'O'"
                htype_display = 'Both (Aroma and Bittering)'
            elif 'b' in hop_temp.lower():
                self.h_type = "'B'"
                htype_display = 'Bittering'
            elif 'a' in hop_temp.lower():
                self.h_type = "'A'"
                htype_display = 'Aroma'
            else:
                print("Enter valid hop type.")
        self.body[2] = (None, ('Type: ' + htype_display))
    # Saves the user provided alpha formatted for mysql, and a tuple for screen formatting
    def get_alpha(self):
        self.alpha = None
        while self.alpha is None:
            hop_temp = input("Alpha Acid %: ")
            try:
                self.alpha = Decimal(hop_temp)
            except decimal.InvalidOperation:
                print("Alpha % must be a numeric value.")
        self.alpha = round(self.alpha, 2)
        hop_temp = str(self.alpha)
        self.body[3] = (None, ('Alpha Acid Content: ' + hop_temp + '%'))
    # Saves the user provided beta formatted for mysql, and a tuple for screen formatting
    def get_beta(self):
        self.beta = None
        while self.beta is None:
            hop_temp = input("Beta Acid %: ")
            try:
                self.beta = Decimal(hop_temp)
            except decimal.InvalidOperation:
                print("Beta % must be a numeric value.")
        self.beta = round(self.beta, 2)
        hop_temp = str(self.beta)
        self.body[4] = (None, ('Beta Acid Content: ' + hop_temp + '%'))
    # Saves the user provided price formatted for mysql, and a tuple for screen formatting
    def get_price(self):
        self.price = None
        while self.price is None:
            hop_temp = input("Price: ")
            try:
                self.price = Decimal(hop_temp)
            except decimal.InvalidOperation:
                print("Price must be a numeric value.")
        self.price = round(self.price, 2)
        hop_temp = str(self.price)
        self.body[5] = (None, ('Price: $' + hop_temp))
    # Saves the user provided quantity formatted for mysql, and a tuple for screen formatting
    def get_qty(self):
        self.qty = None
        while self.qty is None:
            hop_temp = input("Inventory Quantity: ")
            try:
                self.qty = Decimal(hop_temp)
            except decimal.InvalidOperation:
                print("Quantity must be a numeric value.")
        self.qty = round(self.qty, 2)
        hop_temp = str(self.qty)
        self.body[6] = (None, ('Inventory Quantity: ' + hop_temp + ' oz'))
    # Saves the user provided notes formatted for mysql, and a tuple for screen formatting
    def get_notes(self):
        hnotes_lst = []
        hnotes_loop = 0
        self.notes = input("Notes: ")
        for i in self.notes:
            hnotes_lst.append(i)
            hnotes_loop += 1
            if hnotes_loop == 25:
                break
        hnotes_display = ''.join(hnotes_lst)
        self.body[7] = (None, (hnotes_display + '...'))
        self.notes = form.sql_sanitize(self.notes)
        self.notes = form.quote_str(self.notes)
    # Saves the provided (or default) values to the database. Returns True if operation was successful. Returns False if operation was unsuccessful along with error
    def save(self, db):
        try:
            curs = db.cursor()
            query_str = 'INSERT INTO hops(hop_name, hop_origin, hop_type, alpha, beta, hop_price, hop_qty, hop_notes) VALUES ({}, {}, {}, {}, {}, {}, {}, {})'.format(self.name, self.origin, self.h_type, self.alpha, self.beta, self.price, self.qty, self.notes)
            curs.execute(query_str)
            db.commit()
            curs.close()
            return (True, None)
        except mysql.connector.errors.IntegrityError as err:
            return (False, err)
        except mysql.connector.errors.DataError as err:
            return (False, err)

class Yeast:
    def __init__(self, db_id, name, age_rate, prod_id, lab, y_type, alc_tol, flocc, min_atten, max_atten, min_temp, max_temp, price, qty, notes):
        self.db_id = db_id
        self.name = name
        self.age_rate = age_rate
        self.prod_id = prod_id
        self.lab = lab
        self.y_type = y_type
        self.alc_tol = alc_tol
        self.flocc = flocc
        self.min_atten = min_atten
        self.max_atten = max_atten
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.price = price
        self.qty = qty
        self.notes = notes

class Ferm:
    def __init__(self, db_id, name, origin, f_type, grav, colour, dia_pow, prot_cont, price, qty, notes):
        self.db_id = db_id
        self.name = name
        self.origin = origin
        self.f_type = f_type
        self.grav = grav
        self.colour = colour
        self.dia_pow = dia_pow
        self.prot_cont = prot_cont
        self.price = price
        self. qty = qty
        self.notes = notes

class Water:
    def __init__(self, db_id, name, ca, mg, na, so4, cl, hco3, price, qty, notes):
        self.db_id = db_id
        self.name = name
        self.ca = ca
        self.mg = mg
        self.na = na
        self.so4 = so4
        self.cl = cl
        self.hco3 = hco3
        self.price = price
        self.qty = qty
        self.notes = notes

class Misc:
    def __init__(self, db_id, name, measure, m_type, price, qty, notes):
        self.db_id = db_id
        self.name = name
        self.measure = measure
        self.m_type = m_type
        self.price = price
        self.qty = qty
        self.notes = notes