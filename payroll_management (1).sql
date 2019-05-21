-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2019 at 07:32 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `payroll_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `Emp_id` int(11) NOT NULL,
  `Emp_name` varchar(30) NOT NULL,
  `Basic_salary` float NOT NULL,
  `DA` float NOT NULL,
  `Leave_Taken` int(11) NOT NULL,
  `HRA` float NOT NULL,
  `MA` float NOT NULL,
  `PA` float NOT NULL,
  `Gross_salary` float NOT NULL,
  `Tax` float NOT NULL,
  `Ecp` int(11) NOT NULL,
  `Net_salary` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`Emp_id`, `Emp_name`, `Basic_salary`, `DA`, `Leave_Taken`, `HRA`, `MA`, `PA`, `Gross_salary`, `Tax`, `Ecp`, `Net_salary`) VALUES
(2, 'Sonu', 20000, 26000, 0, 4000, 2000, 500, 52500, 5250, 0, 47250),
(3, 'Ravish', 25000, 33000, 0, 5000, 2500, 500, 66000, 6600, 0, 59400),
(4, 'Rishav', 20000, 26400, 0, 4000, 2000, 500, 52900, 5290, 0, 47610),
(5, 'sourabh', 21000, 27720, 0, 4200, 2100, 500, 55520, 5552, 0, 49968),
(6, 'Rahul', 23000, 30360, 0, 4600, 2300, 500, 60760, 6076, 0, 54684),
(7, 'Sonu kumar', 250000, 330000, 0, 50000, 25000, 500, 655500, 65550, 0, 589950),
(8, 'Rohan', 10000, 13200, 0, 2000, 1000, 500, 26700, 2670, 0, 24030),
(9, 'asasds', 12334, 16280.9, 0, 2466.8, 1233.4, 500, 32815.1, 3281.51, 0, 29533.6),
(10, 'werw', 34563, 45623.2, 0, 6912.6, 3456.3, 500, 91055.1, 9105.51, 0, 81949.6),
(11, 'werw', 34563, 45623.2, 0, 6912.6, 3456.3, 500, 91055.1, 9105.51, 0, 81949.6),
(12, 'Parbhat', 30000, 39600, 0, 6000, 3000, 500, 79100, 7910, 0, 71190),
(13, 'Saurabh', 14000, 18480, 0, 2800, 1400, 500, 37180, 3718, 0, 33462),
(14, 'Sonu', 13000, 17160, 0, 2600, 1300, 500, 34560, 3456, 0, 31104),
(15, 'Sonu', 19333.3, 25520, 16, 3866.67, 1933.33, 500, 51153.3, 5115.33, 6138, 39899.6),
(16, 'Rishav', 18900, 24948, 18, 3780, 1890, 500, 50018, 5001.8, 6002, 39014),
(17, 'Rishav', 21000, 27720, 15, 4200, 2100, 500, 55520, 5552, 6662, 43305.6),
(18, 'sonu', 8333.33, 11000, 20, 1666.67, 833.333, 500, 22333.3, 2233.33, 2680, 17420),
(19, 'akhilesh', 50000, 66000, 30, 10000, 5000, 500, 131500, 13150, 15780, 102570),
(20, 'akhil', 10000, 12760, 16, 1933.33, 966.667, 500, 25826.7, 2582.67, 3099, 20144.8),
(21, 'Ram', 15000, 19140, 16, 2900, 1450, 500, 38490, 3849, 4619, 30022.2),
(22, 'ravish', 15000, 19140, 16, 2900, 1450, 500, 38490, 3849, 4619, 30022.2),
(23, 'ram', 10000, 13200, 4, 2000, 1000, 500, 26700, 2670, 3204, 20826);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`Emp_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `Emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
