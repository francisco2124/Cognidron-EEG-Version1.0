import pandas as pd


class pandasPrueva():

    def prueva(self):

        Lista = [["Nobre","Edad","Sexo"], ["Javier", 23,"h"],["Erika", 20,"M"]]

        data = pd.DataFrame(Lista[1:],columns=Lista[0])

        data.head()

        data.to_csv("C:\CogniDron-EEG\Reportes_De_Potencias\Reporte1.csv", index=False)



if __name__ == "__main__":
    x = pandasPrueva()
    x.prueva()