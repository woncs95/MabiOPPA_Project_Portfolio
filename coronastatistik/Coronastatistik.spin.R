install.packages("readxl", repos="http://cran.r-project.org/")
install.packages('tinytex', repos="http://cran.r-project.org/")
tinytex::install_tinytex()

library(tinytex)
library(readxl)

#Excel-Daten importieren #엑셀파일 불러오기 및 데이터 정의
data_xls = read_excel("Sterbefällenvergleich 2016-2020 nach Tagen.xlsx", na="Na")
data2_xls = read_excel("D - Überblick.xlsx", na="Na")
d_2020=data_xls[[2]][73:355]
d_2019=data_xls[[3]][73:355]
d_2018=data_xls[[4]][73:355]
d_2017=data_xls[[5]][73:355]


#2017-2020 사망자수 그래프
farbe=c("red","black","darkgrey","grey")
plot(d_2020,type="l",xlab="Tage vom 13.03 bis 22.12",ylab="Sterbefälle",col=farbe[1],ylim=c(1500,4000),main="Sterbefällevergleich in 2017-2020 und deren Durchschnitte")
lines(d_2019,col=farbe[2])
lines(d_2018,col=farbe[3])
lines(d_2017,col=farbe[4])
legend("topright",c(expression(2020),expression(2019),expression(2018),expression(2017)),lty=c(rep(1,4),2),col=farbe,cex=0.8)

#각 그래프의 평균을 도표로 나타냄 (목적: 사망자의 평균치에 영향이 있었나?)
m_2020=rep(mean(d_2020),length(d_2020))
m_2019=rep(mean(as.numeric(d_2019)),length(d_2019))
m_2018=rep(mean(as.numeric(d_2018)),length(d_2018))
m_2017=rep(mean(as.numeric(d_2017)),length(d_2017))
lines(m_2020,col="red")
lines(m_2019,col="black")
lines(m_2018,col="darkgrey")
lines(m_2017,col="grey")

#통계에러 수정
c_2020=data2_xls[[4]][2:284]
c_2020[4]=13
c_2020[5]=13
c_2020

#Gesamtzahl als Fall jeweiliger Tage umstellen (누적통계치를 각 일의 통계치로 계산함)
for(i in 0:281){
  c_2020[283-i]=as.numeric(c_2020[283-i])-as.numeric(c_2020[282-i])
}
c_2020

#Plot erstellen (코로나 사망자수와 전체 사망자수의 비율)
plot(as.numeric(c_2020)/as.numeric(d_2020)*100,xlab="Tage 13.03-20.12",ylab="Prozent(%)",type="l",col="red",main="Verhalten Coronabedingte Sterbefälle/Gesamtfälle")


