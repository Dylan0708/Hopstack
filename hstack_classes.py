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
        self.name = form.sql_sanitize(temp_name)
        self.name = form.quote_str(self.name)
    # Saves the user provided origin formatted for mysql, and a tuple for screen formatting
    def get_origin(self):
        temp_origin = input("Origin: ")
        self.body[1] = (None, ('Origin: ' + temp_origin))
        self.origin = form.sql_sanitize(temp_origin)
        self.origin = form.quote_str(self.origin)
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
        if hnotes_loop == 25:
            self.body[7] = (None, (hnotes_display + '...'))
        else:
            self.body[7] = (None, (hnotes_display))
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
        except mysql.connector.errors.IntegrityError:
            return (False, 'name')
        except mysql.connector.errors.DataError:
            return (False, 'data')

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
        self.name = form.sql_sanitize(temp_name)
        self.name = form.quote_str(self.name)
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
        self.prod_id = form.sql_sanitize(temp_pid)
        self.prod_id = form.quote_str(self.prod_id)
    # Saves the user provided lab formatted for mysql, and a tuple for screen formatting
    def get_lab(self):
        temp_lab = input("Lab: ")
        self.body[3] = (None, ('Lab: ' + temp_lab))
        self.lab = form.sql_sanitize(temp_lab)
        self.lab = form.quote_str(self.lab)
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
    # Saves the user provided maximum temperature formatted for mysql, and a tuple for screen formatting
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
    # Saves the user provided price formatted for mysql, and a tuple for screen formatting
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
    # Saves the user provided quantity formatted for mysql, and a tuple for screen formatting
    def get_qty(self):
        self.qty = None
        while self.qty == None:
            yst_temp = input("Inventory Quantity: ")
            try:
                self.qty = Decimal(yst_temp)
            except decimal.InvalidOperation:
                print("Quantity must be a numeric value.")
        self.qty = round(self.qty, 2)
        yst_temp = str(self.qty)
        self.body[12] = (None, ('Inventory Quantity: ' + yst_temp + ' Units'))
    # Saves the user provided notes formatted for mysql, and a tuple for screen formatting
    def get_notes(self):
        ynotes_lst = []
        ynotes_loop = 0
        self.notes = input("Notes: ")
        for i in self.notes:
            ynotes_lst.append(i)
            ynotes_loop += 1
            if ynotes_loop == 25:
                break
        ynotes_display = ''.join(ynotes_lst)
        if ynotes_loop == 25:
            self.body[13] = (None, (ynotes_display + '...'))
        else:
            self.body[13] = (None, (ynotes_display))
        self.notes = form.sql_sanitize(self.notes)
        self.notes = form.quote_str(self.notes)
    # Saves the provided (or default) values to the database. Returns True if operation was successful. Returns False if operation was unsuccessful along with error
    def save(self, db):
        try:
            curs = db.cursor()
            query_str = 'INSERT INTO yeast(yeast_name, age_rate, product_id, lab, yeast_type, alcohol_tolerance, flocculation, min_attenuation, max_attenuation, min_temperature, max_temperature, yeast_price, yeast_qty, yeast_notes) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.name, self.age_rate, self.prod_id, self.lab, self.y_type, self.alc_tol, self.flocc, self.min_atten, self.max_atten, self.min_temp, self.max_temp, self.price, self.qty, self.notes)
            curs.execute(query_str)
            db.commit()
            curs.close()
            return (True, None)
        except mysql.connector.errors.IntegrityError:
            return (False, 'name')
        except mysql.connector.errors.DataError:
            return (False, 'data')

class Ferm:
    def __init__(self, name = 'NULL', origin = 'NULL', f_type = 'NULL', grav = 'NULL', colour = 'NULL', dia_pow = 'NULL', prot_cont = 'NULL', price = 0, qty = 0, notes = 'NULL'):
        self.name = name
        self.origin = origin
        self.f_type = f_type
        self.grav = grav
        self.colour = colour
        self.dia_pow = dia_pow
        self.prot_cont = prot_cont
        self.price = price
        self.qty = qty
        self.notes = notes
        self.body = [(None, 'Name'), (None, 'Origin'), (None, 'Type (Base Malt, Specialty Malt, Liquid Extract, Dry Extract, Sugar, Syrup, Juice, Fruit, Adjunct, or Other)'), (None, 'Potential/Specific Gravity'), (None, 'Colour Contribution (Lovibond)'), (None, 'Diastatic Power (Litner)'), (None, 'Protein Content (%)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save'), (None, 'Exit Without Saving')]
    # Saves the user provided name formatted for mysql, and a tuple for screen formatting
    def get_name(self):
        temp_name = input("Name: ")
        self.body[0] = (None, ('Name: ' + temp_name))
        self.name = form.sql_sanitize(temp_name)
        self.name = form.quote_str(self.name)
    # Saves the user provided origin formatted for mysql, and a tuple for screen formatting
    def get_origin(self):
        temp_origin = input("Origin: ")
        self.body[1] = (None, ('Origin: ' + temp_origin))
        self.origin = form.sql_sanitize(temp_origin)
        self.origin = form.quote_str(self.origin)
    # Saves the user provided type formatted for mysql, and a tuple for screen formatting
    def get_type(self):
        self.f_type = None
        while self.f_type == None:
            ferm_temp = input("Type: ")
            if ('b' in ferm_temp.lower()) == True:
                self.f_type = "'B'"
                ftype_display = 'Base Malt'
            elif ('sp' in ferm_temp.lower()) == True:
                self.f_type = "'S'"
                ftype_display = 'Specialty Malt'
            elif ('l' in ferm_temp.lower()) == True:
                self.f_type = "'L'"
                ftype_display = 'Liquid Extract'
            elif ('a' in ferm_temp.lower()) == True:
                self.f_type = "'A'"
                ftype_display = 'Adjunct'
            elif ('d' in ferm_temp.lower()) == True:
                self.f_type = "'D'"
                ftype_display = 'Dry Extract'
            elif ('su' in ferm_temp.lower()) == True:
                self.f_type = "'U'"
                ftype_display = 'Sugar'
            elif ('sy' in ferm_temp.lower()) == True:
                self.f_type = "'Y'"
                ftype_display = 'Syrup'
            elif ('j' in ferm_temp.lower()) == True:
                self.f_type = "'J'"
                ftype_display = 'Juice'
            elif ('f' in ferm_temp.lower()) == True:
                self.f_type = "'F'"
                ftype_display = 'Fruit'
            else:
                self.f_type = "'O'"
                ftype_display = 'Other'
        if self.grav != 'NULL':
            ferm_temp = str(self.grav)
            if self.f_type == "'B'" or self.f_type == "'S'" or self.f_type == "'A'":
                self.body[3] = (None, ('Potential Gravity: ' + ferm_temp))
            else:
                self.body[3] = (None, ('Specific Gravity: ' + ferm_temp))
        if self.dia_pow != 'NULL':
            ferm_temp = str(self.dia_pow)
            if self.f_type != "'B'" and self.f_type != "'S'" and self.f_type != "'A'":
                self.dia_pow = 'NULL'
                self.body[5] = (None, 'Diastatic Power (Litner)')
        if self.prot_cont != 'NULL':
            ferm_temp = str(self.prot_cont)
            if self.f_type != "'B'" and self.f_type != "'S'" and self.f_type != "'A'":
                self.prot_cont = 'NULL'
                self.body[6] = (None, 'Protein Content (%)')
        self.body[2] = (None, ('Type: ' + ftype_display))
    # Saves the user provided potential gravity/specific gravity (depending on type) formatted for mysql, and a tuple for screen formatting
    def get_grav(self):
        if self.f_type == "'B'" or self.f_type == "'S'" or self.f_type == "'A'":
            self.grav = None
            while self.grav == None:
                ferm_temp = input("Potential Gravity: ")
                try:
                    self.grav = Decimal(ferm_temp)
                except decimal.InvalidOperation:
                    print("Potential gravity must be a numeric value.")
            self.grav = round(self.grav, 3)
            ferm_temp = str(self.grav)
            self.body[3] = (None, ('Potential Gravity: ' + ferm_temp))
            return True
        elif self.f_type == "'L'" or self.f_type == "'D'" or self.f_type == "'U'" or self.f_type == "'Y'" or self.f_type == "'J'" or self.f_type == "'F'" or self.f_type == "'O'":
            self.grav = None
            while self.grav == None:
                ferm_temp = input("Specific Gravity: ")
                try:
                    self.grav = Decimal(ferm_temp)
                except decimal.InvalidOperation:
                    print("Specific gravity must be a numeric value.")
            self.grav = round(self.grav, 3)
            ferm_temp = str(self.grav)
            self.body[3] = (None, ('Specific Gravity: ' + ferm_temp))
            return True
        else:
            return False
    # Saves the user provided lovibond formatted for mysql, and a tuple for screen formatting
    def get_col(self):
        self.colour = None
        while self.colour == None:
            ferm_temp = input("Colour Contribution: ")
            try:
                self.colour = Decimal(ferm_temp)
            except decimal.InvalidOperation:
                print("Colour contribution must be a numeric value.")
        self.colour = round(self.colour, 2)
        ferm_temp = str(self.colour)
        self.body[4] = (None, ('Colour Contribution: ' + ferm_temp + ' Lovibond'))
    # Saves the user provided diastatic power (depending on type) formatted for mysql, and a tuple for screen formatting
    def get_dp(self):
        if self.f_type == "'B'" or self.f_type == "'S'" or self.f_type == "'A'":
            self.dia_pow = None
            while self.dia_pow == None:
                ferm_temp = input("Diastatic Power: ")
                try:
                    self.dia_pow = Decimal(ferm_temp)
                except decimal.InvalidOperation:
                    print("Diastatic power must be a numeric value.")
            self.dia_pow = round(self.dia_pow, 1)
            ferm_temp = str(self.dia_pow)
            self.body[5] = (None, ('Diastatic Power: ' + ferm_temp + ' Litner'))
            return True
        else:
            return False
    # Saves the user provided protein content (depending on type) formatted for mysql, and a tuple for screen formatting
    def get_pc(self):
        if self.f_type == "'B'" or self.f_type == "'S'" or self.f_type == "'A'":
            self.prot_cont = None
            while self.prot_cont == None:
                ferm_temp = input("Protein Content %: ")
                try:
                    self.prot_cont = Decimal(ferm_temp)
                except decimal.InvalidOperation:
                    print("Protein content must be a numeric value.")
            self.prot_cont = round(self.prot_cont, 1)
            ferm_temp = str(self.prot_cont)
            self.body[6] = (None, ('Protein Content: ' + ferm_temp + '%'))
            return True
        else:
            return False
    # Saves the user provided price formatted for mysql, and a tuple for screen formatting
    def get_price(self):
        self.price = None
        while self.price == None:
            ferm_temp = input("Price: ")
            try:
                self.price = Decimal(ferm_temp)
            except decimal.InvalidOperation:
                print("Price must be a numeric value.")
        self.price = round(self.price, 2)
        ferm_temp = str(self.price)
        self.body[7] = (None, ('Price: $' + ferm_temp))
    # Saves the user provided quantity formatted for mysql, and a tuple for screen formatting
    def get_qty(self):
        self.qty = None
        while self.qty == None:
            ferm_temp = input("Inventory Quantity: ")
            try:
                self.qty = Decimal(ferm_temp)
            except decimal.InvalidOperation:
                print("Quantity must be a numeric value.")
        self.qty = round(self.qty, 2)
        ferm_temp = str(self.qty)
        self.body[8] = (None, ('Inventory Quantity: ' + ferm_temp + ' lbs'))
    # Saves the user provided notes formatted for mysql, and a tuple for screen formatting
    def get_notes(self):
        fnotes_lst = []
        fnotes_loop = 0
        self.notes = input("Notes: ")
        for i in self.notes:
            fnotes_lst.append(i)
            fnotes_loop += 1
            if fnotes_loop == 25:
                break
        fnotes_display = ''.join(fnotes_lst)
        if fnotes_loop == 25:
            self.body[9] = (None, (fnotes_display + '...'))
        else:
            self.body[9] = (None, (fnotes_display))
        self.notes = form.sql_sanitize(self.notes)
        self.notes = form.quote_str(self.notes)
    # Saves the provided (or default) values to the database. Returns True if operation was successful. Returns False if operation was unsuccessful along with error
    def save(self, db):
        try:
            curs = db.cursor()
            query_str = 'INSERT INTO fermentables(ferm_name, ferm_origin, ferm_type, potential_gravity, colour, diastatic_power, protein_content, ferm_price, ferm_qty, ferm_notes) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.name, self.origin, self.f_type, self.grav, self.colour, self.dia_pow, self.prot_cont, self.price, self.qty, self.notes)
            curs.execute(query_str)
            db.commit()
            curs.close()
            return (True, None)
        except mysql.connector.errors.IntegrityError:
            return (False, 'name')
        except mysql.connector.errors.DataError:
            return (False, 'data') 

class Water:
    def __init__(self, name = 'NULL', ph = 'NULL', ca = 'NULL', mg = 'NULL', na = 'NULL', so4 = 'NULL', cl = 'NULL', hco3 = 'NULL', price = 0, qty = 0, notes = 'NULL'):
        self.name = name
        self.ph = ph
        self.ca = ca
        self.mg = mg
        self.na = na
        self.so4 = so4
        self.cl = cl
        self.hco3 = hco3
        self.price = price
        self.qty = qty
        self.notes = notes
        self.body = [(None, 'Name'), (None, 'PH'), (None, 'Calcium (ppm)'), (None, 'Magnesium (ppm)'), (None, 'Sodium (ppm)'), (None, 'Sulfate (ppm)'), (None, 'Chloride (ppm)'), (None, 'Bicarbonate (ppm)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save'), (None, 'Exit Without Saving')]
    # Saves the user provided name formatted for mysql, and a tuple for screen formatting
    def get_name(self):
        temp_name = input("Name: ")
        self.body[0] = (None, ('Name: ' + temp_name))
        self.name = form.sql_sanitize(temp_name)
        self.name = form.quote_str(self.name)
    # Saves the user provided ph formatted for mysql, and a tuple for screen formatting
    def get_ph(self):
        self.ph = None
        while self.ph == None:
            wat_temp = input("PH: ")
            try:
                self.ph = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("PH must be a numeric value.")
        self.ph = round(self.ph, 2)
        wat_temp = str(self.ph)
        self.body[1] = (None, ('PH: ' + wat_temp))
    # Saves the user provided calcium ppm formatted for mysql, and a tuple for screen formatting
    def get_ca(self):
        self.ca = None
        while self.ca == None:
            wat_temp = input("Calcium (ppm): ")
            try:
                self.ca = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Calcium must be a numeric value.")
        self.ca = round(self.ca, 2)
        wat_temp = str(self.ca)
        self.body[2] = (None, ('Calcium: ' + wat_temp + ' ppm'))
    # Saves the user provided magnesium ppm formatted for mysql, and a tuple for screen formatting
    def get_mg(self):
        self.mg = None
        while self.mg == None:
            wat_temp = input("Magnesium (ppm): ")
            try:
                self.mg = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Magnesium must be a numeric value.")
        self.mg = round(self.mg, 2)
        wat_temp = str(self.mg)
        self.body[3] = (None, ('Magnesium: ' + wat_temp + ' ppm'))
    # Saves the user provided sodium ppm formatted for mysql, and a tuple for screen formatting
    def get_na(self):
        self.na = None
        while self.na == None:
            wat_temp = input("Sodium (ppm): ")
            try:
                self.na = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Sodium must be a numeric value.")
        self.na = round(self.na, 2)
        wat_temp = str(self.na)
        self.body[4] = (None, ('Sodium: ' + wat_temp + ' ppm'))
    # Saves the user provided sulfate ppm formatted for mysql, and a tuple for screen formatting
    def get_so4(self):
        self.so4 = None
        while self.so4 == None:
            wat_temp = input("Sulfate (ppm): ")
            try:
                self.so4 = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Sulfate must be a numeric value.")
        self.so4 = round(self.so4, 2)
        wat_temp = str(self.so4)
        self.body[5] = (None, ('Sulfate: ' + wat_temp + ' ppm'))
    # Saves the user provided chloride ppm formatted for mysql, and a tuple for screen formatting
    def get_cl(self):
        self.cl = None
        while self.cl == None:
            wat_temp = input("Chloride (ppm): ")
            try:
                self.cl = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Chloride must be a numeric value.")
        self.cl = round(self.cl, 2)
        wat_temp = str(self.cl)
        self.body[6] = (None, ('Chloride: ' + wat_temp + ' ppm'))
    # Saves the user provided bicarbonate ppm formatted for mysql, and a tuple for screen formatting
    def get_hco3(self):
        self.hco3 = None
        while self.hco3 == None:
            wat_temp = input("Bicarbonate (ppm): ")
            try:
                self.hco3 = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Bicarbonate must be a numeric value.")
        self.hco3 = round(self.hco3, 2)
        wat_temp = str(self.hco3)
        self.body[7] = (None, ('Bicarbonate: ' + wat_temp + ' ppm'))
    # Saves the user provided price formatted for mysql, and a tuple for screen formatting
    def get_price(self):
        self.price = None
        while self.price == None:
            wat_temp = input("Price: ")
            try:
                self.price = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Price must be a numeric value.")
        self.price = round(self.price, 2)
        wat_temp = str(self.price)
        self.body[8] = (None, ('Price: $' + wat_temp))
    # Saves the user provided quantity formatted for mysql, and a tuple for screen formatting
    def get_qty(self):
        self.qty = None
        while self.qty == None:
            wat_temp = input("Inventory Quantity: ")
            try:
                self.qty = Decimal(wat_temp)
            except decimal.InvalidOperation:
                print("Quantity must be a numeric value.")
        self.qty = round(self.qty, 2)
        wat_temp = str(self.qty)
        self.body[9] = (None, ('Inventory Quantity: ' + wat_temp + ' gal'))
    # Saves the user provided notes formatted for mysql, and a tuple for screen formatting
    def get_notes(self):
        wnotes_lst = []
        wnotes_loop = 0
        self.notes = input("Notes: ")
        for i in self.notes:
            wnotes_lst.append(i)
            wnotes_loop += 1
            if wnotes_loop == 25:
                break
        wnotes_display = ''.join(wnotes_lst)
        if wnotes_loop == 25:
            self.body[10] = (None, (wnotes_display + '...'))
        else:
            self.body[10] = (None, (wnotes_display))
        self.notes = form.sql_sanitize(self.notes)
        self.notes = form.quote_str(self.notes)
    # Saves the provided (or default) values to the database. Returns True if operation was successful. Returns False if operation was unsuccessful along with error
    def save(self, db):
        try:
            curs = db.cursor()
            query_str = 'INSERT INTO water(water_name, ph, calcium, magnesium, sodium, sulfate, chloride, bicarbonate, water_price, water_qty, water_notes) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.name, self.ph, self.ca, self.mg, self.na, self.so4, self.cl, self.hco3, self.price, self.qty, self.notes)
            curs.execute(query_str)
            db.commit()
            curs.close()
            return (True, None)
        except mysql.connector.errors.IntegrityError:
            return (False, 'name')
        except mysql.connector.errors.DataError:
            return (False, 'data') 

class Misc:
    def __init__(self, name = 'NULL', unit = 'NULL', m_type = 'NULL', price = 0, qty = 0, notes = 'NULL'):
        self.name = name
        self.unit = unit
        self.m_type = m_type
        self.price = price
        self.qty = qty
        self.notes = notes
        self.body = [(None, 'Name'), (None, 'Unit (Gallons, Fluid Ounces, Pounds, Dry Ounces, or Units)'), (None, 'Type (Flavour, Water Agent, Yeast Nutrient, Enzyme, Fining, or Other)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save'), (None, 'Exit Without Saving')]
    # Saves the user provided name formatted for mysql, and a tuple for screen formatting
    def get_name(self):
        temp_name = input("Name: ")
        self.body[0] = (None, ('Name: ' + temp_name))
        self.name = form.sql_sanitize(temp_name)
        self.name = form.quote_str(self.name)
    # Saves the user provided unit formatted for mysql, and a tuple for screen formatting
    def get_unit(self):
        self.unit = None
        while self.unit is None:
            msc_temp = input("Unit: ")
            if ('u' in msc_temp.lower()) == True:
                self.unit = "'U'"
                munit_display = 'Units'
            elif ('d' in msc_temp.lower()) == True:
                self.unit = "'w'"
                munit_display = 'Dry Ounces'
            elif ('g' in msc_temp.lower()) == True:
                self.unit = "'V'"
                munit_display = 'Gallons'
            elif ('f' in msc_temp.lower()) == True:
                self.unit = "'v'"
                munit_display = 'Fluid Ounces'
            elif ('p' in msc_temp.lower()) == True:
                self.unit = "'W'"
                munit_display = 'Pounds'
            else:
                print("Enter valid unit.")
        self.body[1] = (None, ('Unit: ' + munit_display))
    # Saves the user provided type formatted for mysql, and a tuple for screen formatting
    def get_type(self):
        self.m_type = None
        while self.m_type is None:
            msc_temp = input("Type: ")
            if ('fl' in msc_temp.lower()) == True:
                self.m_type = "'Fl'"
                mtype_display = 'Flavour'
            elif ('w' in msc_temp.lower()) == True:
                self.m_type = "'Wa'"
                mtype_display = 'Water Agent'
            elif ('y' in msc_temp.lower()) == True:
                self.m_type = "'Yn'"
                mtype_display = 'Yeast Nutrient'
            elif ('enz' in msc_temp.lower()) == True:
                self.m_type = "'En'"
                mtype_display = 'Enzyme'
            elif ('fi' in msc_temp.lower()) == True:
                self.m_type = "'Fi'"
                mtype_display = 'Fining'
            elif ('ot' in msc_temp.lower()) == True:
                self.m_type = "'Ot'"
                mtype_display = 'Other'
            else:
                print("Enter valid misc type.")
        self.body[2] = (None, ('Type: ' + mtype_display))
