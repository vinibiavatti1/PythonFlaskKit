CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `password_hash` VARCHAR(255) NOT NULL,
    `role` VARCHAR(255) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    `active` BOOLEAN NOT NULL DEFAULT TRUE,
    `last_login` DATETIME NULL,
    `hash` VARCHAR(255) NULL,
    `email_verified` BOOLEAN NOT NULL DEFAULT FALSE
);
