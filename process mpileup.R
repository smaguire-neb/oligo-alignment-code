library(stringr)
library(ggplot2)
library(tidyr)
library(dplyr)


get.count<-function(string,char, ref.char, countvec, count.ref){
  count <- str_count(string, char)
  if(tolower(ref.char) == char)
    count <- count + count.ref
  c(countvec,count)
}
processFile = function(filepath) {
  
  char <- vector()
  ref.char <-vector()
  
  a.num <-vector()
  g.num <-vector()
  t.num <-vector()
  c.num <-vector()
  
  con = file(filepath, "r")
  while ( TRUE ) {
    line = readLines(con, n = 1)
    if ( length(line) == 0 ) {
      break
    }
      x<-str_split(line,pattern = "\t", simplify = T )
      char<-c(char, x[1,2])
      ref.char<-c(ref.char, x[1,3])
      
      total.ref<-str_count(x[1,5],",")
      a.num <- get.count(x[1,5],"a",x[1,3],a.num,total.ref)
      g.num <- get.count(x[1,5],"g",x[1,3],g.num,total.ref)
      c.num <- get.count(x[1,5],"c",x[1,3],c.num,total.ref)
      t.num <- get.count(x[1,5],"t",x[1,3],t.num,total.ref)
      
  }
  close(con)
  data<-
    data.frame(char,ref.char,a.num,g.num,c.num,t.num) %>%
    group_by(char) %>%
    mutate(total = sum(a.num,g.num,c.num,t.num), 
           A = (a.num/total)*100,
           G = (g.num/total)*100,
           C = (c.num/total)*100,
           T = (t.num/total)*100)
  data.plot<- 
    data %>%
    select(char,ref.char,A,G,C,T) %>%
    gather(key = nuc, value = percentage, A,G, C, T)

  gg1<-ggplot(data.plot,aes(x=char,y = percentage, fill = nuc))+geom_col()+
    geom_text(y=-2,aes(label=ref.char)) + theme_bw() +
    xlab("Position on Reference") +
    ylab("Percentage of Reads") +
    labs(fill = "Nucleotide")+
    theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank())
  print(gg1)
  return(data)
}

'mpileupout_lib2.txt'
system("sed -n '44,51p' mpileupout_lib2.txt >mpileup_lib2_small.txt")
filepath <- "mpileup_lib2_small.txt"
data<-processFile(filepath)
ggsave("lib4.tiff")

bias.index<-function(data){
  bias<-vector()
  for(row in 1:nrow(data)){
    bias <- c(bias,sqrt((data$A[row]-25)^2 + (data$G[row]-25)^2 + (data$C[row]-25)^2 + (data$T[row]-25)^2))
  }
  bias
}
bias.index(data)


