# Ouvrir le fichier en lecture seule
file = open('tp.txt', "r")
#stocker les donnes dans une liste
donnes=[]
for line in file:
    fields =line.split('\t')
    donnes.append(fields)
    
num =len(donnes)
donnes=[x+[0] for x in donnes]
#--------resultat finale----------
donnes[0][9]="resultat"
for i in range(1,num-1):  
  if float(donnes[i][5])>=10:
    donnes[i][9]="admis" 
  elif float(donnes[i][5])<10 and (float(donnes[i][6])+float(donnes[i][7]))>=45:
    donnes[i][9]="admis avec dettes"
  else:
    donnes[i][9]="ajournee"
#---------------------------------------------
    
 #----la meilleure moyenne, la mauvaise-----   
a=float(donnes[1][5])
b=float(donnes[1][5])
for i in range(1,num-1):
  if(float(donnes[i][5])>a):
    a=float(donnes[i][5])
  if(float(donnes[i][5])<b):
    b=float(donnes[i][5])
#-------------------------------------------     
     
#-----------les statistiques----------------     
nbr_adm=0
nbr_adm_dt=0
nbr_ajr=0
for i in range(1,num-1):
 if donnes[i][9]=="admis":
  nbr_adm+=1
 if donnes[i][9]=="admis avec dettes":
  nbr_adm_dt+=1
 if donnes[i][9]=="ajournee":
  nbr_ajr+=1
#-----------------------------------------

#------les statiques--------------------
  totale=nbr_adm+nbr_adm_dt+nbr_ajr
  p_ad=100*nbr_adm/totale
  p_add=100*nbr_adm_dt/totale
  p_j=100*nbr_ajr/totale
#-------------------------------------
 
#------------------web-----------------
f=open('tp.htm','w')
ht="""<!DOCTYPE html>
  <head><title>Travail à domicile</title></head>
  <body>
  <br><br><h2 align='center'><I> Liste des Etudiants </I></h2><br><br>
  <table border=2 align="center" width='90%'>
  <tr style='color: black;'>
  <td width='15%' bgcolor='DARKSALMON'><div align='center'>Matricule </div></td>
  <td width='15%' bgcolor='DARKSALMON'><div align='center'>Nom </div></td>
  <td width='15%' bgcolor='DARKSALMON'><div align='center'>Prenom</div></td>
  <td width='10%' bgcolor='DARKSALMON'><div align='center'>M.S1 </div></td>
  <td width='10%' bgcolor='DARKSALMON'><div align='center'>M.S2</div></td>
  <td width='10%' bgcolor='DARKSALMON'><div align='center'>moy_annuel</div></td>
  <td width='10%' bgcolor='DARKSALMON'><div align='center'>credit s1</div></td>
  <td width='15%' bgcolor='DARKSALMON'><div align='center'>credits s2</div></td>
  <td width='15%' bgcolor='DARKSALMON'><div align='center'>Unite_acuise</div></td>
  <td width='15%' bgcolor='DARKSALMON'><div align='center'>resultat</div></td>"
  </tr> 
 """
f.write(ht)
#-----------------------------------------------------------------------

#-------------------------liste les etudiants---------------------------
for i in range(0,num-1):
   f.write("<TR>")  
   f.write("<td >")
   f.write(str(donnes[i][0]))
   f.write("</td>")  
   
 
   f.write("<TD>")
   f.write(str(donnes[i][1]))  
   f.write("</TD>")
     
   f.write("<TD>")
   f.write(str(donnes[i][2])) 
   f.write("</TD>")
     
   f.write("<TD>")
   f.write(str(donnes[i][3])) 
   f.write("</TD>")
   
   
   f.write("<TD>")
   f.write(str(donnes[i][4]))  
   f.write("</TD>")
  
   f.write("<TD>")
   f.write(str(donnes[i][5]))
   f.write("</TD>")
   
   f.write("<TD>")
   f.write(str(donnes[i][6]))
   f.write("</TD>")
  
   f.write("<TD>")
   f.write(str(donnes[i][7]))
   f.write("</TD>")
   
   f.write("<TD>")
   f.write(str(donnes[i][8]))
   f.write("</TD>")
   
   f.write("<TD>")
   f.write(str(donnes[i][9])) 
   f.write("</TD>")
 
   f.write("</TR>")
f.write("</table>")
#------------------------------------------
#------------ les static-------------------
f.write(str("<br>"))
f.write(str("<center>"))
f.write(str("la meilleure moyenne est :"))
f.write(str(a))
f.write(str("</center>"))


f.write(str("<center>"))
f.write(str("la mauvaiseest :"))
f.write(str(b))
f.write(str("</center>"))
f.write(str("<br>"))
f.write(str("<br>"))

f.write(str("<center>"))
f.write(str("le nombre admis :"))
f.write(str(nbr_adm))
f.write(str("</center>"))
 

f.write(str("<center>"))
f.write(str("le nombre admis avec dettes :"))
f.write(str(nbr_adm_dt))
f.write(str("</center>"))


f.write(str("<center>"))
f.write(str("le nombre ajourne :"))
f.write(str(nbr_ajr))
f.write(str("</center>"))
f.write(str("<br>"))
f.write(str("<br>"))

f.write(str("<center>"))
f.write(str("pourcentage admis :"))
f.write(str(round (p_ad,2))+"%")
f.write(str("</center>"))


f.write(str("<center>"))
f.write(str("pourcentage admis dettes :"))
f.write(str(round (p_add,2))+"%")
f.write(str("</center>"))


f.write(str("<center>"))
f.write(str("pourcentage ajourne :"))
f.write(str(round(p_j,2))+"%")
f.write(str("</center>"))
f.write(str("<br>"))


f.close()

   
   
  
       
      