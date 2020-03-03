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

%% Pairwise distance definition

% Change this to whatever you want
dist = @(A, B) norm(A - B, 'fro');

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
pcolor(dist_ind); colorbar

%% Comparing authors' transitional matrices with each other

dist_comp = zeros(numel(mats_comp));
for ii = 1:numel(mats_comp)
    for jj = 1:numel(mats_comp)
        dist_comp(ii, jj) = dist(mats_comp{ii}, mats_comp{jj});
    end
end

% Better visualization is on the to-do list
figure(2)
pcolor(dist_comp); colorbar

%% Comparing authors' transitional matrices with their books

dist_both = zeros(numel(mats_comp), numel(mats_ind));
for ii = 1:size(dist_both, 1)
    for jj = 1:size(dist_both, 2)
        dist_both(ii, jj) = dist(mats_comp{ii}, mats_ind{jj});
    end
end

% Better visualization is on the to-do list
figure(3)
pcolor(dist_both); colorbar