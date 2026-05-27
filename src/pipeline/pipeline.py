from src.transform.features import aplicar_pipeline, CLEANING,ENGINEERING


def pipeline(df):
   return(
       df
       # CLEANING
       .pipe(aplicar_pipeline, CLEANING)
       # ENGINEERING
       .pipe(aplicar_pipeline, ENGINEERING)
   )