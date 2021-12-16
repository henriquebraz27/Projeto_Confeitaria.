-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Tempo de geração: 16-Dez-2021 às 03:09
-- Versão do servidor: 8.0.27
-- versão do PHP: 7.4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `confeitaria`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `carrinho`
--

CREATE TABLE `carrinho` (
  `idcompra` int NOT NULL,
  `data` varchar(55) DEFAULT NULL,
  `valortotal` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

CREATE TABLE `produtos` (
  `id` int NOT NULL,
  `nome` varchar(55) DEFAULT NULL,
  `descricao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `imagem` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `valor` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`id`, `nome`, `descricao`, `imagem`, `valor`) VALUES
(1, 'Cupcake de Chocolate', 'Feito com muito amor e uma massa fofinha para você se deliciar com nosso cupcake de chocolate.', 'https://cdn.pixabay.com/photo/2016/01/11/07/18/cupcakes-1133146_1280.jpg', '10'),
(2, 'Bolo de Chocolate c/ Ninho', 'Nosso bolo de chocolate com leite ninho, feito com muito amor, perfeito para encomendar para sua festa de aniversário.', 'https://cdn.pixabay.com/photo/2016/02/29/00/19/cake-1227842__480.jpg', '40'),
(3, 'Brigadeiro Goumert', 'Sua festa de aniversário nunca mais será a mesma, o docinho da tarde perfeito.', 'https://cdn.pixabay.com/photo/2018/03/25/22/35/food-3261027__480.jpg', '6'),
(4, 'Chocotone', 'Massa úmida, perfumada, muito chocolate: esse é o chocotone dos sonhos feito com os melhores ingredientes.', 'https://media.istockphoto.com/photos/chocolate-panettone-cake-for-christmas-traditional-italian-christmas-picture-id1288495342?b=1&k=20&m=1288495342&s=170667a&w=0&h=Y2p5UCxBsgcBAFhvMo0emqNQ0L4n5Vw5UajHLOX2oF4=', '80'),
(5, 'Cone de brigadeiro', 'Cone de Chocolate com Avelã. Uma receita de “chocone”, deliciosa e ótimo custo benefício.', 'https://media.istockphoto.com/photos/ice-cream-cone-stuffed-with-dulce-de-leche-chocolate-brigadeiro-picture-id1218473142?b=1&k=20&m=1218473142&s=170667a&w=0&h=TRPp2anQvZzBDDFpbDS-d26mnivpv42Oq4xefioV4U0=', '8'),
(6, 'Torta de frango', 'Quem não gosta de uma deliciosa torta de frango?\r\nMassa fofinha, frango temperadinho e perfeito para seu lanche da tarde.', 'https://cdn.pixabay.com/photo/2018/03/16/18/25/cake-salty-3232107_1280.jpg', '55');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `nome` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `senha` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `email`, `senha`) VALUES
(1, 'agner', 'agner_esteves@hotmail.com', 'agner'),
(2, 'agner', 'agner_esteves@hotmail.com', '123'),
(3, 'agner', 'agner_esteves@hotmail.com', '123');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `carrinho`
--
ALTER TABLE `carrinho`
  ADD PRIMARY KEY (`idcompra`);

--
-- Índices para tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `carrinho`
--
ALTER TABLE `carrinho`
  MODIFY `idcompra` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
