
# This code covers the code presented in 
# Section 6.1 Linear Regression

income_input = as.data.frame(  read.csv("C:\\Users\\omche\\Documents\\GitHub\\MscIT-Practicals\\Sem-2\\BDA-Practicals\\Input files\\income.csv")   )
income_input[1:10,]

summary(income_input)

library(lattice)

splom(~income_input[c(2:5)],  groups=NULL, data=income_input, 
      axis.line.tck = 0,
      axis.text.alpha = 0)
# can use pairs() as used in earlier pracs

results <- lm(Income~Age + Education + Gender, income_input)
summary(results)

results2 <- lm(Income ~ Age + Education, income_input)
summary(results2)



# compute confidence intevals for the model parameters
confint(results2, level = .95)

# compute a confidence interval on the expected income of a person
Age <- 41
Education <- 12
new_pt <- data.frame(Age, Education)

conf_int_pt <- predict(results2, new_pt, level=.95, interval="confidence")
conf_int_pt 

# compute a prediction interval on the income of the same person
pred_int_pt <- predict(results2, new_pt, level=.95, interval="prediction")
pred_int_pt




