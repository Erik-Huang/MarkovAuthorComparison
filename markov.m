clear;
clc;
close all;

A_tab = readtable('IB_markov.csv');
B_tab = readtable('M_markov.csv');
C_tab = readtable('M_markov2.csv');
A = table2array(A_tab);
B = table2array(B_tab);
C = table2array(C_tab);
