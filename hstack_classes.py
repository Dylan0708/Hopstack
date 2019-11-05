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
    def __init__(self, name = 'NULL', age_rate = 21, prod_id = 'NULL', lab = 'NULL', y_type = 'NULL', alc_tol = 'NULL', flocc = 'NULL', min_atten = 'NULL', max_atten = 'NULL', min_temp = 'NULL', max_temp = 'NULL', price = 0, qty = 0, notes = 'NULL'):
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
        self.body = [(None, 'Name'), (None, 'Monthly Viability Loss (%)'), (None, 'Product ID'), (None, 'Lab'), (None, 'Type (Ale, Lager, Brett, Diastaticus, Kveik, Pediococcus, Lactobacillus, or Mixed Culture)'), (None, 'Alcohol Tolerance (%)'), (None, 'Flocculation (Low, Medium, or High)'), (None, 'Minimum Attenuation (%)'), (None, 'Maximum Attenuation (%)'), (None, 'Minimum Temperature (°C)'), (None, 'Maximum Temperature (°C)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save'), (None, 'Exit Without Saving')]
    # Saves the user provided name formatted for mysql, and a tuple for screen formatting
    def get_name(self):
        temp_name = input("Name: ")
        self.body[0] = (None, ('Name: ' + temp_name))
        self.name = form.quote_str(temp_name)
    # Saves the user provided age rate formatted for mysql, and a tuple for screen formatting
    def get_ar(self):
        self.age_rate = None
        while self.age_rate is None:
            self.age_rate = input("Monthly Viability Loss: ")
            try:
                self.age_rate = Decimal(self.age_rate)
                self.age_rate = int(round(self.age_rate))
            except decimal.InvalidOperation:
                print("Viability loss must be a numeric value.")
                self.age_rate = None
            if self.age_rate is not None:
                if self.age_rate > 100 or self.age_rate < 0:
                    self.age_rate = None
                    print("Viability loss must be between 0 and 100.")
        self.body[1] = (None, ('Monthly Viability Loss: ' + str(self.age_rate) + '%'))
    # Saves the user provided product id formatted for mysql, and a tuple for screen formatting
    def get_pid(self):
        temp_pid = input("Product ID: ")
        self.body[2] = (None, ('Product ID: ' + temp_pid))
        self.prod_id = form.quote_str(temp_pid)
    # Saves the user provided lab formatted for mysql, and a tuple for screen formatting
    def get_lab(self):
        temp_lab = input("Lab: ")
        self.body[3] = (None, ('Lab: ' + temp_lab))
        self.lab = form.quote_str(temp_lab)
    # Saves the user provided type formatted for mysql, and a tuple for screen formatting
    def get_type(self):
        self.y_type = None
        while self.y_type is None:
            yst_temp = input("Type: ")
            if ('lac' in yst_temp.lower()) == True:
                self.y_type = "'Lac'"
                ytype_display = 'Lactobacillus'
            elif ('lag' in yst_temp.lower()) == True:
                self.y_type = "'Lag'"
                ytype_display = 'Lager'
            elif ('p' in yst_temp.lower()) == True:
                self.y_type = "'Ped'"
                ytype_display = 'Pediococcus'
            elif ('d' in yst_temp.lower()) == True:
                self.y_type = "'Dia'"
                ytype_display = 'Diastaticus'
            elif ('b' in yst_temp.lower()) == True:
                self.y_type = "'Brt'"
                ytype_display = 'Brettanomyces'
            elif ('ale' in yst_temp.lower()) == True:
                self.y_type = "'Ale'"
                ytype_display = 'Ale'
            elif ('k' in yst_temp.lower()) == True:
                self.y_type = "'Kvk'"
                ytype_display = 'Kveik'
            elif ('m' in yst_temp.lower()) == True:
                self.y_type = "'Mix'"
                ytype_display = 'Mixed Culture'
            else:
                print("Enter valid yeast/bacteria type.")
        self.body[4] = (None, ('Type: ' + ytype_display))
    # Saves the user provided alcohol tolerance formatted for mysql, and a tuple for screen formatting
    def get_alc(self):
        self.alc_tol = None
        while self.alc_tol == None:
            self.alc_tol = input("Alcohol Tolerance: ")
            try:
                self.alc_tol = Decimal(self.alc_tol)
                self.alc_tol = int(round(self.alc_tol))
            except decimal.InvalidOperation:
                print("Alcohol tolerance must be a numeric value.")
                self.alc_tol = None
        self.body[5] = (None, ('Alcohol Tolerance: ' + str(self.alc_tol) + '%'))
    # Saves the user provided flocculation formatted for mysql, and a tuple for screen formatting
    def get_floc(self):
        self.flocc = None
        while self.flocc == None:
            yst_temp = input("Flocculation: ")
            if ('h' in yst_temp.lower()) == True:
                self.flocc = "'H'"
                yfloc_display = 'High'
            elif ('m' in yst_temp.lower()) == True:
                self.flocc = "'M'"
                yfloc_display = 'Medium'
            elif ('l' in yst_temp.lower()) == True:
                self.flocc = "'L'"
                yfloc_display = 'Low'
            else:
                print("Enter valid flocculation level.")
        self.body[6] = (None, ('Flocculation: ' + yfloc_display))
    # Saves the user provided minimum attenuation formatted for mysql, and a tuple for screen formatting
    def get_minat(self):
        self.min_atten = None
        while self.min_atten == None:
            self.min_atten = input("Minimum Attenuation: ")
            try:
                self.min_atten = Decimal(self.min_atten)
                self.min_atten = int(round(self.min_atten))
            except decimal.InvalidOperation:
                print("Minimum attenuation must be a numeric value.")
                self.min_atten = None
            if self.min_atten != None:
                if self.min_atten > 100 or self.min_atten < 0:
                    self.min_atten = None
                    print("Minimum attenuation must be between 0 and 100.")
                elif type(self.max_atten) == int:
                    if self.min_atten > self.max_atten:
                        self.min_atten = None
                        print("Minimum attenuation can't be higher than maximum attenuation.")
        self.body[7] = (None, ('Minimum Attenuation: ' + str(self.min_atten) + '%'))
    # Saves the user provided maximum attenuation formatted for mysql, and a tuple for screen formatting
    def get_maxat(self):
        self.max_atten = None
        while self.max_atten == None:
            self.max_atten = input("Maximum Attenuation: ")
            try:
                self.max_atten = Decimal(self.max_atten)
                self.max_atten = int(round(self.max_atten))
            except decimal.InvalidOperation:
                print("Maximum attenuation must be a numeric value.")
                self.max_atten = None
            if self.max_atten != None:
                if self.max_atten > 100 or self.max_atten < 0:
                    self.max_atten = None
                    print("Maximum attenuation must be between 0 and 100.")
                elif type(self.min_atten) == int:
                    if self.min_atten > self.max_atten:
                        self.max_atten = None
                        print("Maximum attenuation can't be lower than minimum attenuation.")
        self.body[8] = (None, ('Maximum Attenuation: ' + str(self.max_atten) + '%'))
    # Saves the user provided minimum temperature formatted for mysql, and a tuple for screen formatting
    def get_mintmp(self):
        self.min_temp = None
        while self.min_temp == None:
            self.min_temp = input("Minimum Temperature: ")
            try:
                self.min_temp = Decimal(self.min_temp)
                self.min_temp = int(round(self.min_temp))
            except decimal.InvalidOperation:
                print("Minimum temperature must be a numeric value.")
                self.min_temp = None
            if self.min_temp != None:
                if type(self.max_temp) == int:
                    if self.min_temp > self.max_temp:
                        self.min_temp = None
                        print("Minimum temperature can't be higher than maximum temperature.")
        self.body[9] = (None, ('Minimum Temperature: ' + str(self.min_temp) + '°C'))
    # Saves the user provided minimum temperature formatted for mysql, and a tuple for screen formatting
    def get_maxtmp(self):
        self.max_temp = None
        while self.max_temp == None:
            self.max_temp = input("Maximum Temperature: ")
            try:
                self.max_temp = Decimal(self.max_temp)
                self.max_temp = int(round(self.max_temp))
            except decimal.InvalidOperation:
                print("Maximum temperature must be a numeric value.")
                self.max_temp = None
            if self.max_temp != None:
                if type(self.min_temp) == int:
                    if self.min_temp > self.max_temp:
                        self.max_temp = None
                        print("Maximum temperature can't be lower than minimum temperature.")
        self.body[10] = (None, ('Maximum Temperature: ' + str(self.max_temp) + '°C'))
    def get_price(self):
        self.price = None
        while self.price == None:
            yst_temp = input("Price: ")
            try:
                self.price = Decimal(yst_temp)
            except decimal.InvalidOperation:
                print("Price must be a numeric value.")
        self.price = round(self.price, 2)
        yst_temp = str(self.price)
        self.body[11] = (None, ('Price: $' + yst_temp))

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