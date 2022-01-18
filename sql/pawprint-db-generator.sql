SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `pawprint` DEFAULT CHARACTER SET utf8 ;
USE `pawprint` ;

CREATE TABLE IF NOT EXISTS `pawprint`.`Admin` (
  `admin_id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(64) NOT NULL,
  `name` VARCHAR(64) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`admin_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`Location` (
  `location_id` INT NOT NULL AUTO_INCREMENT,
  `province` VARCHAR(64) NOT NULL,
  `city` VARCHAR(64) NOT NULL,
  `street` VARCHAR(64) NOT NULL,
  `address_number` INT(11) NOT NULL,
  `postal_code` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`location_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`Breeder` (
  `breeder_id` INT NOT NULL AUTO_INCREMENT,
  `phone_number` VARCHAR(12) NULL,
  `email` VARCHAR(64) NOT NULL,
  `name` VARCHAR(64) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  `location_id` INT(11) NOT NULL,
  PRIMARY KEY (`breeder_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC),
  INDEX `location_id_idx` (`location_id` ASC),
  CONSTRAINT `location_id`
    FOREIGN KEY (`location_id`)
    REFERENCES `pawprint`.`Location` (`location_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`Breed` (
  `breed_id` INT(11) NOT NULL AUTO_INCREMENT,
  `breed_name` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`breed_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`Parent` (
  `parent_id` INT(11) NOT NULL AUTO_INCREMENT,
  `breed_id` INT(11) NOT NULL,
  `name` VARCHAR(64) NOT NULL,
  `birth_date` DATETIME NULL,
  `description` TEXT NULL,
  `sex_m` TINYINT(1) NOT NULL,
  `breeder_id` INT(11) NOT NULL,
  PRIMARY KEY (`parent_id`),
  INDEX `breeder_id_idx` (`breeder_id` ASC),
  INDEX `breed_id_idx` (`breed_id` ASC),
  CONSTRAINT `breeder_parent_id`
    FOREIGN KEY (`breeder_id`)
    REFERENCES `pawprint`.`Breeder` (`breeder_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `breed_id`
    FOREIGN KEY (`breed_id`)
    REFERENCES `pawprint`.`Breed` (`breed_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`Litter` (
  `litter_id` INT(11) NOT NULL AUTO_INCREMENT,
  `breed_id` INT(11) NOT NULL,
  `birth_date` DATETIME NOT NULL,
  `parent_1_id` INT(11) NULL,
  `parent_2_id` INT(11) NULL,
  `breeder_id` INT(11) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`litter_id`),
  INDEX `parent_id_idx1` (`parent_2_id` ASC),
  INDEX `parent_id_idx` (`parent_1_id` ASC),
  INDEX `breeder_id_idx` (`breeder_id` ASC),
  INDEX `breed_id_idx` (`breed_id` ASC),
  CONSTRAINT `parent_1_id`
    FOREIGN KEY (`parent_1_id`)
    REFERENCES `pawprint`.`Parent` (`parent_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `parent_2_id`
    FOREIGN KEY (`parent_2_id`)
    REFERENCES `pawprint`.`Parent` (`parent_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `breeder_id`
    FOREIGN KEY (`breeder_id`)
    REFERENCES `pawprint`.`Breeder` (`breeder_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `breed_litter_id`
    FOREIGN KEY (`breed_id`)
    REFERENCES `pawprint`.`Breed` (`breed_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`Listing` (
  `listing_id` INT NOT NULL AUTO_INCREMENT,
  `litter_id` INT NOT NULL,
  `date_posted` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_closed` DATETIME NOT NULL,
  `title` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`listing_id`),
  INDEX `litter_id_idx` (`litter_id` ASC),
  CONSTRAINT `litter_id`
    FOREIGN KEY (`litter_id`)
    REFERENCES `pawprint`.`Litter` (`litter_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`User` (
  `user_id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `phone_number` VARCHAR(12) NULL,
  `email` VARCHAR(64) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  `location_id` INT(11) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `pawprint`.`Pet` (
  `pet_id` INT(11) NOT NULL AUTO_INCREMENT,
  `colour` VARCHAR(32) NOT NULL,
  `weight` FLOAT NOT NULL,
  `price` FLOAT NOT NULL,
  `sex_m` TINYINT(1) NOT NULL,
  `date_adopted` DATETIME NULL,
  `litter_id` INT(11) NOT NULL,
  `adopter_id` INT(11) NULL,
  PRIMARY KEY (`pet_id`),
  INDEX `litter_id_idx` (`litter_id` ASC),
  INDEX `breeder_id_idx` (`adopter_id` ASC),
  CONSTRAINT `pet_litter_id`
    FOREIGN KEY (`litter_id`)
    REFERENCES `pawprint`.`Litter` (`litter_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `breeder_pet_id`
    FOREIGN KEY (`adopter_id`)
    REFERENCES `pawprint`.`User` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;