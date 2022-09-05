-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema project_app
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project_app` DEFAULT CHARACTER SET utf8 ;
USE `project_app` ;

-- -----------------------------------------------------
-- Table `project_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_app`.`users` (
  `users_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `users_password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`users_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_app`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_app`.`posts` (
  `posts_id` INT NOT NULL AUTO_INCREMENT,
  `posts_content` VARCHAR(3000) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `user_id` INT NOT NULL,
  `post_likes` INT NULL DEFAULT 0,
  PRIMARY KEY (`posts_id`),
  INDEX `fk_posts_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_app`.`users` (`users_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_app`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_app`.`comments` (
  `comments_id` INT NOT NULL AUTO_INCREMENT,
  `comments_content` VARCHAR(3000) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `post_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`comments_id`),
  INDEX `fk_comments_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `project_app`.`posts` (`posts_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_app`.`users` (`users_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_app`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_app`.`likes` (
  `likes_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `likes` INT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`likes_id`),
  INDEX `fk_likes_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_likes_posts1_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_app`.`users` (`users_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `project_app`.`posts` (`posts_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


select * from posts;

drop table posts;

select likes.user_id, likes.post_id, users.first_name, users.last_name, users.users_id
from likes left join posts on posts.posts_id = likes.post_id left join users on users.users_id = likes.user_id
where post_id = 4 AND posts_id = 4 AND users.users_id = likes.user_id;

SELECT DISTINCT likes.user_id, likes.post_id, users.first_name, users.last_name, users.users_id
from likes left join posts on posts.posts_id = likes.post_id left join users on users.users_id = likes.user_id
where post_id = 3 AND posts_id = 3 AND users.users_id = likes.user_id;

SELECT posts.posts_content, users.first_name, users.last_name, posts.user_id, posts.posts_id, users.users_id, posts.post_likes
FROM users LEFT JOIN posts ON users.users_id = posts.user_id
WHERE posts_id > 0
ORDER BY post_likes DESC;

SELECT * FROM users LEFT JOIN posts on users.users_id = posts.user_id LEFT JOIN likes ON users.users_id = likes.user_id;
delete
from posts
where posts_id < 6;

SELECT * FROM posts LEFT JOIN users on users.users_id = posts.user_id LEFT JOIN likes ON posts.posts_id = likes.post_id WHERE posts_id = 4;

select * from users; 