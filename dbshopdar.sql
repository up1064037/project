-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Φιλοξενητής: localhost:3306
-- Χρόνος δημιουργίας: 10 Μάη 203 στις 19:01:38
-- Έκδοση διακομιστή: 8.0.22-0ubuntu0.20.04.3
-- Έκδοση PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `dbshopdar`
--
CREATE DATABASE IF NOT EXISTS `dbshopdar` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `dbshopdar`;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `admin`
--

CREATE TABLE `admin` (
  `id` int NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Άδειασμα δεδομένων του πίνακα `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin', '12345'),
(3, 'admin8', '12345'),
(5, 'admin10', '12345');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `categories`
--

CREATE TABLE `categories` (
  `id` int NOT NULL,
  `title` varchar(200) NOT NULL,
  `descr` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Άδειασμα δεδομένων του πίνακα `categories`
--

INSERT INTO `categories` (`id`, `title`, `descr`) VALUES
(1, 'test1', 'werew'),
(2, 'test2', 'tewer234');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `materials`
--

CREATE TABLE `materials` (
  `id` int NOT NULL,
  `mtitle` varchar(200) NOT NULL,
  `mdescr` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Άδειασμα δεδομένων του πίνακα `materials`
--

INSERT INTO `materials` (`id`, `mtitle`, `mdescr`) VALUES
(4, 'mat44', 'm1000400'),
(7, 'mat66', 'weiorupow');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `orders`
--

CREATE TABLE `orders` (
  `id` int NOT NULL,
  `ids` int NOT NULL,
  `idm` int NOT NULL,
  `qnty` float(10,2) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `products`
--

CREATE TABLE `products` (
  `id` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `descr` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Άδειασμα δεδομένων του πίνακα `products`
--

INSERT INTO `products` (`id`, `title`, `descr`) VALUES
(2, 'pr1', 'pppp1'),
(3, 'p2', 'wrewer');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `prod_cat`
--

CREATE TABLE `prod_cat` (
  `id` int NOT NULL,
  `idc` int NOT NULL,
  `idp` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `prod_mat`
--

CREATE TABLE `prod_mat` (
  `id` int NOT NULL,
  `idp` int NOT NULL,
  `idm` int NOT NULL,
  `quant` float(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Άδειασμα δεδομένων του πίνακα `prod_mat`
--

INSERT INTO `prod_mat` (`id`, `idp`, `idm`, `quant`) VALUES
(4, 2, 4, 2.00),
(5, 2, 7, 2.00),
(12, 3, 4, 3.00),
(13, 3, 7, 6.00);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `sales`
--

CREATE TABLE `sales` (
  `id` int NOT NULL,
  `idp` int NOT NULL,
  `qnt` int NOT NULL,
  `dates` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `supplier`
--

CREATE TABLE `supplier` (
  `id` int NOT NULL,
  `fullname` varchar(400) NOT NULL,
  `phone` varchar(40) NOT NULL,
  `addr` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Ευρετήρια για πίνακα `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Ευρετήρια για πίνακα `materials`
--
ALTER TABLE `materials`
  ADD PRIMARY KEY (`id`);

--
-- Ευρετήρια για πίνακα `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idm` (`idm`),
  ADD KEY `ids` (`ids`);

--
-- Ευρετήρια για πίνακα `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Ευρετήρια για πίνακα `prod_cat`
--
ALTER TABLE `prod_cat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idp` (`idp`),
  ADD KEY `idc` (`idc`);

--
-- Ευρετήρια για πίνακα `prod_mat`
--
ALTER TABLE `prod_mat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idp` (`idp`,`idm`),
  ADD KEY `prod_mat_ibfk_1` (`idm`);

--
-- Ευρετήρια για πίνακα `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idp` (`idp`);

--
-- Ευρετήρια για πίνακα `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT για άχρηστους πίνακες
--

--
-- AUTO_INCREMENT για πίνακα `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT για πίνακα `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT για πίνακα `materials`
--
ALTER TABLE `materials`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT για πίνακα `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `products`
--
ALTER TABLE `products`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT για πίνακα `prod_cat`
--
ALTER TABLE `prod_cat`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `prod_mat`
--
ALTER TABLE `prod_mat`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT για πίνακα `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT για πίνακα `supplier`
--
ALTER TABLE `supplier`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Περιορισμοί για άχρηστους πίνακες
--

--
-- Περιορισμοί για πίνακα `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`idm`) REFERENCES `materials` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`ids`) REFERENCES `supplier` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Περιορισμοί για πίνακα `prod_cat`
--
ALTER TABLE `prod_cat`
  ADD CONSTRAINT `prod_cat_ibfk_1` FOREIGN KEY (`idp`) REFERENCES `products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `prod_cat_ibfk_2` FOREIGN KEY (`idc`) REFERENCES `categories` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Περιορισμοί για πίνακα `prod_mat`
--
ALTER TABLE `prod_mat`
  ADD CONSTRAINT `prod_mat_ibfk_1` FOREIGN KEY (`idm`) REFERENCES `materials` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `prod_mat_ibfk_2` FOREIGN KEY (`idp`) REFERENCES `products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Περιορισμοί για πίνακα `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`idp`) REFERENCES `products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
