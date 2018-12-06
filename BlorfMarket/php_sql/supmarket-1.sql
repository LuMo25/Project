SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS `recepices` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `billing_address` varchar(100) NOT NULL,
  `delivery_address` varchar(100) NOT NULL,
  `articles` varchar(500) NOT NULL,
  `price` double NOT NULL,
  `customer` int(11) NOT NULL,
  `currency` varchar(5) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=31 ;

INSERT INTO `recepices` (`id`, `billing_address`, `delivery_address`, `articles`, `price`, `customer`, `currency`, `status`) VALUES
(26, '4 rue des abricots', '4 rue des abricots', '||BH921S00M-M11', 20.99, 7, 'GBP', 'pending'),
(27, '45 allée des prunes', '45 allée des prunes', '||PE381A02N-J11', 7.99, 8, 'GBP', 'pending'),
(28, '24 avenue du commerce', '24 avenue du commerce', '||DC122S00S-C11', 35.99, 9, 'GBP', 'pending'),
(29, 'AZERT', 'YUIOP', '||BH921S00M-M11', 20.99, 10, 'GBP', 'pending'),
(30, '4 rue des abricots', '4 rue des abricots', '||BH921S00M-M11||PE381A02N-J11', 28.98, 7, 'GBP', 'pending');


CREATE TABLE IF NOT EXISTS `users` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` text NOT NULL,
  `billing_address` varchar(100) NOT NULL,
  `delivery_address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;


INSERT INTO `users` (`id`, `email`, `login`, `password`, `role`, `billing_address`, `delivery_address`) VALUES
(6, 'webmaster@tms.com', 'webmaster', 'admin', 'admin', 'none', 'none'),
(7, 'client@example.com', 'client', 'test', 'guest', '4 rue des abricots', '4 rue des abricots'),
(8, 'client2@example.com', 'client2', 'test', 'guest', '45 allée des prunes', '45 allée des prunes'),
(9, 'client3@example.com', 'client3', 'test', 'guest', '24 avenue du commerce', '24 avenue du commerce'),
(10, 'client4@ex.com', 'client4', 'test', 'guest', 'AZERT', 'YUIOP');
