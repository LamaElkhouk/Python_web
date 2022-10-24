# import modules
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import io

# Title
st.title("Projet")
st.write("Mon projet consiste à étudier un jeu de données présentant des individus, des étudiants pour étudier et analyser leur santé mental et je souhaite savoir si il y'a un lien entre les differents resultats de ses étudiants et leurs note moyenne !Si oui, serait-il possible d'identifier quels sont le/le(s) groupe(s) d'étudiant(s) le(s) plus toucher par cette influence")
df= pd.read_csv('Student_Mental_health.csv')
code = '''
# import modules
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import io

df= pd.read_csv('Student_Mental_health.csv')

 '''
st.code(code, language='python')

# number of rows
rows = len(df.axes[0])
# number of columns
cols = len(df.axes[1])


st.write("Number of Rows: ", rows)
st.write("Number of Columns: ", cols)
st.write(df)


st.write("Les données (variables) constituant mon dataframe")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

code='''
df= pd.read_csv('Student_Mental_health.csv')
# number of rows
rows = len(df.axes[0])
# number of columns
cols = len(df.axes[1])


st.write("Number of Rows: ", rows)
st.write("Number of Columns: ", cols)
st.write(df)


st.write("Les données (variables) constituant mon dataframe")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)'''
st.code(code, language='python')

st.write("""
On étudie un échantillon de 101 étudiants ayant 11 caractéristiques:

=> personnelles :

age, domaine d'études, son année d'étude, sa moyenne globale (CGPA = A=4 B=3 C=2 D=1 et F=0) et son état civil.

=> En rapport avec leur santé mentale:

Est ce qu'ils sont en dépression? ressent-ils de l'anxiété ? ont-ils déja eu une crise de panique? ont-ils consulté un spécialiste pour un traitement?

=> Il y'a également la toute premiere caractéristique "timestamp",qui selon n'est pas une variable pertinente pour l'étude, elle représente la date et heure à laquel chaque étudiant à été interroger.

Le dataframe est constitué principalement de variables qualitatives de type Object (string) et d'une variable quantitative "l'age", qui est de type float.
""")

st.write("Dataframe en version plus simplifier")


code ='''
#J'ai renommé les noms de variables
df.rename(columns = {'Choose your gender':'gender','What is your course?':'course','Your current year of Study':'current year','What is your CGPA?':'CGPA','Do you have Depression?':'depression', 'Do you have Anxiety?':'anxiety','Do you have Panic attack?':'panic attack','Did you seek any specialist for a treatment?':'specialist for a treatment'}, inplace = True)

note_moyenne=[]

for i in df['CGPA']:
    i=i.split()
    moyenne=(float(i[0])+float(i[2]))/2
    note_moyenne.append(moyenne)



#df.insert(6,"note moyenne",1)

df['note moyenne']=note_moyenne

df.head(5)


#sb.catplot(x="note_moyenne", y="depression", data = df, kind= "box", height=7)

'''
st.code(code, language='python')


#J'ai renommé les noms de variables
df.rename(columns = {'Choose your gender':'gender','What is your course?':'course','Your current year of Study':'current year','What is your CGPA?':'CGPA','Do you have Depression?':'depression', 'Do you have Anxiety?':'anxiety','Do you have Panic attack?':'panic attack','Did you seek any specialist for a treatment?':'specialist for a treatment'}, inplace = True)



note_moyenne=[]

for i in df['CGPA']:
    i=i.split()
    moyenne=(float(i[0])+float(i[2]))/2
    note_moyenne.append(moyenne)



#df.insert(6,"note moyenne",1)

df['note moyenne']=note_moyenne
st.write(df.head(5))
#sb.catplot(x="note_moyenne", y="depression", data = df, kind= "box", height=7)

st.write("Peut-on décrire la note moyenne par rapport à depression ? panic attack et anxiety?")

code=''' df['note moyenne'].describe() '''
st.code(code, language='python')
st.write(df['note moyenne'].describe())


st.write("""
la moyenne des notes est de 3.35

l'écart-type : 0.58

donc les notes vont de 2.77 à 3.93 qui sont plutot de bonne notes!

max => 3.75 == 100% 0.58 represente 15.46% de 3.75% qui est plutot faible mais on ne peut pas vraiment conclure qu'elle soit significative

Correlation entre la variable qui décrit la note_moyenne de chaque étudiant avec la variable chacune des variables qui décrit si oui ou non il est anxieux, anxiety, si oui ou non il est en depression et si oui ou non il a des crises de panique, panic attack

 """)

code=''' 
#sb.catplot(y="note moyenne", x="anxiety", data= df, kind="bar", height=5, aspect=1)
sb.catplot(y="anxiety", x="note moyenne", data = df, kind= "box", height=4)'''
st.code(code, language='python')

 #sb.catplot(y="note moyenne", x="anxiety", data= df, kind="bar", height=5, aspect=1)
fig=sb.catplot(y="anxiety", x="note moyenne", data = df, kind= "box", height=4)
st.pyplot(fig)


st.write("on a deux valeurs aberrantes => il existe des individus ne souffrant d'anxiété et n'ayant pas de bonnes notes")
code=''' 
sb.catplot(y="depression", x="note moyenne", data = df, kind= "box", height=7)'''
st.code(code, language='python')

fig=sb.catplot(y="depression", x="note moyenne", data = df, kind= "box", height=7)
st.pyplot(fig)

st.write("on a deux valeurs aberrantes => deux individus ayant une note inferieur a 2.5 et ne souffre pas d'anxiété ...")
code=''' 
sb.catplot(y="panic attack", x="note moyenne", data = df, kind= "box", height=7)'''
st.code(code, language='python')

fig=sb.catplot(y="panic attack", x="note moyenne", data = df, kind= "box", height=7)
st.pyplot(fig)

st.write("quatres valeurs aberrantes => il existe des étudiants ayant des notes inferieur a 2.5 , certain d'entre eux souffre de crise de panic d'autres non")
st.write("Suppresion des valeurs aberrantes")

code=''' 
new_df = df[ df['note moyenne'] > 2.5] 
sb.catplot(x="note moyenne", y="depression", data = new_df, kind= "box", height=7)'''

st.code(code, language='python')
new_df = df[ df['note moyenne'] > 2.5] 
fig=sb.catplot(x="note moyenne", y="depression", data = new_df, kind= "box", height=7)
st.pyplot(fig)
st.write(""" 
absence de mediane => 50 % souffrent de depression et les autres 50% non

50% ont des bonnes notes se situant entre 3.6 et 3.8 !

""")

code='''
sb.catplot(x="note moyenne", y="anxiety", data = new_df, kind= "box", height=7)'''
st.code(code, language='python')

fig=sb.catplot(x="note moyenne", y="anxiety", data = new_df, kind= "box", height=7)
st.pyplot(fig)

st.write(""" 
absence de mediane => 50 % souffrent d'anxiété et les autres 50% non

50% ont des bonnes notes se situant entre 3.6 et 3.8 !

""")

code='''sb.catplot(x="note moyenne", y="panic attack", data = new_df, kind= "box", height=7)'''
st.code(code, language='python')

fig=sb.catplot(x="note moyenne", y="panic attack", data = new_df, kind= "box", height=7)
st.pyplot(fig)

st.write(""" 
absence de mediane => 50 % souffrent de crise de panique et les autres 50% non

50% ont des bonnes notes se situant entre 3.6 et 3.8 !

J'ai converti mes variables quantitatives en variables qualitatives

""")

code=''' 
#J'ai remplacé les 'yes' et 'No' par 1 et 0
df['depression']= df['depression'].replace(['Yes','No'],[1,0])
df['anxiety']= df['anxiety'].replace(['Yes','No'],[1,0])
df['panic attack']= df['panic attack'].replace(['Yes','No'],[1,0])
df['specialist for a treatment']= df['specialist for a treatment'].replace(['Yes','No'],[1,0])
df['Marital status']= df['Marital status'].replace(['Yes','No'],[1,0])
'''
st.code(code, language='python')

#J'ai remplacé les 'yes' et 'No' par 1 et 0
df['depression']= df['depression'].replace(['Yes','No'],[1,0])
df['anxiety']= df['anxiety'].replace(['Yes','No'],[1,0])
df['panic attack']= df['panic attack'].replace(['Yes','No'],[1,0])
df['specialist for a treatment']= df['specialist for a treatment'].replace(['Yes','No'],[1,0])
df['Marital status']= df['Marital status'].replace(['Yes','No'],[1,0])

st.write("y'a t-il correlation entre les notes et la depression?")

code='''
sb.catplot(x="note moyenne", y="anxiety", data= df, kind="bar", height=10)
 '''
st.code(code, language='python')

fig=sb.catplot(x="note moyenne", y="anxiety", data= df, kind="bar", height=10)
st.pyplot(fig)

st.write(""" 
36 % ont des notes se situant aux alentours de 3.75

les ecarts-types sont énormes donc les deux variables ne sont pas correler

plus un étudiant à de bonnes notes, plus il souffre anxiété

""")
code=''' sb.catplot(x="note moyenne", y="depression", data= df, kind="bar", height=10)'''
st.code(code, language='python')

fig=sb.catplot(x="note moyenne", y="depression", data= df, kind="bar", height=10)
st.pyplot(fig)

st.write("""
30 % ont des notes se situant aux alentours de 3.75

les ecarts-types sont énormes donc les deux variables ne sont pas correler

plus un étudiant à de bonnes notes, plus il souffre de depression

 """)

code=''' sb.catplot(x="note moyenne", y="panic attack", data= df, kind="bar", height=10)'''
st.code(code, language='python')

fig=sb.catplot(x="note moyenne", y="panic attack", data= df, kind="bar", height=10)
st.pyplot(fig)

st.write(""" 
40 % ont des notes se situant aux alentours de 3.75

les ecarts-types sont énormes donc les deux variables ne sont pas correler

qu'ils aient de bonne notes ou pas , il y'a des etudiant qui souffre crise de panique

""")

st.write("matrice et heatmap")
code=''' 
matrice=df.corr()
matrice'''
st.code(code, language='python')


matrice=df.corr()
st.write(matrice)


code='''
plt.figure(figsize=(15,6))
sb.heatmap(matrice, annot=True)'''
st.code(code, language='python')

fig=plt.figure(figsize=(15,6))
sb.heatmap(matrice, annot=True)

st.write(fig)

st.write(""" 
il est vrai que la note n'a pas d'influence sur l'anxité, la depression et la crise de panique..mais de ce qu'on peut en conclure de notre heatmap ! la santé mentale est plus relier a sa vie sentimentale et non lié a ses études, les étudiants souffrent de dépression à cause de leur celiba... mais cela n'influe en aucun cas les notes..
""")

st.write("""
Conclusion

Comme on a pu le constaté avec ce jeu de données qui presente la situation de 100 étudiants , plus un étudiants est anxieux , a des crise de panique ou/et qui est en depression, il aura tendance à avoir de bonnes notes, cela peut etre expliquer par le fait d'avoir peur d'échouer ! ou alors que sa dépression est dû a d'autres facteurs et que cela n'influence pas ses études , que les étudiants qui n'ont pas de bonnes notes ne sont peut etre pas interessés par ce qu'ils font et donc souhaite faire autres choses de leurs vie ou voir meme se réorienté!

s'ajoute a cela le fait qu'on a fait cette etude uniquement sur 101 étudiants , il aurait fallut avoir plus de données, voir verié et interroger des étudiants de d'autres région ?

donc pour conclure, on ce qui concerne cet échantillon, la santé mentale n'a finalement pas un effet negatif sur les notes de la majorité des étudiants

""")