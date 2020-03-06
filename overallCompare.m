clear
clc
close all


%% Import all data

% I ignore the matricesPathList file because its contents are outdated.
% Instead, I will crawl through all '-Matrices' directories

mats_ind = cell(1, 1);
mats_comp = cell(1, 1);

k_ind = 1;
k_comp = 1;

% Crawls through the current directory its folders for .csv files. If the 
% file is a composite matrix, it goes in a seperate array from the
% individual book matrices.

allFiles = dir('* Matrices/*.csv');
for jj = 1:numel(allFiles)
    file = allFiles(jj);
    mat_tab = readtable([file.folder '/' file.name]);
    mat = table2array(mat_tab);
    if (endsWith(file.name, 'Composite.csv'))
        mats_comp{k_comp} = mat;
        k_comp = k_comp + 1;
    else
        mats_ind{k_ind} = mat;
        k_ind = k_ind + 1;
    end
end

names = ["Alice Caldwell Hegan Rice";"Arthur Conan Doyle";"Ellen Glasgow";"Emerson Hough";"George Barr McCutcheon";"Gilbert Parker";"Harold MacGrath";"Irving Bacheller";"John Fox";"Mary Johnston"];
shortNames = ["Rice";"Doyle";"Glasgow";"Hough";"McCutcheon";"Parker";"MacGrath";"Bacheller";"Fox";"Johnston"];

%% Pairwise distance definition

% Change this to whatever you want
dist = @(A, B) norm(A - B, 1);
%dist = @(A, B) abs(norm(A, 2) - norm(B, 2));

%% Comparing individual books with each other. 

% We should see something resembling a diagonal matrix
dist_ind = zeros(numel(mats_ind));
for ii = 1:numel(mats_ind)
    for jj = 1:numel(mats_ind)
        dist_ind(ii, jj) = dist(mats_ind{ii}, mats_ind{jj});
    end
end

% Better visualization is on the to-do list
figure(1)
imagesc(dist_ind); colorbar; hold on;
ax = gca; caxis([0 1.5])
set(gca,'xaxisLocation','top')
set(ax,'XTick', (1:4:size(dist_ind,2)))
set(ax,'YTick', (1:4:size(dist_ind,1)))
title("A^2-B^4")
% row grids
for i = 1:size(dist_ind, 1)
    plot([.5,size(dist_ind, 2)+.5],[i-.5,i-.5],'k-');
end
% column grids
for j = 1:size(dist_ind, 2)
    plot([j-.5,j-.5],[.5,size(dist_ind, 2)+.5],'k-');
end

%% Comparing authors' transitional matrices with each other

dist_comp = zeros(numel(mats_comp));
for ii = 1:numel(mats_comp)
    for jj = 1:numel(mats_comp)
        dist_comp(ii, jj) = dist(mats_comp{ii}, mats_comp{jj});
    end
end

% Better visualization is on the to-do list
figure(2)
imagesc(dist_comp); colorbar; hold on;
ax = gca;
set(gca,'xaxisLocation','top')
set(ax,'XTick', (1:size(dist_comp,2)))
set(ax,'YTick', (1:size(dist_comp,1)))
set(ax,'XTickLabel', shortNames')
set(ax,'YTickLabel', names')
title("Comparison between all authors")
% row grids
for i = 1:size(dist_comp, 1)
    plot([.5,size(dist_comp, 2)+.5],[i-.5,i-.5],'k-');
end
% column grids
for j = 1:size(dist_comp, 2)
    plot([j-.5,j-.5],[.5,size(dist_comp, 2)+.5],'k-');
end

%% Comparing authors' transitional matrices with their books

dist_both = zeros(numel(mats_comp), numel(mats_ind));
for ii = 1:size(dist_both, 1)
    for jj = 1:size(dist_both, 2)
        dist_both(ii, jj) = dist(mats_comp{ii}, mats_ind{jj});
    end
end

% Better visualization is on the to-do list
figure(3)
imagesc(dist_both); colorbar; hold on;
ax = gca;
set(gca,'xaxisLocation','top')
set(ax,'XTick', (1:4:size(dist_both,2)))
set(ax,'YTick', (1:size(dist_both,1)))
set(ax,'YTickLabel', names')
title("Comparison between all authors and all books")
% row grids
for i = 1:size(dist_both, 1)
    plot([.5,size(dist_both, 2)+.5],[i-.5,i-.5],'k-');
end
% column grids
for j = 1:size(dist_both, 2)
    plot([j-.5,j-.5],[.5,size(dist_both, 2)+.5],'k-');
end



