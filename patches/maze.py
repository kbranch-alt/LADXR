from roomEditor import RoomEditor
from assembler import ASM
import random
import utils

ALL_SIGN_OPTION_TILES = [
(101, 1), (102, 1), (106, 1), (107, 1), (108, 1), (111, 1), (74, 2), (75, 2),
(76, 2), (77, 2), (78, 2), (81, 2), (82, 2), (88, 2), (91, 2), (92, 2),
(101, 2), (102, 2), (103, 2), (105, 2), (106, 2), (107, 2), (108, 2), (111, 2),
(112, 2), (113, 2), (114, 2), (121, 2), (128, 3), (43, 4), (44, 4), (46, 4),
(47, 4), (48, 4), (52, 4), (126, 4), (137, 4), (148, 4), (151, 4), (152, 4),
(156, 4), (157, 4), (3, 5), (6, 5), (18, 5), (21, 5), (22, 5), (24, 5),
(44, 5), (47, 5), (48, 5), (52, 5), (53, 5), (56, 5), (74, 5), (95, 5),
(96, 5), (97, 5), (117, 5), (118, 5), (121, 5), (122, 5), (123, 5), (143, 5),
(144, 5), (146, 5), (147, 5), (148, 5), (151, 5), (153, 5), (26, 6), (27, 6),
(81, 6), (95, 6), (96, 6), (97, 6), (103, 6), (105, 6), (111, 6), (112, 6),
(113, 6), (114, 6), (115, 6), (4, 9), (6, 9), (11, 9), (12, 9), (13, 9),
(14, 9), (18, 9), (21, 9), (22, 9), (24, 9), (25, 9), (26, 9), (27, 9),
(28, 9), (85, 9), (91, 9), (92, 9), (95, 9), (118, 9), (134, 9), (3, 10),
(4, 10), (5, 10), (6, 10), (7, 10), (11, 10), (12, 10), (13, 10), (14, 10),
(21, 10), (22, 10), (23, 10), (24, 10), (26, 10), (27, 10), (28, 10), (85, 10),
(86, 10), (91, 10), (92, 10), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11),
(7, 11), (14, 11), (75, 11), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12),
(8, 12), (57, 12), (101, 12), (131, 12), (156, 12), (61, 13), (62, 13), (63, 13),
(66, 13), (67, 13), (68, 13), (105, 13), (106, 13), (107, 13), (108, 13), (58, 17),
(73, 17), (74, 17), (76, 17), (77, 17), (82, 17), (83, 17), (3, 18), (4, 18),
(16, 18), (17, 18), (18, 18), (21, 18), (22, 18), (23, 18), (24, 18), (26, 18),
(27, 18), (28, 18), (31, 18), (32, 18), (36, 18), (58, 18), (78, 18), (82, 18),
(83, 18), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (12, 19), (17, 19),
(18, 19), (22, 19), (23, 19), (24, 19), (27, 19), (36, 19), (43, 19), (45, 19),
(46, 19), (78, 19), (82, 19), (3, 20), (6, 20), (8, 20), (13, 20), (14, 20),
(15, 20), (16, 20), (18, 20), (22, 20), (23, 20), (24, 20), (35, 20), (36, 20),
(37, 20), (42, 20), (44, 20), (45, 20), (46, 20), (78, 20), (82, 20), (83, 20),
(148, 20), (151, 20), (152, 20), (154, 20), (3, 21), (5, 21), (6, 21), (8, 21),
(14, 21), (15, 21), (18, 21), (22, 21), (24, 21), (25, 21), (26, 21), (31, 21),
(32, 21), (38, 21), (42, 21), (43, 21), (44, 21), (45, 21), (46, 21), (48, 21),
(54, 21), (63, 21), (64, 21), (71, 21), (72, 21), (73, 21), (78, 21), (82, 21),
(91, 21), (96, 21), (97, 21), (98, 21), (128, 21), (132, 21), (137, 21), (138, 21),
(153, 21), (3, 22), (4, 22), (5, 22), (6, 22), (7, 22), (8, 22), (12, 22),
(13, 22), (14, 22), (15, 22), (16, 22), (17, 22), (18, 22), (22, 22), (23, 22),
(32, 22), (38, 22), (54, 22), (55, 22), (56, 22), (57, 22), (58, 22), (61, 22),
(62, 22), (63, 22), (71, 22), (72, 22), (73, 22), (74, 22), (78, 22), (82, 22),
(83, 22), (138, 22), (141, 22), (155, 22), (3, 25), (4, 25), (5, 25), (22, 25),
(23, 25), (24, 25), (28, 25), (32, 25), (33, 25), (38, 25), (44, 25), (54, 25),
(55, 25), (56, 25), (57, 25), (58, 25), (66, 25), (67, 25), (68, 25), (87, 25),
(94, 25), (95, 25), (101, 25), (102, 25), (103, 25), (104, 25), (105, 25), (106, 25),
(107, 25), (108, 25), (111, 25), (112, 25), (113, 25), (114, 25), (115, 25), (116, 25),
(117, 25), (133, 25), (138, 25), (146, 25), (147, 25), (148, 25), (3, 26), (5, 26),
(25, 26), (31, 26), (38, 26), (67, 26), (68, 26), (71, 26), (82, 26), (88, 26),
(92, 26), (93, 26), (94, 26), (95, 26), (101, 26), (102, 26), (103, 26), (118, 26),
(121, 26), (122, 26), (123, 26), (125, 26), (126, 26), (127, 26), (131, 26), (132, 26),
(133, 26), (134, 26), (135, 26), (136, 26), (137, 26), (138, 26), (147, 26), (148, 26),
(151, 26), (1, 27), (2, 27), (3, 27), (5, 27), (22, 27), (25, 27), (26, 27),
(34, 27), (42, 27), (43, 27), (65, 27), (67, 27), (68, 27), (71, 27), (81, 27),
(82, 27), (91, 27), (92, 27), (93, 27), (94, 27), (96, 27), (97, 27), (98, 27),
(101, 27), (102, 27), (103, 27), (104, 27), (12, 28), (13, 28), (14, 28), (18, 28),
(21, 28), (22, 28), (24, 28), (25, 28), (26, 28), (27, 28), (35, 28), (36, 28),
(43, 28), (47, 28), (67, 28), (72, 28), (73, 28), (75, 28), (76, 28), (13, 29),
(14, 29), (15, 29), (31, 29), (32, 29), (37, 29), (38, 29), (54, 29), (55, 29),
(65, 29), (66, 29), (72, 29), (73, 29), (74, 29), (75, 29), (76, 29), (5, 30),
(6, 30), (7, 30), (45, 30), (63, 30), (65, 30), (112, 30), (5, 33), (6, 33),
(7, 33), (63, 33), (67, 33), (73, 33), (112, 33), (18, 34), (27, 34), (28, 34),
(31, 34), (32, 34), (33, 34), (34, 34), (35, 34), (36, 34), (47, 34), (48, 34),
(51, 34), (55, 34), (56, 34), (63, 34), (73, 34), (74, 34), (107, 34), (111, 34),
(112, 34), (113, 34), (115, 34), (34, 35), (35, 35), (36, 35), (37, 35), (47, 35),
(48, 35), (63, 35), (64, 35), (65, 35), (72, 35), (73, 35), (74, 35), (77, 35),
(87, 35), (88, 35), (98, 35), (101, 35), (102, 35), (103, 35), (104, 35), (113, 35),
(114, 35), (115, 35), (16, 36), (26, 36), (33, 36), (34, 36), (35, 36), (36, 36),
(37, 36), (38, 36), (41, 36), (47, 36), (57, 36), (76, 36), (87, 36), (102, 36),
(103, 36), (104, 36), (105, 36), (113, 36), (114, 36), (115, 36), (2, 37), (7, 37),
(8, 37), (14, 37), (15, 37), (41, 37), (47, 37), (48, 37), (57, 37), (58, 37),
(62, 37), (66, 37), (67, 37), (76, 37), (77, 37), (103, 37), (104, 37), (105, 37),
(113, 37), (114, 37), (115, 37), (3, 38), (4, 38), (14, 38), (15, 38), (16, 38),
(23, 38), (24, 38), (25, 38), (42, 38), (46, 38), (47, 38), (48, 38), (57, 38),
(58, 38), (62, 38), (75, 38), (76, 38), (77, 38), (87, 38), (103, 38), (104, 38),
(105, 38), (113, 38), (114, 38), (115, 38), (4, 41), (5, 41), (12, 41), (15, 41),
(16, 41), (23, 41), (24, 41), (25, 41), (47, 41), (48, 41), (65, 41), (75, 41),
(76, 41), (77, 41), (86, 41), (87, 41), (103, 41), (104, 41), (106, 41), (107, 41),
(108, 41), (4, 42), (5, 42), (11, 42), (16, 42), (17, 42), (23, 42), (24, 42),
(25, 42), (26, 42), (32, 42), (37, 42), (47, 42), (48, 42), (71, 42), (75, 42),
(76, 42), (77, 42), (86, 42), (87, 42), (103, 42), (104, 42), (105, 42), (106, 42),
(107, 42), (113, 42), (4, 43), (5, 43), (6, 43), (7, 43), (16, 43), (23, 43),
(24, 43), (25, 43), (26, 43), (27, 43), (48, 43), (51, 43), (67, 43), (68, 43),
(71, 43), (84, 43), (85, 43), (86, 43), (87, 43), (92, 43), (98, 43), (103, 43),
(106, 43), (107, 43), (113, 43), (5, 44), (6, 44), (7, 44), (8, 44), (16, 44),
(17, 44), (23, 44), (24, 44), (26, 44), (27, 44), (47, 44), (48, 44), (55, 44),
(56, 44), (57, 44), (62, 44), (67, 44), (72, 44), (73, 44), (74, 44), (85, 44),
(86, 44), (91, 44), (92, 44), (94, 44), (96, 44), (103, 44), (104, 44), (106, 44),
(107, 44), (108, 44), (113, 44), (5, 45), (6, 45), (7, 45), (8, 45), (12, 45),
(15, 45), (23, 45), (24, 45), (25, 45), (26, 45), (27, 45), (33, 45), (34, 45),
(35, 45), (36, 45), (47, 45), (48, 45), (53, 45), (54, 45), (55, 45), (56, 45),
(57, 45), (58, 45), (61, 45), (62, 45), (63, 45), (64, 45), (65, 45), (66, 45),
(67, 45), (68, 45), (72, 45), (73, 45), (74, 45), (85, 45), (86, 45), (91, 45),
(92, 45), (93, 45), (94, 45), (95, 45), (96, 45), (97, 45), (98, 45), (104, 45),
(105, 45), (106, 45), (108, 45), (113, 45), (14, 46), (15, 46), (16, 46), (23, 46),
(34, 46), (35, 46), (47, 46), (48, 46), (95, 46), (105, 46), (113, 46), (5, 49),
(6, 49), (7, 49), (8, 49), (11, 49), (12, 49), (13, 49), (14, 49), (15, 49),
(16, 49), (23, 49), (24, 49), (32, 49), (35, 49), (36, 49), (44, 49), (45, 49),
(46, 49), (47, 49), (48, 49), (51, 49), (52, 49), (56, 49), (74, 49), (85, 49),
(105, 49), (106, 49), (113, 49), (114, 49), (115, 49), (6, 50), (15, 50), (23, 50),
(24, 50), (31, 50), (36, 50), (37, 50), (46, 50), (47, 50), (48, 50), (71, 50),
(85, 50), (91, 50), (105, 50), (106, 50), (108, 50), (111, 50), (112, 50), (113, 50),
(114, 50), (115, 50), (6, 51), (7, 51), (15, 51), (23, 51), (24, 51), (36, 51),
(47, 51), (48, 51), (51, 51), (72, 51), (85, 51), (86, 51), (87, 51), (88, 51),
(91, 51), (101, 51), (103, 51), (104, 51), (105, 51), (106, 51), (113, 51), (114, 51),
(115, 51), (6, 52), (7, 52), (15, 52), (16, 52), (23, 52), (24, 52), (26, 52),
(28, 52), (36, 52), (37, 52), (48, 52), (51, 52), (85, 52), (86, 52), (87, 52),
(88, 52), (91, 52), (101, 52), (102, 52), (103, 52), (104, 52), (105, 52), (106, 52),
(113, 52), (6, 53), (7, 53), (15, 53), (23, 53), (24, 53), (26, 53), (27, 53),
(28, 53), (32, 53), (35, 53), (43, 53), (48, 53), (51, 53), (52, 53), (53, 53),
(55, 53), (61, 53), (62, 53), (72, 53), (85, 53), (86, 53), (87, 53), (88, 53),
(91, 53), (92, 53), (93, 53), (95, 53), (97, 53), (98, 53), (101, 53), (102, 53),
(103, 53), (104, 53), (105, 53), (106, 53), (114, 53), (4, 54), (5, 54), (6, 54),
(7, 54), (15, 54), (16, 54), (34, 54), (35, 54), (36, 54), (42, 54), (44, 54),
(63, 54), (65, 54), (67, 54), (72, 54), (73, 54), (75, 54), (77, 54), (95, 54),
(6, 57), (7, 57), (8, 57), (11, 57), (33, 57), (35, 57), (36, 57), (37, 57),
(46, 57), (48, 57), (51, 57), (52, 57), (54, 57), (55, 57), (58, 57), (63, 57),
(68, 57), (72, 57), (6, 58), (33, 58), (35, 58), (37, 58), (42, 58), (44, 58),
(45, 58), (47, 58), (48, 58), (51, 58), (58, 58), (68, 58), (71, 58), (7, 59),
(23, 59), (24, 59), (25, 59), (26, 59), (33, 59), (37, 59), (43, 59), (44, 59),
(45, 59), (47, 59), (48, 59), (51, 59), (58, 59), (63, 59), (68, 59), (71, 59),
(72, 59), (94, 59), (95, 59), (96, 59), (6, 60), (7, 60), (33, 60), (35, 60),
(36, 60), (37, 60), (43, 60), (44, 60), (45, 60), (46, 60), (47, 60), (48, 60),
(51, 60), (56, 60), (95, 60), (96, 60), (113, 60), (115, 60), (6, 61), (7, 61),
(43, 61), (44, 61), (45, 61), (46, 61), (47, 61), (48, 61), (51, 61), (52, 61),
(54, 61), (57, 61), (95, 61), (96, 61), (115, 61), (5, 62), (6, 62), (7, 62),
(57, 62), (93, 62), (94, 62), (95, 62), (96, 62), (97, 62), (114, 62), (115, 62),
(116, 62), (3, 65), (4, 65), (5, 65), (6, 65), (7, 65), (63, 65), (64, 65),
(68, 65), (71, 65), (82, 65), (83, 65), (84, 65), (85, 65), (86, 65), (87, 65),
(88, 65), (91, 65), (93, 65), (95, 65), (96, 65), (98, 65), (114, 65), (115, 65),
(116, 65), (6, 66), (7, 66), (22, 66), (23, 66), (34, 66), (36, 66), (37, 66),
(38, 66), (41, 66), (65, 66), (66, 66), (68, 66), (71, 66), (72, 66), (73, 66),
(77, 66), (81, 66), (82, 66), (88, 66), (91, 66), (93, 66), (95, 66), (107, 66),
(108, 66), (111, 66), (134, 66), (17, 67), (23, 67), (35, 67), (36, 67), (37, 67),
(42, 67), (43, 67), (44, 67), (65, 67), (67, 67), (71, 67), (72, 67), (73, 67),
(77, 67), (83, 67), (88, 67), (95, 67), (96, 67), (111, 67), (134, 67), (17, 68),
(34, 68), (35, 68), (36, 68), (37, 68), (38, 68), (42, 68), (43, 68), (58, 68),
(62, 68), (63, 68), (65, 68), (67, 68), (71, 68), (72, 68), (73, 68), (74, 68),
(76, 68), (77, 68), (78, 68), (82, 68), (83, 68), (88, 68), (92, 68), (94, 68),
(95, 68), (104, 68), (111, 68), (112, 68), (134, 68), (156, 68), (17, 69), (28, 69),
(31, 69), (37, 69), (38, 69), (42, 69), (43, 69), (44, 69), (47, 69), (62, 69),
(63, 69), (65, 69), (67, 69), (72, 69), (73, 69), (74, 69), (75, 69), (76, 69),
(86, 69), (87, 69), (88, 69), (92, 69), (94, 69), (98, 69), (105, 69), (122, 69),
(124, 69), (13, 70), (14, 70), (15, 70), (16, 70), (17, 70), (21, 70), (37, 70),
(38, 70), (42, 70), (43, 70), (44, 70), (48, 70), (51, 70), (52, 70), (53, 70),
(54, 70), (56, 70), (57, 70), (62, 70), (63, 70), (64, 70), (65, 70), (67, 70),
(68, 70), (72, 70), (73, 70), (74, 70), (75, 70), (85, 70), (102, 70), (103, 70),
(104, 70), (105, 70), (106, 70), (107, 70), (157, 70), (15, 73), (16, 73), (17, 73),
(22, 73), (23, 73), (24, 73), (25, 73), (26, 73), (28, 73), (32, 73), (36, 73),
(37, 73), (38, 73), (42, 73), (46, 73), (47, 73), (48, 73), (51, 73), (56, 73),
(57, 73), (62, 73), (64, 73), (65, 73), (66, 73), (67, 73), (73, 73), (74, 73),
(75, 73), (76, 73), (78, 73), (81, 73), (85, 73), (91, 73), (94, 73), (106, 73),
(157, 73), (5, 74), (7, 74), (15, 74), (17, 74), (18, 74), (22, 74), (27, 74),
(28, 74), (31, 74), (37, 74), (42, 74), (48, 74), (51, 74), (61, 74), (62, 74),
(64, 74), (66, 74), (73, 74), (74, 74), (75, 74), (76, 74), (85, 74), (94, 74),
(107, 74), (157, 74), (4, 75), (5, 75), (6, 75), (7, 75), (18, 75), (23, 75),
(24, 75), (27, 75), (28, 75), (31, 75), (37, 75), (38, 75), (48, 75), (51, 75),
(52, 75), (62, 75), (63, 75), (64, 75), (66, 75), (94, 75), (101, 75), (102, 75),
(103, 75), (107, 75), (108, 75), (142, 75), (153, 75), (154, 75), (7, 76), (12, 76),
(13, 76), (18, 76), (23, 76), (24, 76), (28, 76), (31, 76), (37, 76), (38, 76),
(48, 76), (51, 76), (52, 76), (53, 76), (54, 76), (62, 76), (63, 76), (64, 76),
(65, 76), (67, 76), (85, 76), (86, 76), (87, 76), (88, 76), (94, 76), (96, 76),
(98, 76), (101, 76), (102, 76), (103, 76), (104, 76), (105, 76), (107, 76), (108, 76),
(111, 76), (7, 77), (12, 77), (13, 77), (14, 77), (22, 77), (23, 77), (24, 77),
(26, 77), (28, 77), (31, 77), (37, 77), (38, 77), (46, 77), (47, 77), (48, 77),
(51, 77), (52, 77), (53, 77), (54, 77), (61, 77), (62, 77), (63, 77), (64, 77),
(65, 77), (67, 77), (68, 77), (76, 77), (83, 77), (84, 77), (85, 77), (86, 77),
(87, 77), (93, 77), (94, 77), (95, 77), (97, 77), (98, 77), (101, 77), (102, 77),
(103, 77), (105, 77), (106, 77), (108, 77), (111, 77), (147, 77), (151, 77), (152, 77),
(153, 77), (156, 77), (6, 78), (7, 78), (15, 78), (22, 78), (24, 78), (25, 78),
(26, 78), (27, 78), (28, 78), (31, 78), (32, 78), (33, 78), (35, 78), (36, 78),
(37, 78), (38, 78), (45, 78), (46, 78), (47, 78), (48, 78), (51, 78), (52, 78),
(53, 78), (54, 78), (55, 78), (94, 78), (95, 78), (96, 78), (116, 78), (117, 78),
(11, 81), (18, 81), (21, 81), (31, 81), (38, 81), (51, 81), (73, 81), (74, 81),
(77, 81), (78, 81), (81, 81), (82, 81), (83, 81), (85, 81), (88, 81), (98, 81),
(101, 81), (108, 81), (111, 81), (118, 81), (11, 82), (18, 82), (21, 82), (31, 82),
(38, 82), (51, 82), (52, 82), (61, 82), (62, 82), (73, 82), (74, 82), (75, 82),
(76, 82), (77, 82), (78, 82), (91, 82), (98, 82), (102, 82), (111, 82), (131, 82),
(144, 82), (146, 82), (2, 83), (11, 83), (18, 83), (21, 83), (31, 83), (38, 83),
(52, 83), (55, 83), (56, 83), (57, 83), (58, 83), (61, 83), (62, 83), (65, 83),
(67, 83), (73, 83), (78, 83), (81, 83), (111, 83), (132, 83), (147, 83), (11, 84),
(12, 84), (16, 84), (17, 84), (18, 84), (21, 84), (27, 84), (31, 84), (38, 84),
(42, 84), (47, 84), (52, 84), (56, 84), (57, 84), (58, 84), (61, 84), (62, 84),
(65, 84), (67, 84), (73, 84), (74, 84), (83, 84), (85, 84), (94, 84), (101, 84),
(111, 84), (122, 84), (123, 84), (124, 84), (126, 84), (127, 84), (128, 84), (132, 84),
(3, 85), (7, 85), (8, 85), (11, 85), (12, 85), (13, 85), (14, 85), (15, 85),
(16, 85), (17, 85), (21, 85), (31, 85), (38, 85), (42, 85), (43, 85), (45, 85),
(46, 85), (47, 85), (52, 85), (55, 85), (56, 85), (57, 85), (58, 85), (61, 85),
(62, 85), (65, 85), (66, 85), (67, 85), (73, 85), (74, 85), (78, 85), (85, 85),
(86, 85), (87, 85), (101, 85), (123, 85), (124, 85), (125, 85), (126, 85), (127, 85),
(128, 85), (132, 85), (147, 85), (3, 86), (12, 86), (13, 86), (14, 86), (15, 86),
(16, 86), (17, 86), (18, 86), (21, 86), (31, 86), (38, 86), (42, 86), (43, 86),
(44, 86), (45, 86), (46, 86), (47, 86), (52, 86), (73, 86), (74, 86), (78, 86),
(132, 86), (135, 86), (6, 89), (8, 89), (21, 89), (22, 89), (23, 89), (24, 89),
(25, 89), (26, 89), (27, 89), (28, 89), (31, 89), (32, 89), (42, 89), (43, 89),
(44, 89), (45, 89), (47, 89), (52, 89), (62, 89), (63, 89), (65, 89), (66, 89),
(68, 89), (71, 89), (73, 89), (74, 89), (101, 89), (118, 89), (121, 89), (127, 89),
(128, 89), (131, 89), (132, 89), (136, 89), (137, 89), (138, 89), (145, 89), (148, 89),
(156, 89), (6, 90), (7, 90), (8, 90), (21, 90), (22, 90), (28, 90), (31, 90),
(42, 90), (43, 90), (44, 90), (52, 90), (54, 90), (55, 90), (57, 90), (58, 90),
(61, 90), (62, 90), (63, 90), (74, 90), (75, 90), (93, 90), (101, 90), (122, 90),
(128, 90), (131, 90), (144, 90), (145, 90), (146, 90), (2, 91), (5, 91), (6, 91),
(12, 91), (16, 91), (21, 91), (22, 91), (23, 91), (28, 91), (31, 91), (32, 91),
(52, 91), (61, 91), (74, 91), (75, 91), (83, 91), (122, 91), (134, 91), (135, 91),
(146, 91), (156, 91), (3, 92), (5, 92), (6, 92), (11, 92), (17, 92), (18, 92),
(21, 92), (22, 92), (23, 92), (28, 92), (31, 92), (52, 92), (61, 92), (66, 92),
(67, 92), (84, 92), (117, 92), (125, 92), (135, 92), (153, 92), (3, 93), (4, 93),
(5, 93), (6, 93), (18, 93), (21, 93), (22, 93), (23, 93), (24, 93), (26, 93),
(27, 93), (28, 93), (31, 93), (46, 93), (52, 93), (53, 93), (61, 93), (63, 93),
(64, 93), (84, 93), (111, 93), (112, 93), (115, 93), (116, 93), (117, 93), (122, 93),
(124, 93), (125, 93), (126, 93), (135, 93), (138, 93), (144, 93), (145, 93), (147, 93),
(148, 93), (152, 93), (154, 93), (5, 94), (44, 94), (45, 94), (46, 94), (47, 94),
(84, 94), (94, 94), (112, 94), (113, 94), (115, 94), (116, 94), (117, 94), (118, 94),
(6, 97), (15, 97), (18, 97), (21, 97), (22, 97), (24, 97), (25, 97), (26, 97),
(27, 97), (28, 97), (31, 97), (32, 97), (33, 97), (34, 97), (35, 97), (45, 97),
(46, 97), (47, 97), (48, 97), (58, 97), (66, 97), (68, 97), (92, 97), (112, 97),
(114, 97), (115, 97), (151, 97), (152, 97), (154, 97), (156, 97), (15, 98), (22, 98),
(23, 98), (35, 98), (36, 98), (37, 98), (41, 98), (44, 98), (45, 98), (51, 98),
(114, 98), (115, 98), (154, 98), (156, 98), (157, 98), (1, 99), (2, 99), (11, 99),
(16, 99), (17, 99), (18, 99), (24, 99), (35, 99), (36, 99), (37, 99), (43, 99),
(44, 99), (45, 99), (54, 99), (84, 99), (86, 99), (87, 99), (112, 99), (113, 99),
(114, 99), (115, 99), (116, 99), (2, 100), (11, 100), (34, 100), (35, 100), (38, 100),
(45, 100), (52, 100), (54, 100), (58, 100), (85, 100), (86, 100), (87, 100), (112, 100),
(114, 100), (115, 100), (125, 100), (2, 101), (3, 101), (4, 101), (5, 101), (6, 101),
(12, 101), (13, 101), (15, 101), (27, 101), (33, 101), (34, 101), (35, 101), (37, 101),
(38, 101), (52, 101), (81, 101), (83, 101), (84, 101), (85, 101), (112, 101), (115, 101),
(123, 101), (126, 101), (131, 101), (154, 101), (155, 101), (156, 101), (12, 102), (13, 102),
(14, 102), (15, 102), (17, 102), (21, 102), (22, 102), (23, 102), (24, 102), (25, 102),
(26, 102), (42, 102), (43, 102), (44, 102), (51, 102), (52, 102), (53, 102), (57, 102),
(58, 102), (82, 102), (83, 102), (84, 102), (85, 102), (86, 102), (112, 102), (113, 102),
(114, 102), (115, 102), (116, 102), (117, 102), (122, 102), (123, 102), (124, 102), (125, 102),
(126, 102), (127, 102), (128, 102), (131, 102), (133, 102), (134, 102), (135, 102), (136, 102),
(1, 105), (2, 105), (3, 105), (4, 105), (5, 105), (6, 105), (8, 105), (18, 105),
(22, 105), (23, 105), (24, 105), (25, 105), (26, 105), (27, 105), (28, 105), (31, 105),
(32, 105), (33, 105), (43, 105), (44, 105), (46, 105), (47, 105), (48, 105), (51, 105),
(52, 105), (53, 105), (58, 105), (82, 105), (83, 105), (84, 105), (85, 105), (86, 105),
(113, 105), (114, 105), (115, 105), (116, 105), (117, 105), (122, 105), (124, 105), (125, 105),
(127, 105), (128, 105), (131, 105), (152, 105), (156, 105), (157, 105), (158, 105), (18, 106),
(22, 106), (23, 106), (24, 106), (25, 106), (26, 106), (32, 106), (46, 106), (47, 106),
(55, 106), (82, 106), (83, 106), (84, 106), (85, 106), (86, 106), (113, 106), (114, 106),
(122, 106), (124, 106), (127, 106), (128, 106), (131, 106), (145, 106), (148, 106), (151, 106),
(152, 106), (153, 106), (157, 106), (158, 106), (18, 107), (26, 107), (27, 107), (32, 107),
(33, 107), (47, 107), (48, 107), (51, 107), (54, 107), (55, 107), (113, 107), (115, 107),
(122, 107), (123, 107), (124, 107), (126, 107), (127, 107), (131, 107), (145, 107), (146, 107),
(147, 107), (148, 107), (151, 107), (153, 107), (154, 107), (14, 108), (15, 108), (22, 108),
(26, 108), (27, 108), (32, 108), (33, 108), (56, 108), (77, 108), (82, 108), (105, 108),
(106, 108), (113, 108), (114, 108), (115, 108), (124, 108), (125, 108), (126, 108), (128, 108),
(131, 108), (146, 108), (147, 108), (152, 108), (153, 108), (154, 108), (1, 109), (6, 109),
(7, 109), (11, 109), (14, 109), (15, 109), (22, 109), (26, 109), (27, 109), (28, 109),
(32, 109), (33, 109), (34, 109), (38, 109), (52, 109), (53, 109), (56, 109), (57, 109),
(63, 109), (82, 109), (105, 109), (106, 109), (113, 109), (114, 109), (116, 109), (124, 109),
(146, 109), (148, 109), (152, 109), (153, 109), (154, 109), (2, 110), (105, 110), (106, 110),
(113, 110), (114, 110), (115, 110), (116, 110), (117, 110), (142, 110), (143, 110), (2, 113),
(3, 113), (5, 113), (6, 113), (7, 113), (8, 113), (11, 113), (13, 113), (14, 113),
(22, 113), (23, 113), (24, 113), (25, 113), (26, 113), (27, 113), (32, 113), (46, 113),
(47, 113), (48, 113), (51, 113), (55, 113), (81, 113), (113, 113), (114, 113), (115, 113),
(116, 113), (117, 113), (142, 113), (143, 113), (146, 113), (147, 113), (148, 113), (151, 113),
(152, 113), (153, 113), (154, 113), (155, 113), (156, 113), (2, 114), (14, 114), (15, 114),
(16, 114), (17, 114), (23, 114), (24, 114), (25, 114), (27, 114), (47, 114), (48, 114),
(51, 114), (52, 114), (78, 114), (81, 114), (82, 114), (113, 114), (114, 114), (115, 114),
(116, 114), (117, 114), (136, 114), (146, 114), (147, 114), (148, 114), (152, 114), (156, 114),
(2, 115), (3, 115), (31, 115), (33, 115), (35, 115), (36, 115), (37, 115), (38, 115),
(41, 115), (43, 115), (44, 115), (45, 115), (46, 115), (47, 115), (48, 115), (51, 115),
(52, 115), (53, 115), (54, 115), (55, 115), (61, 115), (86, 115), (114, 115), (115, 115),
(116, 115), (117, 115), (134, 115), (138, 115), (146, 115), (147, 115), (148, 115), (151, 115),
(152, 115), (153, 115), (156, 115), (3, 116), (12, 116), (33, 116), (34, 116), (45, 116),
(46, 116), (47, 116), (48, 116), (54, 116), (61, 116), (78, 116), (81, 116), (115, 116),
(117, 116), (122, 116), (131, 116), (135, 116), (151, 116), (152, 116), (153, 116), (154, 116),
(155, 116), (2, 117), (3, 117), (4, 117), (6, 117), (14, 117), (15, 117), (16, 117),
(17, 117), (18, 117), (21, 117), (23, 117), (24, 117), (26, 117), (33, 117), (34, 117),
(35, 117), (45, 117), (46, 117), (47, 117), (54, 117), (55, 117), (68, 117), (71, 117),
(72, 117), (75, 117), (76, 117), (78, 117), (81, 117), (86, 117), (108, 117), (111, 117),
(115, 117), (116, 117), (117, 117), (123, 117), (131, 117), (132, 117), (135, 117), (137, 117),
(138, 117), (145, 117), (146, 117), (151, 117), (152, 117), (154, 117), (155, 117), (156, 117),
(15, 118), (16, 118), (23, 118), (24, 118), (25, 118), (26, 118), (43, 118), (44, 118),
(45, 118), (46, 118), (47, 118), (48, 118), (56, 118), (65, 118), (66, 118), (67, 118),
(78, 118), (81, 118), (82, 118), (84, 118), (85, 118), (86, 118), (87, 118), (88, 118),
(91, 118), (107, 118), (115, 118), (123, 118), (135, 118), (138, 118), (145, 118), (146, 118),
(147, 118), (152, 118), (2, 121), (4, 121), (5, 121), (7, 121), (8, 121), (11, 121),
(12, 121), (14, 121), (15, 121), (16, 121), (17, 121), (23, 121), (24, 121), (25, 121),
(26, 121), (44, 121), (45, 121), (46, 121), (47, 121), (48, 121), (55, 121), (68, 121),
(91, 121), (92, 121), (108, 121), (111, 121), (112, 121), (113, 121), (114, 121), (115, 121),
(116, 121), (123, 121), (135, 121), (148, 121), (151, 121), (152, 121), (5, 122), (6, 122),
(7, 122), (8, 122), (11, 122), (15, 122), (16, 122), (17, 122), (23, 122), (24, 122),
(25, 122), (26, 122), (27, 122), (32, 122), (33, 122), (34, 122), (35, 122), (36, 122),
(37, 122), (38, 122), (42, 122), (47, 122), (55, 122), (56, 122), (68, 122), (91, 122),
(108, 122), (113, 122), (115, 122), (116, 122), (123, 122), (131, 122), (133, 122), (134, 122),
(135, 122), (145, 122), (152, 122), (8, 123), (11, 123), (12, 123), (23, 123), (24, 123),
(25, 123), (31, 123), (35, 123), (36, 123), (37, 123), (38, 123), (41, 123), (42, 123),
(43, 123), (46, 123), (47, 123), (48, 123), (55, 123), (56, 123), (68, 123), (91, 123),
(111, 123), (112, 123), (113, 123), (121, 123), (122, 123), (123, 123), (131, 123), (133, 123),
(134, 123), (135, 123), (136, 123), (137, 123), (141, 123), (145, 123), (148, 123), (152, 123),
(153, 123), (5, 124), (8, 124), (11, 124), (12, 124), (13, 124), (14, 124), (18, 124),
(23, 124), (24, 124), (25, 124), (26, 124), (31, 124), (32, 124), (35, 124), (37, 124),
(38, 124), (41, 124), (42, 124), (43, 124), (44, 124), (45, 124), (46, 124), (47, 124),
(48, 124), (51, 124), (52, 124), (56, 124), (57, 124), (58, 124), (68, 124), (71, 124),
(91, 124), (111, 124), (112, 124), (131, 124), (132, 124), (133, 124), (91, 125), (126, 125),
(127, 125), (128, 125), (131, 125), (132, 125), ]


def get_options_from(signs, all_options, cx, cy):
    options = []
    for x in range(cx - 1, 0, -1):
        if (x, cy) in signs:
            break
        if (x, cy) in all_options:
            options.append((x, cy, 3))
    for x in range(cx + 1, 16 * 10):
        if (x, cy) in signs:
            break
        if (x, cy) in all_options:
            options.append((x, cy, 2))
    for y in range(cy - 1, 0, -1):
        if (cx, y) in signs:
            break
        if (cx, y) in all_options:
            options.append((cx, y, 1))
    for y in range(cy + 1, 16 * 8):
        if (cx, y) in signs:
            break
        if (cx, y) in all_options:
            options.append((cx, y, 0))
    return options


def buildMaze(rnd):
    for n in range(50):
        all_options = set(ALL_SIGN_OPTION_TILES)
        signs = [(27, 84)]
        directions = []
        while len(signs) < 20:
            cx, cy = signs[-1]
            options = get_options_from(signs, all_options, cx, cy)
            nx, ny, arrow = rnd.choice(options)
            for x in range(cx, nx, -1 if nx < cx else 1):
                if (x, cy) in all_options:
                    all_options.remove((x, cy))
            for y in range(cy, ny, -1 if ny < cy else 1):
                if (cx, y) in all_options:
                    all_options.remove((cx, y))
            for y in range(ny // 8 * 8, ny // 8 * 8 + 8):
                for x in range(nx // 10 * 10, nx // 10 * 10 + 10):
                    if (x, y) in all_options:
                        all_options.remove((x, y))
            signs.append((nx, ny))
            directions.append(arrow)
        # We got a maze, now we just need to connect it to the egg
        below_egg_options = get_options_from(signs, all_options, 65, 5)
        from_last_sign_options = get_options_from(signs, all_options, signs[-1][0], signs[-1][1])
        connection_options = []
        for x, y, wrong_arrow in below_egg_options:
            for xx, yy, arrow in from_last_sign_options:
                if xx == x and yy == y:
                    connection_options.append((x, y, arrow, wrong_arrow))
        if not connection_options:
            continue
        nx, ny, arrow, wrong_arrow = rnd.choice(connection_options)
        signs.append((nx, ny))
        directions.append(arrow)
        signs.append((65, 5))
        directions.append(wrong_arrow ^ 1)

        for idx in range(5, len(directions) - 1):
            if rnd.randint(0, 100) < 20:
                directions[idx] |= 0x80  # Set as flying sign

        return signs, directions
    raise RuntimeError("Failed to build a maze in 50 tries.")


def patchMaze(rom, signs, directions):
    for n in range(0x100):
        rom.banks[0x0C][0x3800 + n] = 0
        rom.banks[0x0C][0x3900 + n] = 0

    for idx in range(len(signs)):
        x, y = signs[idx]
        arrow = directions[idx] if idx < len(directions) else 0x40

        re = RoomEditor(rom, (x // 10) | ((y // 8) << 4))
        re.entities.insert(0, (x % 10, y % 8, 0x4C))
        re.store(rom)

        rom.banks[0x0C][0x3800 + re.room] = arrow
        rom.banks[0x0C][0x3900 + re.room] = idx

    re = RoomEditor(rom, 0x06)
    re.removeEntities(0xDE)
    re.store(rom)

    # Patch the egg event to instantly open the egg
    rom.patch(0x19, 0x0AD1, ASM("jp nz, $4BCC"), ASM("jp $4BCC"))
    rom.patch(0x19, 0x0BD9, ASM("jr nz, $46"), ASM("jr $46"))
    rom.patch(0x19, 0x0CC3, ASM("call $27F2"), "", fill_nop=True)

    # Patch unused entity 4C into our custom sign.
    rom.patch(0x03, 0x004C, "41", "94")
    rom.patch(0x03, 0x0147, "00", "98")
    rom.patch(0x20, 0x00e4, "000000", ASM("dw $4000\ndb $0C"))

    rom.patch(0x0C, 0x0000, 0x0800, ASM("""
SignEntityHandler:

    call getSignData
    and  $80
    jr   z, .standingSign
    
    ; Flying sign
    ldh  a, [$FFE7] ; hFrameCounter
    rra
    rra
    rra
    and  $07
    ld   e, a
    ld   d, b
    ld   hl, flyingZPositions
    add  hl, de
    ld   a, [hl]

    ld   hl, $C310 ; wEntitiesPosZTable
    add  hl, bc
    ld   [hl], a

    ldh  a, [$FFE7] ; hFrameCounter
    and  $08
    ld   e, a
    ld   d, b
    ld   hl, wingSprites
    add  hl, de
    ld   c, $02
    call $3CE6 ; RenderActiveEntitySpritesRect

    ld   de, flyingSpriteData
    call $3BC0 ; RenderActiveEntitySpritesPair

    call $3B5A ; CheckLinkCollisionWithEnemy_trampoline  
    ret  nc
    ld   a, [$C146] ; wIsLinkInTheAir  
    and  a
    ret  z

    ld   a, [$C19F]  ; wDialogState  
    ld   hl, $C14F ; wInventoryAppearing  
    or   [hl]
    ld   hl, $C134 ; wDialogCooldown
    or   [hl]
    ret  nz

    ld   a, [$DB9A] ; wWindowY  
    cp   $80
    ret  nz

    ldh  a, [$FFCC] ; hJoypadState
    and  $10 ; J_A
    ret  z
    jp   signUsed

.standingSign:
    ld   de, spriteData
    call $3BC0 ; RenderActiveEntitySpritesPair

    ; Check collision and prevent link from moving on the sprite.
    call $3B5A ; CheckLinkCollisionWithEnemy_trampoline  
    jr   nc, .noCollision
    call $0CBE ; CopyLinkFinalPositionToPosition 
    call $0CB6 ; ResetPegasusBoots  
    call $178E ; ClearLinkPositionIncrement  
.noCollision:

    ld   a, [$C19F]  ; wDialogState  
    ld   hl, $C14F ; wInventoryAppearing  
    or   [hl]
    ld   hl, $C134 ; wDialogCooldown
    or   [hl]
    ret  nz

    ld   a, [$DB9A] ; wWindowY  
    cp   $80
    ret  nz

    ldh  a, [$FFCC] ; hJoypadState
    and  $10 ; J_A
    ret  z
    
    ldh  a, [$FF9E] ; hLinkDirection
    cp   $02
    ret  nz
    
    ldh  a, [$FF98] ; hLinkPositionX 
    ld   hl, $FFEE ; hActiveEntityPosX  
    sub  [hl]
    add  a, $08
    cp   $10
    ret  nc

    ldh  a, [$FF99] ; hLinkPositionY 
    ld   hl, $FFEF ; hActiveEntityPosY  
    sub  [hl]
    sub  a, $08
    cp   $04
    ret  nc

signUsed:
    call getSignNumber
    call $27D0 ; Enable SRAM
    ld   hl, $B020
    cp   [hl]
    jr   nz, wrongSign

correctSign:
    inc  [hl]
    call getSignData
    bit  6, a
    jr   nz, endSign
    ; Show the direction message
    and  $03
    add  a, $A9
    call $2373 ; OpenDialogInTable1 
    ret

endSign:
    ld   hl, $B020
    dec  [hl]
    ld   hl, $C280 ; wEntitiesStatusTable
    add  hl, bc
    ld   [hl], b

    ld   a, $DE
    call $3B86 ; SpawnNewEntity_trampoline  
    ret  c
    ld   hl, $C290 ; wEntitiesStateTable
    add  hl, de
    ld   a, $01
    ld   [hl], a

    ret

wrongSign:
    xor  a
    ld   [$B020], a 
    call getSignNumber
    and  a
    jr   z, firstSign

    ld   a, $1D   ; JINGLE_WRONG_ANSWER
    ldh  [$FFF2], a ; hJingle
    ld   a, $AD
    call $2373 ; OpenDialogInTable1
    ret

firstSign:
    ld   a, $01
    ld   [$B020], a
    jr correctSign

flyingZPositions:
    db   $0F, $0F, $10, $11, $11, $11, $10, $0F

spriteData:
    db $F0, $09
    db $F2, $29
flyingSpriteData:
    db $F4, $09
    db $F6, $29

wingSprites:
    db   $00, $FC, $22, $00, $00, $0C, $22, $20, $00, $FC, $22, $40, $00, $0C, $22, $60

getSignData:
    ld   hl, $C3E0 ; wEntitiesRoomTable
    add  hl, bc
    ld   l, [hl]
    ld   h, $78 ; sign data table at 7800, one byte per room.
    ld   a, [hl]
    ret

getSignNumber:
    ld   hl, $C3E0 ; wEntitiesRoomTable
    add  hl, bc
    ld   l, [hl]
    ld   h, $79 ; sign number table at 7900, one byte per room.
    ld   a, [hl]
    ret

""", 0x4000), fill_nop=True)

    rom.banks[0x3F][0x3700:0x3780] = utils.createTileData(""" 2222222
........
.3333333
.2222222
........
 .3.2222
 .3.2..2
 .3.2222
 .3.2.2.
2.3.2222
..3.....
.2222222
........
 2233.22
22233.22
 22233..
""" + """ 2222222
........
.3333333
.2222222
........
 .3.2222
 .3.2.2.
 .3.2222
 .3.2.2.
2.3.2222
..3.....
.2222222
........
 2233.33
22233.33
 22233..
""" + """
........
.3333333
.2222222
........
 .3.2222
 .3.2..2
 .3.2222
 .3.2.2.
2.3.2222
..3.....
.2222222
........
     .22
     .22
      ..
""" + """
........
.3333333
.2222222
........
 .3.2222
 .3.2.2.
 .3.2222
 .3.2.2.
2.3.2222
..3.....
.2222222
........
     .33
     .33
      ..""", " .32")
