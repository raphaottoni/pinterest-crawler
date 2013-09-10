SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `pinterestTwitter` DEFAULT CHARACTER SET utf8mb4 ;
USE `pinterestTwitter` ;

-- -----------------------------------------------------
-- Table `pinterestTwitter`.`boards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`boards` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(5000) NULL DEFAULT NULL,
  `category` VARCHAR(45) NULL DEFAULT NULL,
  `nFollowers` INT(11) NULL DEFAULT NULL,
  `nPins` INT(11) NULL DEFAULT NULL,
  `shared` TINYINT(1) NULL DEFAULT '0',
  `nshared` INT(11) NULL DEFAULT '0',
  `keyName` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nameChave` (`keyName` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 21978617
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pinterestID` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(45) NULL DEFAULT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(500) NULL DEFAULT NULL,
  `nFollowers` INT(11) NULL DEFAULT NULL,
  `nFollowing` INT(11) NULL DEFAULT NULL,
  `nBoards` INT(11) NULL DEFAULT NULL,
  `nPins` INT(11) NULL DEFAULT NULL,
  `nLikes` INT(11) NULL DEFAULT NULL,
  `nCategories` INT(11) NULL DEFAULT NULL,
  `nDomains` INT(11) NULL DEFAULT NULL,
  `popularity` FLOAT NULL DEFAULT NULL,
  `influence` FLOAT NULL DEFAULT NULL,
  `entropy` FLOAT NULL DEFAULT '-1',
  `entropyDomain` FLOAT NULL DEFAULT NULL,
  `followback` FLOAT NULL DEFAULT NULL,
  `mainCategory` VARCHAR(45) NULL DEFAULT NULL,
  `mainDomain` VARCHAR(100) NULL DEFAULT NULL,
  `facebook` VARCHAR(100) NULL DEFAULT NULL,
  `location` VARCHAR(50) NULL DEFAULT NULL,
  `twitter` VARCHAR(100) NULL DEFAULT NULL,
  `website` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `pinterestID_UNIQUE` (`pinterestID` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 2378852
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`pins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`pins` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nLikes` INT(11) NULL DEFAULT NULL,
  `nRepins` INT(11) NULL DEFAULT NULL,
  `nComments` INT(11) NULL DEFAULT NULL,
  `facebookLikes` INT(11) NULL DEFAULT NULL,
  `date` DATETIME NULL DEFAULT NULL,
  `category` VARCHAR(45) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `originalUser` VARCHAR(45) NULL DEFAULT NULL,
  `domain` VARCHAR(100) NULL DEFAULT NULL,
  `pinterestURL` VARCHAR(100) NULL DEFAULT NULL,
  `imageUrl` VARCHAR(100) NULL DEFAULT NULL,
  `outsideURL` VARCHAR(5000) NULL DEFAULT NULL,
  `via` VARCHAR(45) NULL DEFAULT NULL,
  `exif` BLOB NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  `board_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `pinterestURL_UNIQUE` (`pinterestURL` ASC),
  INDEX `fk_pins_user_idx` (`user_id` ASC),
  INDEX `fk_pins_albuns1_idx` (`board_id` ASC),
  CONSTRAINT `fk_pins_albuns1`
    FOREIGN KEY (`board_id`)
    REFERENCES `pinterestTwitter`.`boards` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pins_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `pinterestTwitter`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 255315357
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pin_id` INT(11) NOT NULL,
  `pinterestID` VARCHAR(45) NOT NULL DEFAULT '',
  `comment` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `pinterestID` (`pinterestID` ASC, `comment`(255) ASC),
  INDEX `fk_comments_pins1_idx` (`pin_id` ASC),
  CONSTRAINT `fk_comments_pins1`
    FOREIGN KEY (`pin_id`)
    REFERENCES `pinterestTwitter`.`pins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`likes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `originalUser` VARCHAR(45) NULL DEFAULT NULL,
  `nLikes` INT(11) NULL DEFAULT NULL,
  `nRepins` INT(11) NULL DEFAULT NULL,
  `description` VARCHAR(500) NULL DEFAULT NULL,
  `pinterestURL` VARCHAR(100) NULL DEFAULT NULL,
  `domain` VARCHAR(100) NULL DEFAULT NULL,
  `outsideURL` VARCHAR(100) NULL DEFAULT NULL,
  `date` DATETIME NULL DEFAULT NULL,
  `category` VARCHAR(45) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `pinterestURL` (`pinterestURL` ASC),
  INDEX `fk_likes_user1_idx` (`user_id` ASC),
  CONSTRAINT `fk_likes_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `pinterestTwitter`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`liwcPins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`liwcPins` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pin_id` INT(11) NOT NULL,
  `user_id` INT(11) NULL DEFAULT NULL,
  `total_words` SMALLINT(5) UNSIGNED NULL DEFAULT '0',
  `matched_words` SMALLINT(5) UNSIGNED NULL DEFAULT '0',
  `funct` SMALLINT(6) NULL DEFAULT '0',
  `pronoun` SMALLINT(6) NULL DEFAULT '0',
  `ppron` SMALLINT(6) NULL DEFAULT '0',
  `i` SMALLINT(6) NULL DEFAULT '0',
  `we` SMALLINT(6) NULL DEFAULT '0',
  `you` SMALLINT(6) NULL DEFAULT '0',
  `shehe` SMALLINT(6) NULL DEFAULT '0',
  `they` SMALLINT(6) NULL DEFAULT '0',
  `ipron` SMALLINT(6) NULL DEFAULT '0',
  `article` SMALLINT(6) NULL DEFAULT '0',
  `verb` SMALLINT(6) NULL DEFAULT '0',
  `auxverb` SMALLINT(6) NULL DEFAULT '0',
  `past` SMALLINT(6) NULL DEFAULT '0',
  `present` SMALLINT(6) NULL DEFAULT '0',
  `future` SMALLINT(6) NULL DEFAULT '0',
  `adverb` SMALLINT(6) NULL DEFAULT '0',
  `preps` SMALLINT(6) NULL DEFAULT '0',
  `conj` SMALLINT(6) NULL DEFAULT '0',
  `negate` SMALLINT(6) NULL DEFAULT '0',
  `quant` SMALLINT(6) NULL DEFAULT '0',
  `number` SMALLINT(6) NULL DEFAULT '0',
  `swear` SMALLINT(6) NULL DEFAULT '0',
  `social` SMALLINT(6) NULL DEFAULT '0',
  `family` SMALLINT(6) NULL DEFAULT '0',
  `friend` SMALLINT(6) NULL DEFAULT '0',
  `humans` SMALLINT(6) NULL DEFAULT '0',
  `affect` SMALLINT(6) NULL DEFAULT '0',
  `posemo` SMALLINT(6) NULL DEFAULT '0',
  `negemo` SMALLINT(6) NULL DEFAULT '0',
  `anx` SMALLINT(6) NULL DEFAULT '0',
  `anger` SMALLINT(6) NULL DEFAULT '0',
  `sad` SMALLINT(6) NULL DEFAULT '0',
  `cogmech` SMALLINT(6) NULL DEFAULT '0',
  `insight` SMALLINT(6) NULL DEFAULT '0',
  `cause` SMALLINT(6) NULL DEFAULT '0',
  `discrep` SMALLINT(6) NULL DEFAULT '0',
  `tentat` SMALLINT(6) NULL DEFAULT '0',
  `certain` SMALLINT(6) NULL DEFAULT '0',
  `inhib` SMALLINT(6) NULL DEFAULT '0',
  `incl` SMALLINT(6) NULL DEFAULT '0',
  `excl` SMALLINT(6) NULL DEFAULT '0',
  `percept` SMALLINT(6) NULL DEFAULT '0',
  `see` SMALLINT(6) NULL DEFAULT '0',
  `hear` SMALLINT(6) NULL DEFAULT '0',
  `feel` SMALLINT(6) NULL DEFAULT '0',
  `bio` SMALLINT(6) NULL DEFAULT '0',
  `body` SMALLINT(6) NULL DEFAULT '0',
  `health` SMALLINT(6) NULL DEFAULT '0',
  `sexual` SMALLINT(6) NULL DEFAULT '0',
  `ingest` SMALLINT(6) NULL DEFAULT '0',
  `relativ` SMALLINT(6) NULL DEFAULT '0',
  `motion` SMALLINT(6) NULL DEFAULT '0',
  `space` SMALLINT(6) NULL DEFAULT '0',
  `time` SMALLINT(6) NULL DEFAULT '0',
  `work` SMALLINT(6) NULL DEFAULT '0',
  `achieve` SMALLINT(6) NULL DEFAULT '0',
  `leisure` SMALLINT(6) NULL DEFAULT '0',
  `home` SMALLINT(6) NULL DEFAULT '0',
  `money` SMALLINT(6) NULL DEFAULT '0',
  `relig` SMALLINT(6) NULL DEFAULT '0',
  `death` SMALLINT(6) NULL DEFAULT '0',
  `assent` SMALLINT(6) NULL DEFAULT '0',
  `nonfl` SMALLINT(6) NULL DEFAULT '0',
  `filler` SMALLINT(6) NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `unique_pins_id` (`pin_id` ASC),
  CONSTRAINT `fk_pins_id`
    FOREIGN KEY (`pin_id`)
    REFERENCES `pinterestTwitter`.`pins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 26022289
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`sharing`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`sharing` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `owner` TINYINT(1) NULL DEFAULT '0',
  `user_id` INT(11) NOT NULL,
  `board_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id_2` (`user_id` ASC, `board_id` ASC),
  INDEX `fk_compartilhamentos_user1_idx` (`user_id` ASC),
  INDEX `fk_compartilhamentos_albuns1_idx` (`board_id` ASC),
  INDEX `user_id` (`user_id` ASC, `board_id` ASC),
  CONSTRAINT `fk_compartilhamentos_albuns1`
    FOREIGN KEY (`board_id`)
    REFERENCES `pinterestTwitter`.`boards` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_compartilhamentos_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `pinterestTwitter`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 21955065
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`twitterInfo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`twitterInfo` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `twitterUserID` VARCHAR(45) NULL DEFAULT NULL,
  `name` VARCHAR(24) NULL DEFAULT NULL,
  `description` VARCHAR(200) NULL DEFAULT NULL,
  `language` VARCHAR(12) NULL DEFAULT NULL,
  `location` VARCHAR(64) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `nTweets` INT(11) NULL DEFAULT NULL,
  `nFollowers` INT(11) NULL DEFAULT NULL,
  `nFollowing` VARCHAR(45) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `twitterUserID_UNIQUE` (`twitterUserID` ASC),
  INDEX `fk_twitterInfo_users2_idx` (`user_id` ASC),
  CONSTRAINT `fk_twitterInfo_users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `pinterestTwitter`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`tweets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`tweets` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `twitterID` BIGINT(20) NULL DEFAULT NULL,
  `date` DATETIME NULL DEFAULT NULL,
  `content` VARCHAR(150) NULL DEFAULT NULL,
  `retweetCount` INT(11) NULL DEFAULT NULL,
  `favoriteCount` INT(11) NULL DEFAULT NULL,
  `isRetweet` TINYINT(4) NULL DEFAULT NULL,
  `isReply` TINYINT(4) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  `twitterInfo_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tweets_users2_idx` (`user_id` ASC),
  INDEX `fk_tweets_twitterInfo2_idx` (`twitterInfo_id` ASC),
  CONSTRAINT `fk_tweets_users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `pinterestTwitter`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tweets_twitterInfo2`
    FOREIGN KEY (`twitterInfo_id`)
    REFERENCES `pinterestTwitter`.`twitterInfo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`twitterCollector`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`twitterCollector` (
  `user_id` INT(11) NOT NULL,
  `twitter` VARCHAR(100) NULL DEFAULT NULL,
  `status` ENUM('AVAILABLE','PROCESSING','COMPLETE','ERROR') NOT NULL DEFAULT 'AVAILABLE',
  `thread_id` VARCHAR(32) NULL DEFAULT NULL,
  `updated_at` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE INDEX `userid_UNIQUE` (`user_id` ASC),
  INDEX `status_INDEX` (`status` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pinterestTwitter`.`usersToCollect`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pinterestTwitter`.`usersToCollect` (
  `pinterestID` VARCHAR(45) NOT NULL,
  `statusColeta` SMALLINT(6) NOT NULL DEFAULT '0',
  `crawler` VARCHAR(45) NULL DEFAULT NULL,
  `qtd` SMALLINT(6) NOT NULL DEFAULT '0',
  `updated_at` TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`pinterestID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
