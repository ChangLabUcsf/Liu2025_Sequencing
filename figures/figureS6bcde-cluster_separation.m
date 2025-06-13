% Please rotate the 3D scatter plot to see the different angles in Panels b-d

clear all

N_NMF_use = 4;

file_name = 'fig1_nmf_clustering.mat';
work_path = GetWorkPath;

plot_order = [2,3,1,4];
cr_color = {'#F48024','#EC1848','#716FB2','#90BD31'};

load(fullfile(work_path,file_name));

B = data_NMF*W;  


%% Do PCA for the ERP
data_rs = resample(double(data_NMF),1,4);
data_rs = data_rs';
data_rs_centered = data_rs - mean(data_rs,1);
[coeff, score,~,~,var_exp] = pca(data_rs_centered);
data_rs_pca = data_rs_centered*coeff(:,1:4);

% project NMF base to the PC space
B_rs = resample(double(B),1,4);
B_rs = B_rs';
B_rs_demean = B_rs - mean(B_rs,1);
B_pca = B_rs_demean*coeff(:,1:4);

ind_cluster = cell(N_NMF_use,1);
FL_task = nmf_weights';
[FL_max,cl_max] = max(FL_task,[],1);

for cc = 1:max(cl_max)
    ind_cl = find(cl_max == cc);
    ind_cluster{cc} = ind_cl;
end

%% Plot PCA results

figure;
hold on
set(gca,'FontSize',14)

B_pca_angle = zeros(N_NMF_use);
dist_within = [];
dist_between = [];

for k = 1:N_NMF_use
    gi = plot_order(k);
    scatter3(data_rs_pca(ind_cluster{gi},2),data_rs_pca(ind_cluster{gi},3),data_rs_pca(ind_cluster{gi},4),40,hex2rgb(cr_color{k}),'filled','MarkerFaceAlpha',0.5);
    plot3([0 B_pca(gi,2)]*30,[0 B_pca(gi,3)]*30,[0 B_pca(gi,4)]*30,'color',cr_color{k},'LineWidth',1.5)
    
    for di = 1:length(ind_cluster{gi})
        for dj = di+1:length(ind_cluster{gi})
            dist_within = [dist_within;norm(data_rs_pca(ind_cluster{gi}(di),2:4)-data_rs_pca(ind_cluster{gi}(dj),2:4))];
        end
    end

    for j = k:N_NMF_use
        gj = plot_order(j);
        angle_this = acos(min(dot(B_pca(gi,2:4),B_pca(gj,2:4))/(norm(B_pca(gi,2:4))*norm(B_pca(gj,2:4))),1));
        B_pca_angle(gi,gj) = rad2deg(angle_this);
        B_pca_angle_plot_order(k,j) = rad2deg(angle_this);

        for di = 1:length(ind_cluster{gi})
            for dj = 1:length(ind_cluster{gj})
                dist_between = [dist_between;norm(data_rs_pca(ind_cluster{gi}(di),2:4)-data_rs_pca(ind_cluster{gj}(dj),2:4))];
            end
        end
    end
end
xlabel('PC2')
ylabel('PC3')
zlabel('PC4')
B_pca_angle_plot_order

% compare within group and between group distances
[p_rs, ~, stat_rs]= ranksum(dist_within,dist_between);
p_rs
stat_rs.zval

figure;
hold on
singlebox_vt(dist_within,'k',1);
singlebox_vt(dist_between,'k',2);

if p_rs < 0.001
    plot([[1 1],[2 2]],[12,[1 1]*12.5,12],'k')
    text(1.5,13,'***','FontSize',18,'HorizontalAlignment','center')
end
xlim([0.5,2.5])
set(gca,'XTick',[1,2],'XTickLabel',{'Within-cluster','Between clusters'})
ylabel('Euclidean distance in PC space')
ylim([0,14])
set(gca,'FontSize',14)


