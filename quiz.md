
# 🎯 Python Quiz: Find the Python Equivalent

| #  | R Code | Topic |
|----|--------|-------|
| 1  | `ifelse(x > 5, "big", "small")` | Basic control flow |
| 2  | `v <- c(1,2,3,4)` | List |
| 3  | `v[1:3]` | Slicing a list |
| 4  | `for (i in 1:5) { print(i) }` | For-loop |
| 5  | `mean(df$Age, na.rm = TRUE)` | Mean with missing values |
| 6  | `length(unique(df$Sex))` | Number of unique values |
| 7  | `grep("^M", names)` | Regex matching |
| 8  | `gsub(" ", "_", names)` | Regex substitution |
| 9  | `lapply(names, nchar)` | List comprehension |
| 10 | `read.csv("titanic.csv")` | Reading CSV |
| 11 | `filter(df, Survived == 1)` | Filtering |
| 12 | `mutate(df, age2 = Age^2)` | Create new column |
| 13 | `group_by(df, Sex) %>% summarize(mean_age = mean(Age, na.rm=TRUE))` | Groupby aggregation |
| 14 | `arrange(df, desc(Age))` | Sorting descending |
| 15 | `select(df, Name, Age)` | Selecting columns |
| 16 | `nrow(df)` | Number of rows |
| 17 | `sum(is.na(df$Age))` | Counting missing values |
| 18 | `plot(df$Age, df$Fare)` | Scatterplot |
| 19 | `df$Sex <- as.factor(df$Sex)` | Changing dtype |
| 20 | `table(df$Survived)` | Counting values |
