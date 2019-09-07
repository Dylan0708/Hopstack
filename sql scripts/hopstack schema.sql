-- Initilize Tables
CREATE TABLE hops 
(
    hop_id INT AUTO_INCREMENT, 
    hop_name VARCHAR(20) NOT NULL, 
    hop_origin VARCHAR(20), -- Country of origin
    hop_type VARCHAR(1), -- A = Aroma, B = Bittering, O = Both
    alpha DECIMAL(4, 2), -- Alpha acid content in %
    beta DECIMAL(4, 2), -- Beta acid content in %
    hop_price DECIMAL (4, 2) DEFAULT 0, 
    hop_qty DECIMAL(5, 2) DEFAULT 0,
    hop_notes VARCHAR(1000),
    PRIMARY KEY(hop_id)
);

CREATE TABLE yeast 
(
    yeast_id INT AUTO_INCREMENT,
    yeast_name VARCHAR(20) NOT NULL, 
    production_date DATE DEFAULT (CURRENT_DATE()), 
    age_rate INT DEFAULT 21, -- % viability lost every month
    product_id VARCHAR(10), -- Lab provided product id
    lab VARCHAR(20), -- Lab of origin
    yeast_type VARCHAR(3), -- Ale, Lag, Brt, Dia, Ped, Lac, Kvk, Mix
    alcohol_tolerance INT, -- Alcohol tolerance in %
    flocculation VARCHAR(1), -- L = Low, M = Medium, H = High
    min_attenuation INT, -- Minimum attenuation in &
    max_attenuation INT, -- Maximum attenuation in %
    min_temperature INT, -- Minimum temperature in C
    max_temperature INT, -- Maximum temperature in C
    yeast_price DECIMAL(4, 2) DEFAULT 0, 
    yeast_qty DECIMAL(5, 2) DEFAULT 0,
    yeast_notes VARCHAR(1000), 
    PRIMARY KEY(yeast_id)
);

CREATE TABLE fermentables
(
	ferm_id INT AUTO_INCREMENT,
	ferm_name VARCHAR(20) NOT NULL,
	ferm_origin VARCHAR(20), -- Country of origin
	ferm_type VARCHAR(1), -- B = Base, S = Specialty, L = Liquid Extract, D = Dry Extract, U = Sugar, Y = Syrup, J = Juice, F = Fruit, A = Adjunct, O = Other
	potential_gravity DECIMAL(4, 3), -- Base gravity potential for ferm_type B, S, A / Specific gravity for ferm_type L, D, U, Y, J, F, O
	colour DECIMAL(5, 2), -- Colour contribution in Lovibond
	diastatic_power DECIMAL(4, 1), -- Measure of enzyme content in Litner for ferm_type B, S, A
	protein_content DECIMAL(3, 1), -- Measure of protein content in % for ferm_type B, S, A
	ferm_price DECIMAL(4, 2) DEFAULT 0,
	ferm_qty DECIMAL(5, 2) DEFAULT 0,
	ferm_notes VARCHAR(1000),
	PRIMARY KEY(ferm_id)
);

CREATE TABLE water
(
	water_id INT AUTO_INCREMENT,
	water_name VARCHAR(20) NOT NULL,
	ph DECIMAL(3, 2),
	alkalinity INT, -- ppm as CaCO3
	effective_hardness INT, -- ppm as CaCO3
	residual_alkalinity INT, -- ppm as CaCO3
	calcium DECIMAL(5, 2), -- ppm
	magnesium DECIMAL(5, 2), -- ppm
	sodium DECIMAL(5, 2), -- ppm
	sulfate DECIMAL(5, 2), -- ppm
	chloride DECIMAL(5, 2), -- ppm
	bicarbonate DECIMAL(5, 2), -- ppm
	water_price DECIMAL(4, 2) DEFAULT 0,
	water_qty DECIMAL(5, 2) DEFAULT 0,
	water_notes VARCHAR(1000),
	PRIMARY KEY(water_id)
);

CREATE TABLE misc
(
	misc_id INT AUTO_INCREMENT,
	misc_name VARCHAR(20) NOT NULL,
	measurement VARCHAR(1), -- V = Volume, W = Weight, U = Unit
	misc_type VARCHAR(2), -- Fl = Flavour, Wa = Water Agent, Yn = Yeast Nutrient, En = Enzyme, Fi = Fining, Ot = Other
	misc_price DECIMAL(4, 2) DEFAULT 0,
	misc_qty DECIMAL(5, 2) DEFAULT 0,
	misc_notes VARCHAR(1000),
	PRIMARY KEY(misc_id)
);

CREATE TABLE inventory 
(
	inv_id INT AUTO_INCREMENT, 
    name VARCHAR(20), 
    type VARCHAR(1), 
    qty DECIMAL(5, 2), 
    price DECIMAL(4, 2),
    hop_id INT DEFAULT NULL,
    yeast_id INT DEFAULT NULL,
    ferm_id INT DEFAULT NULL,
    water_id INT DEFAULT NULL, 
    misc_id INT DEFAULT NULL,
    PRIMARY KEY(inv_id),
    FOREIGN KEY(hop_id) REFERENCES hops(hop_id) ON DELETE CASCADE,
    FOREIGN KEY(yeast_id) REFERENCES yeast(yeast_id) ON DELETE CASCADE,
    FOREIGN KEY(ferm_id) REFERENCES fermentables(ferm_id) ON DELETE CASCADE,
    FOREIGN KEY(water_id) REFERENCES water(water_id) ON DELETE CASCADE,
    FOREIGN KEY(misc_id) REFERENCES misc(misc_id) ON DELETE CASCADE
);

CREATE TABLE recipe
(
	recipe_name VARCHAR(50),
    iteration INT DEFAULT 1,
	recipe_ingredients JSON,
	recipe_total DECIMAL(6, 2),
	functional_cost DECIMAL(6, 2),
	recipe_notes VARCHAR(1000),
    recipe_changes JSON,
    PRIMARY KEY(recipe_name)
);

CREATE TABLE iteration_notes
(
	recipe_name VARCHAR(50),
    iteration INT DEFAULT 1,
    change_log JSON,
    PRIMARY KEY(recipe_name, iteration),
    FOREIGN KEY(recipe_name) REFERENCES recipe(recipe_name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE list
(
	list_id INT AUTO_INCREMENT,
	list_name VARCHAR(50),
	timestamp DATETIME DEFAULT(NOW()),
	list_ingredients JSON,
	list_total DECIMAL(7, 2),
	list_notes VARCHAR(1000),
    PRIMARY KEY(list_id)
);

-- Set Triggers
DELIMITER $$
CREATE
	TRIGGER add_hop AFTER INSERT
    ON hops
    FOR EACH ROW BEGIN
		IF (NEW.hop_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, hop_id) VALUES(NEW.hop_name, 'h', NEW.hop_qty, NEW.hop_price, NEW.hop_id);
		END IF;
	END$$

CREATE
	TRIGGER update_hop AFTER UPDATE
    ON hops
    FOR EACH ROW BEGIN
		IF (OLD.hop_qty = 0 AND NEW.hop_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, hop_id) VALUES(NEW.hop_name, 'h', NEW.hop_qty, NEW.hop_price, NEW.hop_id);
		ELSEIF (OLD.hop_qty > 0 AND NEW.hop_qty = 0) THEN
			DELETE FROM inventory WHERE(inventory.hop_id = NEW.hop_id);
		ELSEIF (OLD.hop_qty > 0 AND NEW.hop_qty > 0) THEN
			UPDATE inventory SET name = NEW.hop_name, qty = NEW.hop_qty, price = NEW.hop_price WHERE (inventory.hop_id = NEW.hop_id);
		END IF;
	END$$

CREATE
	TRIGGER add_yeast AFTER INSERT
    ON yeast
    FOR EACH ROW BEGIN
		IF (NEW.yeast_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, yeast_id) VALUES(NEW.yeast_name, 'y', NEW.yeast_qty, NEW.yeast_price, NEW.yeast_id);
		END IF;
	END$$

CREATE
	TRIGGER update_yeast AFTER UPDATE
    ON yeast
    FOR EACH ROW BEGIN
		IF (OLD.yeast_qty = 0 AND NEW.yeast_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, yeast_id) VALUES(NEW.yeast_name, 'y', NEW.yeast_qty, NEW.yeast_price, NEW.yeast_id);
		ELSEIF (OLD.yeast_qty > 0 AND NEW.yeast_qty = 0) THEN
			DELETE FROM inventory WHERE(inventory.yeast_id = NEW.yeast_id);
		ELSEIF (OLD.yeast_qty > 0 AND NEW.yeast_qty > 0) THEN
			UPDATE inventory SET name = NEW.yeast_name, qty = NEW.yeast_qty, price = NEW.yeast_price WHERE (inventory.yeast_id = NEW.yeast_id);
		END IF;
	END$$

CREATE
	TRIGGER add_ferm AFTER INSERT
    ON fermentables
    FOR EACH ROW BEGIN
		IF (NEW.ferm_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, ferm_id) VALUES(NEW.ferm_name, 'f', NEW.ferm_qty, NEW.ferm_price, NEW.ferm_id);
		END IF;
	END$$

CREATE
	TRIGGER update_ferm AFTER UPDATE
    ON fermentables
    FOR EACH ROW BEGIN
		IF (OLD.ferm_qty = 0 AND NEW.ferm_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, ferm_id) VALUES(NEW.ferm_name, 'f', NEW.ferm_qty, NEW.ferm_price, NEW.ferm_id);
		ELSEIF (OLD.ferm_qty > 0 AND NEW.ferm_qty = 0) THEN
			DELETE FROM inventory WHERE(inventory.ferm_id = NEW.ferm_id);
		ELSEIF (OLD.ferm_qty > 0 AND NEW.ferm_qty > 0) THEN
			UPDATE inventory SET name = NEW.ferm_name, qty = NEW.ferm_qty, price = NEW.ferm_price WHERE (inventory.ferm_id = NEW.ferm_id);
		END IF;
	END$$

CREATE
	TRIGGER add_water AFTER INSERT
    ON water
    FOR EACH ROW BEGIN
		IF (NEW.water_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, water_id) VALUES(NEW.water_name, 'w', NEW.water_qty, NEW.water_price, NEW.water_id);
		END IF;
	END$$

CREATE
	TRIGGER update_water AFTER UPDATE
    ON water
    FOR EACH ROW BEGIN
		IF (OLD.water_qty = 0 AND NEW.water_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, water_id) VALUES(NEW.water_name, 'w', NEW.water_qty, NEW.water_price, NEW.water_id);
		ELSEIF (OLD.water_qty > 0 AND NEW.water_qty = 0) THEN
			DELETE FROM inventory WHERE(inventory.water_id = NEW.water_id);
		ELSEIF (OLD.water_qty > 0 AND NEW.water_qty > 0) THEN
			UPDATE inventory SET name = NEW.water_name, qty = NEW.water_qty, price = NEW.water_price WHERE (inventory.water_id = NEW.water_id);
		END IF;
	END$$
    
CREATE
	TRIGGER add_misc AFTER INSERT
    ON misc
    FOR EACH ROW BEGIN
		IF (NEW.misc_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, misc_id) VALUES(NEW.misc_name, 'm', NEW.misc_qty, NEW.misc_price, NEW.misc_id);
		END IF;
	END$$

CREATE
	TRIGGER update_misc AFTER UPDATE
    ON misc
    FOR EACH ROW BEGIN
		IF (OLD.misc_qty = 0 AND NEW.misc_qty > 0) THEN
			INSERT INTO inventory(name, type, qty, price, misc_id) VALUES(NEW.misc_name, 'm', NEW.misc_qty, NEW.misc_price, NEW.misc_id);
		ELSEIF (OLD.misc_qty > 0 AND NEW.misc_qty = 0) THEN
			DELETE FROM inventory WHERE(inventory.misc_id = NEW.misc_id);
		ELSEIF (OLD.misc_qty > 0 AND NEW.misc_qty > 0) THEN
			UPDATE inventory SET name = NEW.misc_name, qty = NEW.misc_qty, price = NEW.misc_price WHERE (inventory.misc_id = NEW.misc_id);
		END IF;
	END$$
    
CREATE
	TRIGGER add_recipe AFTER INSERT
    ON recipe
    FOR EACH ROW BEGIN
		INSERT INTO iteration_notes(recipe_name, change_log) VALUES(NEW.recipe_name, '["Initial Recipe"]');
	END$$
    
CREATE
	TRIGGER update_recipe AFTER UPDATE
    ON recipe 
    FOR EACH ROW BEGIN
		INSERT INTO iteration_notes(recipe_name, iteration, change_log) VALUES(NEW.recipe_name, NEW.iteration, NEW.recipe_changes);
	END$$
DELIMITER ;
