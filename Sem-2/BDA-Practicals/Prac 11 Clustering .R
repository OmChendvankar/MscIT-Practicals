
# 1. Open & Read Iris data set
iris
View(iris)

newiris = iris
newiris
summary(newiris)
View(newiris)
newiris$Species = NULL
View(newiris)


#2.Apply kmeans to newiris, and 
#  store the clustering result in kc. 
# The cluster number is set to 3.

kc = kmeans(newiris,3)
kc

table(iris$Species, kc$cluster)

# 4.	Plot the clusters and their centres
plot(newiris[c("Sepal.Length", "Sepal.Width")], col=kc$cluster)

# Mark Cluster centers
points(kc$centers[,c("Sepal.Length", "Sepal.Width")], col=1:3, pch=6, cex=2)










