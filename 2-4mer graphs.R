library(readxl)
library(dplyr)
double<-read_excel("/Users/smaguire/Desktop/Template switching/2-4mer frequency.xlsx",sheet=1)
triple<-read_excel("/Users/smaguire/Desktop/Template switching/2-4mer frequency.xlsx",sheet=2)
quad<-read_excel("/Users/smaguire/Desktop/Template switching/2-4mer frequency.xlsx",sheet=3)

expected.double= .25*.25*100
expected.triple= .25*.25*.25*100
expected.quad= .25*.25*.25*.25*100

process.mers<-function(data,expected){
  group_by(data,library) %>%
    mutate(total = sum(count), percentage = (count/total)*100) %>%
    group_by(code) %>%
    summarise(avg.per = mean(percentage), sd.per = sd(percentage)) %>%
    mutate(represent = avg.per/expected, rank = rank(avg.per)) %>%
    ggplot(.,aes(x=rank,y=represent))+geom_col()+
    geom_errorbar(aes(ymin = represent - sd.per, ymax = represent+sd.per))+
    geom_text(aes(label = code), y = -.2, angle = 90) + ylim(-.3,NA) + theme_bw() + 
    theme(axis.text.x = element_blank(),
          axis.ticks.x = element_blank()) +
    geom_hline(yintercept = 1,col='red',lty=2)+
    ylab("Relative Representation in Library")
}

process.mers.quad<-function(data,expected){
  group_by(data,library) %>%
    mutate(total = sum(count), percentage = (count/total)*100) %>%
    group_by(code) %>%
    summarise(avg.per = mean(percentage), sd.per = sd(percentage)) %>%
    mutate(represent = avg.per/expected, rank = rank(avg.per)) %>%
    filter(rank >= 226 | rank <= 30) %>%
    mutate(rank = rank(avg.per)) %>%
    ggplot(.,aes(x=rank,y=represent))+geom_col()+
    geom_errorbar(aes(ymin = represent - sd.per, ymax = represent+sd.per))+
    geom_text(aes(label = code), y = -.4, angle = 90, size = 2.5) + ylim(-.3,NA) + theme_bw() + 
    theme(axis.text.x = element_blank(),
          axis.ticks.x = element_blank()) +
    geom_hline(yintercept = 1,col='red',lty=2)+
    ylab("Relative Representation in Library")
}

process.mers(double,expected.double)
process.mers(triple,expected.triple)
process.mers.quad(quad,expected.quad)
