USE mysqldb;

CREATE TABLE IF NOT EXISTS `mysqldb`.`tarefa` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `titulo` VARCHAR(50) NOT NULL,
  `data` DATE NOT NULL,
  `status` ENUM('p', 'e', 'c') NOT NULL DEFAULT 'p',
  `descricao` TEXT NOT NULL
);

GRANT ALL PRIVILEGES ON `mysql`.* TO 'back_user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
