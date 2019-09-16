class Hop:
    def __init__(self, db_id, name, origin, h_type, alpha, beta, price, qty, notes):
        self.db_id = db_id
        self.name = name
        self.origin = origin
        self.h_type = h_type
        self.alpha = alpha
        self.beta = beta
        self.price = price
        self.qty = qty
        self.notes = notes

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