clear
clc
close all
%load("allMatrices.mat")

%{
filetext = fileread('matricesPathList.txt');

expr = '[^\n]*Matrices*[^\n]*';

matches = regexp(filetext,expr,'match');

disp(matches{1})

folderExpr = '[^\n]*Matrices*[^\n]';
currFolderMatches = regexp(matches{1},folderExpr,'match');
y = regexp(matches{2},folderExpr,'match');
if (currFolderMatches{1} == y{1})
    disp("right")
end
%}
%% The Adventure of Wisteria Lodge - Arthur Conan Doyle
clear
clc
close all

addpath("Arthur Conan Doyle Matrices/")
book_table = readtable("ArthurConanDoyleTAOWL.csv");
book_matrix = table2array(book_table);

figure(1)
imagesc(book_matrix);
hold on;
% row grids
for i = 1:size(book_matrix, 1)
    plot([.5,size(book_matrix, 2)+.5],[i-.5,i-.5],'k-');
end
% column grids
for j = 1:size(book_matrix, 2)
    plot([j-.5,j-.5],[.5,size(book_matrix, 2)+.5],'k-');
end
h = colorbar;
ylabel(h,'Probability');
ax = gca;
set(gca,'xaxisLocation','top')
set(ax,'XTick', (1:size(book_matrix,2)))
set(ax,'YTick', (1:size(book_matrix,1)))
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '_', '#'];
set(ax,'XTickLabel',letters')
set(ax,'YTickLabel',letters')
title("The Adventure of Wisteria Lodge - Arthur Conan Doyle")

%% Arthur Conan Doyle
clear
clc
close all

addpath("Arthur Conan Doyle Matrices/")
book_table = readtable("ArthurConanDoyleComposite.csv");
book_matrix = table2array(book_table);

figure(1)
imagesc(book_matrix);
hold on;
% row grids
for i = 1:size(book_matrix, 1)
    plot([.5,size(book_matrix, 2)+.5],[i-.5,i-.5],'k-');
end
% column grids
for j = 1:size(book_matrix, 2)
    plot([j-.5,j-.5],[.5,size(book_matrix, 2)+.5],'k-');
end
h = colorbar;
ylabel(h,'Probability');
ax = gca;
set(gca,'xaxisLocation','top')
set(ax,'XTick', (1:size(book_matrix,2)))
set(ax,'YTick', (1:size(book_matrix,1)))
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '_', '#'];
set(ax,'XTickLabel',letters')
set(ax,'YTickLabel',letters')
title("Arthur Conan Doyle")

%% Pairwise distance calculation
clear
clc
close all

addpath("Mary Johnston Matrices/")
MJ_CTmp = readtable("MaryJohnstonComposite.csv");
MJ_C = table2array(MJ_CTmp);
MJ_1Tmp = readtable("MaryJohnstonLR.csv");
MJ_1 = table2array(MJ_1Tmp);
MJ_2Tmp = readtable("MaryJohnstonTLR.csv");
MJ_2 = table2array(MJ_2Tmp);

addpath("Arthur Conan Doyle Matrices/")
ACD_CTmp = readtable("ArthurConanDoyleComposite.csv");
ACD_C = table2array(ACD_CTmp);
ACD_1Tmp = readtable("ArthurConanDoyleTAOSH.csv");
ACD_1 = table2array(ACD_1Tmp);
ACD_2Tmp = readtable("ArthurConanDoyleTAOWL.csv");
ACD_2 = table2array(ACD_2Tmp);

mats_ind{1} = MJ_1;
mats_ind{2} = MJ_2;
mats_ind{3} = ACD_1;
mats_ind{4} = ACD_2;

% Change this to whatever you want
dist = @(A, B) norm(A - B, 'fro');
%dist = @(A, B) abs(norm(A, 2) - norm(B, 2));

disp(dist(ACD_C, ACD_1))
disp(dist(ACD_C, ACD_2))

disp(dist(MJ_C, MJ_1))
disp(dist(MJ_C, MJ_2))

disp(dist(ACD_C, MJ_1))
disp(dist(ACD_C, MJ_2))

dist_ind = zeros(numel(mats_ind));
for ii = 1:numel(mats_ind)
    for jj = 1:numel(mats_ind)
        dist_ind(ii, jj) = dist(mats_ind{ii}, mats_ind{jj});
    end
end
figure(1)
imagesc(dist_ind);
colormap gray; colorbar; hold on;
ax = gca;
set(gca,'xaxisLocation','top')
set(ax,'XTick', (1:size(dist_ind,2)))
set(ax,'YTick', (1:size(dist_ind,1)))
letters = ["Lewis Rand", "The Long Roll", "T. A. of Sherlock Holmes", "T. A. of Wisteria Lodge"];
set(ax,'XTickLabel',letters')
set(ax,'YTickLabel',letters')
title("Arthur Conan Doyle's Novels Versus Mary Johnston's")
set(gca,'xaxisLocation','top')
% row grids
for i = 1:size(dist_ind, 1)
    plot([.5,size(dist_ind, 2)+.5],[i-.5,i-.5],'k-');
end
% column grids
for j = 1:size(dist_ind, 2)
    plot([j-.5,j-.5],[.5,size(dist_ind, 2)+.5],'k-');
end



