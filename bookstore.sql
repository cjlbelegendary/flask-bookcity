-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2024-12-21 20:14:52
-- 服务器版本： 5.7.26
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `bookstore`
--

-- --------------------------------------------------------

--
-- 表的结构 `books`
--

CREATE TABLE `books` (
  `ID` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `图片` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `书名` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `作者` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `出版社` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `价格` float DEFAULT NULL,
  `数量` int(11) DEFAULT NULL,
  `位置` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `简介` varchar(600) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `books`
--

INSERT INTO `books` (`ID`, `图片`, `书名`, `作者`, `出版社`, `价格`, `数量`, `位置`, `简介`) VALUES
('4', 'https://img3m1.ddimg.cn/6/9/21055821-5_u_1703840299.jpg', '我与地坛', '史铁生', '人民文学出版社', 40, 20, '一楼C区1号书架', '我是简介'),
('11', '1', '1', '1', '1', 1, 12131, '1', '13'),
('12', '1', '1', '2', '2', 2, 2, '2', '3'),
('13', '121', '212', '121', '1212', 1212, 121, '21', '12'),
('6', 'https://www.xduph.com/pages/ShowPic.aspx?path=%5cbook%5c1e9958a3-a47f-4c02-bad1-3189e412e92b%5c1e9958a3-a47f-4c02-bad1-3189e412e92b.jpg&ptype=1%20&vpath=1', '人工智能应用素养', '何淼　顾海花　杜璐', '西安电子科技大学出版社', 59, 44, '二楼D区3号书架', '本书立足服务国家智能制造产业升级的需求，阐述了人工智能的基本概念、术语以及行业的发展态势和生态环境，详细介绍了人工智能在电子信息工程、网络通信、智能制造、数字商务、数字艺术和智能交通这六大常见工业生产领域的交叉应用和实践案例，旨在通过这本具有通识性的教材，推动人工智能技术在不同领域的交叉应用，同时普及跨领域的人工智能知识。本书不仅适用于高校师生，也适合智能产品的设计与运维人员、行业智能化方案的制定与推广人员、智能化产品销售人员参考使用。同时，本书还可以作为社会公众了解人工智能技术的通识读物，帮助大家打开通往人工智能的大门。'),
('7', 'https://img.rednet.cn/2020/09-11/7b517603-72ef-4c18-a463-e8f8b60e6f24.jpeg', '蛤蟆先生去看心理医生', '罗伯特·戴博德', '天津人民出版社', 38, 30, '一楼C区3号书架', '为了向大众读者普及心理学知识，告诉大家心理咨询是怎么一回事，作者借用了英国文学经典《柳林风声》的故事主角，让蛤蟆先生和他的朋友们再次登场，演绎了这个关于心理咨询的故事。读者犹如亲临现场，体验心理咨询的每一个细节，见证疗愈和改变的发生。'),
('10', 'https://img3m6.ddimg.cn/87/11/29490306-1_w_8.jpg', '第七天', '余华', '新星出版社', 49, 40, '一楼C区1号书架', '一个叫杨飞的人死去了，但他的灵魂似乎还没走远，他接到一通电话，殡仪馆的人抱怨他火化迟到，而即将被火化的正是杨飞自己。 他在去殡仪馆的路上经历了一系列真实而荒诞的事件，以及与生前亲友的爱恨离别，也慢慢解开了自己的身世之谜……  “走过去吧，那里树叶会向你招手，石头会向你微笑，河水会向你问候。那里没有贫贱也没有富贵，没有悲伤也没有疼痛，没有仇也没有恨。”'),
('9', 'https://img3m3.ddimg.cn/23/25/29311943-1_w_34.jpg', '活着', '余华', '北京十月文艺出版社', 45, 30, '一楼C区1号书架', '《活着》是当代作家余华的代表作，讲述了一个人历尽世间沧桑和磨难的一生，亦将中国大半个世纪的社会变迁凝缩其间。《活着》还讲述了眼泪的宽广和丰富；讲述了绝望的不存在；讲述了人是为了活着本身而活着的，而不是为了活着之外的任何事物而活着。');

-- --------------------------------------------------------

--
-- 表的结构 `users`
--

CREATE TABLE `users` (
  `username` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `users`
--

INSERT INTO `users` (`username`, `password`, `type`) VALUES
('admin', '123', 'admin');

--
-- 转储表的索引
--

--
-- 表的索引 `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`ID`);

--
-- 表的索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
